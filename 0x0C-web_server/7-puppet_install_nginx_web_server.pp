# 7-puppet_install_nginx_web_server.pp

# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Ensure Nginx service is running and enabled
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}

# Configure Nginx server
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('nginx/default.erb'),
  notify  => Service['nginx'],
}

# Create custom 404 page
file { '/usr/share/nginx/html/404.html':
  ensure  => file,
  content => 'Ceci n\'est pas une page',
}

# Enable the default site
file { '/etc/nginx/sites-enabled/default':
  ensure => link,
  target => '/etc/nginx/sites-available/default',
}

# Redirect /redirect_me to the specified URL with a 301 status
nginx::resource::location { '/redirect_me':
  ensure    => present,
  location  => '/redirect_me',
  alias     => 'https://www.youtube.com/watch?v=QH2-TGUlwu4',
  status    => '301',
  server    => 'default',
  require   => File['/etc/nginx/sites-available/default'],
}

# Notify Nginx service to restart when configuration changes
Nginx::Resource::Location <| |> ~> Service['nginx']
