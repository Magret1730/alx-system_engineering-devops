# changes nginx open file limit
exec { 'Change nginx limit':
  command  => 'sudo sed -i "s/15/4096/g" /etc/default/nginx',
  provider => shell,
}

exec { 'Restart nginx':
  command  => 'sudo service nginx restart',
  provider => shell,
}
