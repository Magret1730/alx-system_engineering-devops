# Puppet to automate the task of creating a custom HTTP header response

# Install Nginx
class { 'nginx':
  ensure => 'installed',
}

# Define the path to the Nginx configuration file
$nginx_conf = '/etc/nginx/sites-available/default'

# Define the path to the custom 404 page
$custom_404_path = '/usr/share/nginx/html/404.html'

# Create a default HTML page with the required content
file { '/var/www/html/index.html':
  ensure  => present,
  content => 'Hello World!',
}

# Create the custom 404 page with the required string
file { $custom_404_path:
  ensure  => present,
  content => 'Ceci n\'est pas une page',
}

# Configure nginx to listen on port 80
nginx::resource::vhost { 'default':
  listen_port    => '80',
  server_name    => '_',
  www_root       => '/var/www/html',
  ensure         => present,
}

# Configure redirection block
nginx::resource::location { '/redirect_me':
  vhost          => 'default',
  ensure         => present,
  location       => {
    add_header   => 'X-Served-By $hostname',
    return       => '301 https://www.youtube.com/watch?v=QH2-TGUlwu4',
  },
}

# Configure custom 404 page
nginx::resource::location { '/404.html':
  vhost          => 'default',
  ensure         => present,
  location       => {
    alias        => $custom_404_path,
    internal     => true,
  },
}

# Restart Nginx service
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => [
    Nginx::Resource::Vhost['default'],
    Nginx::Resource::Location['/redirect_me'],
    Nginx::Resource::Location['/404.html'],
  ],
}

