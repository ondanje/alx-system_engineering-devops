# Making changes in ssh_config file using puppet

file_line { 'Diasble passwd auth':
  path  => '/etc/ssh/ssh_config',
  line  => 'PasswordAuthentication no',
  match => '^#PasswordAuthentication',
}

file_line { 'Identity file':
  path  => '/etc/ssh/ssh_config',
  line  => 'IdentityFile ~/.ssh/school',
  match => '^#IdentityFile',
}
