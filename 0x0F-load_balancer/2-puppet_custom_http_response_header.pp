# Puppet script to automate the task of creating a custom HTTP header response
include stdlib

# Install Nginx
class { 'nginx':
  ensure => 'installed',
}

# Define the path to the site-specific Nginx configuration file
$nginx_conf = '/etc/nginx/sites-available/default'

# Add custom HTTP header to the site-specific Nginx configuration
file_line { 'http_header':
  path  => $nginx_conf,
  line  => "\tadd_header X-Served-By \"${hostname}\";",
}

# Restart Nginx service after updating configuration
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File_line['http_header'],
}

