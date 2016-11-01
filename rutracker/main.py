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


class rutracker(TorrentProvider, MovieProvider):

    baseurl = 'https://rutracker.cr/forum/'
    urls = {
        'test' : 'https://rutracker.cr',
        'login' : baseurl + 'login.php',
        'login_check': baseurl + 'profile.php',
        'detail' : baseurl + 'viewtopic.php?t=%s',
        'search' : baseurl + 'tracker.php?f=100,101,187,1900,208,209,2090,2091,2092,2093,2199,2200,2221,312,313,521,905,930&o=4&nm=%s',
        'download' : baseurl + 'dl.php?t=%s',
    }

    http_time_between_calls = 1 #seconds
    cat_backup_id = None

    def _searchOnTitle(self, title, movie, quality, results):

        log.debug('Searching rutracker for %s' % (title))

        url = self.urls['search'] % (title.replace(':', ' ').encode("ascii", "xmlcharrefreplace"))
        data = self.getHTMLData(url).decode('cp1251')

        log.debug('Received data from rutracker')
        if data:
            log.debug('Data is valid from rutracker')
            html = BeautifulSoup(data)

            try:
                result_table = html.find('table', attrs = {'class' : 'forumline tablesorter'})
                if not result_table:
                    log.debug('No table results from rutracker')
                    return

                torrents = result_table.find_all('tr', attrs = {'class' : 'tCenter hl-tr'})
                for all_cells in torrents:
                    # all_cells = result.find_all('td')

                    title_cell = all_cells.find('a', attrs = {'class' : 'tLink'})
                    size_cell = all_cells.find('td', attrs = {'class' : 'tor-size'})
                    seed_cell = all_cells.find('b', attrs = {'class' : 'seedmed'})
                    leech_cell = all_cells.find('td', attrs = {'class' : 'leechmed'})
		    leech_cell = leech_cell.find('b')

		    size_cell = size_cell.find('a').getText()
		    
                    topic_id = title_cell['href']
                    topic_id = topic_id.replace('viewtopic.php?t=', '')
                    
                    size = size_cell.replace(u' GB ↓','')
		

                    # Workaround for filtering 1080p and 720p by CouchPotato: BDRip is a source not a video quality!
                    title = title_cell.getText().replace('BDRip', '')
                    title = re.sub('^.*? / ', '', title)
                    title = re.sub('[\[\]\(\)/ ]', '.', title)
                    title = re.sub(':', '-', title)
                    title = re.sub('\.\.+', '.', title)

                    torrent_name = title
                    torrent_size = self.parseSize( size )
                    torrent_seeders = tryInt(seed_cell.getText())
                    torrent_leechers = tryInt(leech_cell.getText())
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
                log.error('Failed to parse rutracker: %s' % (traceback.format_exc()))

    def getLoginParams(self):
        log.debug('Getting login params for rutracker')
        return {
            'login_username': self.conf('username'),
            'login_password': self.conf('password'),
            'login': u'%E2%F5%EE%E4'
        }

    def loginSuccess(self, output):
        log.debug('Checking login success for rutracker: %s' % ('True' if ('forum/profile.php?mode=viewprofile' in output.lower()) else 'False'))
        return 'forum/profile.php?mode=viewprofile' in output.lower()

    loginCheckSuccess = loginSuccess
