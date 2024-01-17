 fixing the extension 'phpp' to 'php'

exec{'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/user/local/bin/:/bin/'
}
