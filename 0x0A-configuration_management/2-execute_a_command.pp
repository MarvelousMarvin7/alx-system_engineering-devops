# kill a proccess killmenow'

exec {'pkill':
command  => 'pkill killmenow',
provider => 'shell',
}
