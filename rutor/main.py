# -*- coding: utf8 -*-
import traceback

from bs4 import BeautifulSoup
from couchpotato.core.helpers.encoding import tryUrlencode
from couchpotato.core.helpers.variable import tryInt
from couchpotato.core.logger import CPLog
from couchpotato.core.media._base.providers.torrent.base import TorrentProvider
from couchpotato.core.media.movie.providers.base import MovieProvider

import re


log = CPLog(__name__)


class rutor(TorrentProvider, MovieProvider):

    baseurl = 'http://rutor.is/'
    urls = {
        'test' : 'http://rutor.is',
        'detail' : baseurl + 'torrent/%s',
        'search' : baseurl + 'search/0/0/100/8/%s',
        'download' : baseurl + 'download/%s',
    }

    http_time_between_calls = 1 #seconds
    cat_backup_id = None

    def _searchOnTitle(self, title, movie, quality, results):

        log.debug('Searching rutor for %s' % (title))

        url = self.urls['search'] % (title.replace(':', ' '))
        data = self.getHTMLData(url)

        log.debug('Received data from rutor')

        if data:
            log.debug('Data is valid from rutor')
            html = BeautifulSoup(data)

            try:
		result_table = html.find('div', attrs = {'id' : 'index'})
                result_table = result_table.find('table')
                if not result_table:
                    log.debug('No table results from rutor')
                    return

                torrents = result_table.find_all('tr', attrs = {'class' : ['gai','tum']})
                for result in torrents:
                    all_cells = result.find_all('td')
		    dl_cell = all_cells[1].find_all('a')[0]
		    title_cell = all_cells[1].find_all('a')[2]
                    size_cell = all_cells[3]
                    seed_cell = all_cells[4].find('span', attrs = {'class' : 'green'}).getText()
                    leech_cell = all_cells[4].find('span', attrs = {'class' : 'red'}).getText()
		    
		    seed_cell = seed_cell.replace(u'&nbsp;', '')
		    leech_cell = leech_cell.replace(u'&nbsp;','')

		    size_cell = size_cell.getText()
                    topic_id = dl_cell['href']
                    topic_id = topic_id.replace('/download/', '')
                    
                    size = size_cell.replace(u'&nbsp;GB','')
		

                    # Workaround for filtering 1080p and 720p by CouchPotato: BDRip is a source not a video quality!
                    title = title_cell.getText().replace('BDRip', '')
                    title = re.sub('^.*? / ', '', title)
                    title = re.sub('[\[\]\(\)/ ]', '.', title)
                    title = re.sub(':', '-', title)
                    title = re.sub('\.\.+', '.', title)

                    torrent_name = title
                    torrent_size = self.parseSize( size )
                    torrent_seeders = tryInt(seed_cell)
                    torrent_leechers = tryInt(leech_cell)
                    torrent_detail_url = self.urls['detail'] % topic_id
                    torrent_url = self.urls['download'] % topic_id

                    log.debug('Title %s' % (torrent_name))
                    log.debug('Size %s' % (torrent_size))   
                    log.debug('Forum %s' % (torrent_detail_url))
                    log.debug('Dl %s' % (torrent_url))
                    log.debug('seed %d' % (torrent_seeders))
                    log.debug('leech %d' % (torrent_leechers))
                    
                    results.append({
                        'id': topic_id,
                        'name': torrent_name,
                        'size': torrent_size,
                        'seeders': torrent_seeders,
                        'leechers': torrent_leechers,
                        'url': torrent_url,
                        'detail_url': torrent_detail_url,
                    })
                    

            except:
                log.error('Failed to parse rutor: %s' % (traceback.format_exc()))
