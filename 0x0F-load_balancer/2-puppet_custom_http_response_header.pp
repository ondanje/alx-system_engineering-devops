#!/usr/bin/env bash
# install and configure an Nginx server using Puppet
# instead of Bash


package { 'nginx':
  ensure => 'installed',
  name   => 'nginx',
}

# Define the nginx configuration file path
$nginx_conf = '/etc/nginx/nginx.conf'

# Add a line after the 'http {' section in nginx.conf
augeas { 'add_custom_header':
  context => "/files${nginx_conf}/",
  changes => [
    "ins http after server[last()]",
    "set http/add_header X-Served-By ${hostname}",
  ],
  onlyif  => "match http[last()]/add_header X-Served-By[. = '${hostname}'] size == 0",
  require => Package['nginx'], # Ensure that nginx is installed before modifying the configuration
}

service { 'nginx':
  ensure    => 'running',
  enable    => true,
  subscribe => Augeas['add_custom_header'], # Subscribe to the Augeas resource
}
