# A Puppet manifest that kills a process named killmenow

exec {'terminate_killmenow':
command => '/usr/bin/pkill -f killmenow'
}
