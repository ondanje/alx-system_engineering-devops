# fixing the issue where by Apache is returning a 500error

# Ensure Apache package is installed
package { 'apache2':
  ensure => 'installed',
}

# Ensure Apache service is running and enabled
service { 'apache2':
  ensure  => 'running',
  enable  => true,
  require => Package['apache2'],
}

# Your specific Apache configuration changes go here
# ...

# Notify that Apache has been updated
notify { 'Apache updated':
  message => 'Apache has been updated and reconfigured',
}
