# Fix typographical error in WordPress setting file
exec { 'Fix typo in filename':
  command  => 'sudo sed -i "s/.phpp/.php/" /var/www/html/wp-settings.php',
  provider => shell,
}
