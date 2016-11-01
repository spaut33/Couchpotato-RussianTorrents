from .main import rutor

def autoload():
  return rutor()

config = [{
  'name': 'rutor',
  'groups': [
    {
      'tab': 'searcher',
      'list': 'torrent_providers',
      'name': 'rutor',
      'description': '<a href="http://rutor.is">rutor</a>',
      'wizard': True,
      'icon': 'AAABAAEAEBAAAAEAGABoAwAAFgAAACgAAAAQAAAAIAAAAAEAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAc4AAMwHNdcQ4vsN3fYS2fUY3fUe3fMj4fkk4fco4PYo5fgk7f5gp8ZuZZtsa59FIXZEGm4kh74PyeoLGp8NHK4PHrwQHr8VIb8XJL4bJrUcKJ8optEdtPMBGcQAIcXeZAPVYwdA3MQFf8EDAJoFAMEEAM0AANIAAM4AAM0EAL8CAI8bXaEV1/cBHMsGDNTVWAOodTIU5/ELuOAJM6sEALsIAMoEALkCBbgFALUGAKshgMcvpNUTzOoFQNIFANqxQgBpkmgKue8IT8UUy+8HO7MHPb8Gt+IG3vQHm9YKi84X4foKI7kRl+AWiMwSDYyxjXZAy84HdNYEALcPguYM+vsL6PgGl/wBWN4K1/EF//8LbdQEALgEVc41zMp0YC+t0N0XxPcCIbwGAMkGGOUGUvQKPPUEANsIU9ENvvAJw/ULnekGAr8FJcIUzfRycEZwzuMFnuYEArQCAdYDANYHAMQFAMwGPcwM2vsHU/QKPegLwvYEEckFBrsOt/Y+kYky5/YGgNAGAKkHAc4JMssSoN0GTb0L2/gHYPkCAPkFKOMP0fIHGc0EAKwLgNAq3OMd/P0Al9ACBqQCAMALbOMG+/8E8v0KjugBAO4CAPAGQ9MNyPYEB8QBAKQCe8cW9//T+/09+/8Aqd8GIbIFAMAKbuUG6f8Ht/IFFeEAAMYPqeYMhOEGB6oCgtUY5fuG0tv//vzs+PlQ9fwAw+4CLLoIALgJR+EFU+wEFcweZNAkquMFMrkArOor4fSrxsvWx8n5/fv5+fn3+/iC8fsLzPIAUscEALMDAL8QPtAsetUFWsUHue1r7/vc6evOzMfFx8n5/fvy+fj89vb/9/e+9/o44/oNi9kBD54CFKQJg9Qu4vu09vr/+ff89fTIz8rFx8n5/fvy+fj59vb49vf/+fbh+vtk6vw1rN03suFn6vnl/f3/+fn49vj18/TIz8rFx8n5/fvy+fj59vb39vf39/f//P3w+fme6/ak8Prv+fj//f369/r39vj18/TIz8rFx8ngBwAA4AMAAMADAADAAwAAwAMAAMABAACAAQAAgAEAAAAAAAAAAAAAgAEAAMADAADgBwAA+B8AAPw/AAD+fwAA',
      'options': [
        {
          'name': 'enabled',
          'type': 'enabler',
          'default': False,
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
