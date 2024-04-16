# Change the OS configuration so that it is possible to login with the
# holberton user and open a file without any error message.
user { 'holberton':
  ensure => present,
}

file { '/etc/security/limits.conf':
  ensure => present,
  owner  => 'root',
  group  => 'root',
  mode   => '0644',
}

exec { 'Change soft limit':
  command  => 'sed -i "/^holberton\ssoft\s/s/.*/holberton\tsoft\tnofile\t10000/" /etc/security/limits.conf',
  path     => '/bin:/usr/bin',
  unless   => 'grep -E "^holberton\\ssoft\\s+nofile\\s+10000$" /etc/security/limits.conf',
  provider => shell,
}

exec { 'Change hard limit':
  command  => 'sed -i "/^holberton\shard\s/s/.*/holberton\thard\tnofile\t100000/" /etc/security/limits.conf',
  path     => '/bin:/usr/bin',
  unless   => 'grep -E "^holberton\\shard\\s+nofile\\s+100000$" /etc/security/limits.conf',
  provider => shell,
}
