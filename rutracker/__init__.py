from .main import rutracker

def autoload():
  return rutracker()

config = [{
  'name': 'rutracker',
  'groups': [
    {
      'tab': 'searcher',
      'list': 'torrent_providers',
      'name': 'Rutracker',
      'description': '<a href="https://rutracker.cr">Rutracker</a>',
      'wizard': True,
      'icon': 'AAABAAEAEBAAAAEAGABoAwAAFgAAACgAAAAQAAAAIAAAAAEAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADg4ODLy8vd3d0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADPz8+KioqgoKDb29vj4+Pf39/q6uoAAAAAAAAAAAAAAAAAAAAAAAAAAADe3t7b29vS0tL29vZOTk5paWlycnJ8fHy8vLwAAAAAAADt7e3c3Nzg4ODc3NympqbDw8OIiIjj4+PtTUD8393///////////+8vLwAAAAAAADU1NSgoKCampqUlJSCgoLz8/NKSUni4uLpJxnqOCrwZ1z2oZvj4+PPz88AAAAAAADr6+vx8fGmpqaurq7P9dn///9paWm9WlPhIBLpIRLpIRL///9XV1fOzMwAAAAAAADg4OD///9D1miK5qEQyz////8+PT1GLCuTFQvNHhHhIBLrtrPPz8+kpKQAAAAAAADh4eH8/PwTzEEQyz8Qyz+M5qL///9sbGxWEQyZJBy9WlO7cmzU1NSioqIAAAAAAADDw8P///8Qyz8Qyz8Qyz8Qyz9r34j///+emZk+PT1lZWTS0tKmpqbg4OAAAAAAAADY2NiP56V74pVh3YAQyz////+mpqZYN9DDtfT///+zoPbf39+xsbEAAAAAAAAAAAAAAAAAAAAAAAAAAAA31F/t7e2YmJhMIedAEulRJ+uhivSYmJi8vLwAAAAAAAAAAAAAAAAAAAAAAADj4+P+/v7IyMh2XdBAEulAEulAEunHuflKSUmYmJgAAAAAAAAAAAAAAAAAAAAAAAAAAADg4ODt7e329vZaM+tAEulAEulRJ+v///9+fn7d3d0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADd3d2plPV4WO/////////////e3t7j4+MAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADr6+v///////+/v7/i4uLu7u4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADV1dXp6ekAAAAAAAAAAAAAAAAAAAAAAAD+PwAA/gMAAPgDAAAAAwAAAAMAAAADAAAAAwAAAAMAAAADAAAABwAA8AcAAOAHAADwAwAA/AMAAPwPAAD/PwAA',
      'options': [
        {
          'name': 'enabled',
          'type': 'enabler',
          'default': False,
        },
        {
          'name': 'username',
          'default': '',
        },
        {
          'name': 'password',
          'default': '',
          'type': 'password',
        },
        {
          'name': 'seed_ratio',
          'label': 'Seed ratio',
          'type': 'float',
          'default': 1,
          'description': 'Will not be (re)moved until this seed ratio is met.',
        },
        {
          'name': 'seed_time',
          'label': 'Seed time',
          'type': 'int',
          'default': 48,
          'description': 'Will not be (re)moved until this seed time (in hours) is met.',
        },
        {
          'name': 'extra_score',
          'advanced': True,
          'label': 'Extra Score',
          'type': 'int',
          'default': 0,
          'description': 'Starting score for each release found via this provider.',
        }
      ],
    },
  ],
}]
