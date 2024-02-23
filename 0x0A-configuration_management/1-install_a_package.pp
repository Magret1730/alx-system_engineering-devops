# Using Puppet to install flask from pip3.

#  exec { 'install_flask' :
#  command     => '/usr/bin/pip3 install Flask==2.1.0',
#  path        => '/usr/bin',
#   refreshonly => true,
#   creates     => '/usr/local/lib/python3.8/dist-packages/Flask',
#  }

# Add the directory to the PATH
#  file_line { 'add_flask_to_path':
#  path  => '/etc/environment',
#  line  => 'PATH=$PATH:/home/root/.local/bin',
#  match => '^PATH=.*$',
#  }

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

package { 'werkzeug':
  ensure   => '2.1.1',  # Specify a version compatible with Flask 2.1.0
  provider => 'pip3',
}
