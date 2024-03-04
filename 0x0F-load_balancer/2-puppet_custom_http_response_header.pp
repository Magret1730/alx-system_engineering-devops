# puppet to automate the task of creating a custom HTTP header response

# Ensure the Nginx package is present
package {'nginx':
  ensure => 'present',
}

# Execute command to install Nginx
exec {'install':
  command  => 'sudo apt-get update ; sudo apt-get -y install nginx',
  provider => shell,
}

# Add custom HTTP header to Nginx configuration
-> file_line { 'http_header':
  path  => '/etc/nginx/nginx.conf',
  match => 'http {',
  line  => "http {\n\tadd_header X-Served-By \"${hostname}\";",
}

# Restart Nginx to apply changes
exec {'restart_nginx':
  command  => 'sudo service nginx restart',
  provider => shell,
}
