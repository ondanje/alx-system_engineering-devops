# Enabling holberton user and open a file without any error message.

exec { 'changing hard nofile limit':
command => "sed -i '/^holberton hard/s/5/50000/' /etc/security/limits.conf",
path    => '/usr/local/bin/:/bin/'
}

exec { 'changing soft nofile limit':
command => "sed -i '/^holberton soft/s/4/50000/' /etc/security/limits.conf",
path    => '/usr/local/bin/:/bin/'
}
