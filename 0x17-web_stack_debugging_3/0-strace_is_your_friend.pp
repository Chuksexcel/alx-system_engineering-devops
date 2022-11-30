# GET HTTP method is requested to Apache with 500 error for the web server

exec {'replace':
  provider => shell,
  command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php'
}
