# Set up web server
exec {'update packages':
    command => 'sudo apt -y update',
    path => '/bin/bash',
}

exec {'installing Nginx':
    command => 'sudo apt -y install nginx',
    path => '/bin/bash',
}

exec {'set Nginx like web server':
    command => "sudo ufw allow 'Nginx HTTP'",
    path => '/bin/bash',
}

file { '/data/web_static/releases/test':
    ensure => 'directory',
    owner  => 'ubuntu',
    group  => 'ubuntu',
    mode   => '0777',
}

file { '/data/web_static/shared':
    ensure => 'directory',
    owner  => 'ubuntu',
    group  => 'ubuntu',
    mode   => '0777',
}

file { '/data/web_static/releases/test/index.html':
    ensure => 'present',
    owner  => 'ubuntu',
    group  => 'ubuntu',
    mode   => '0777',
    content => '<h1>Html Testing Server</h1>'
}

exec {'create a symbolic link':
    command => 'sudo ln -sf /data/web_static/releases/test/ /data/web_static/current',
    path => '/bin/bash',
}

exec {'change own and group':
    command => 'sudo chown -R ubuntu:ubuntu /data/',
    path => '/bin/bash',
}


exec {'create new location':
    command => 'sudo sed -i "/^\tlocation \/ {$/ i\\\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}" /etc/nginx/sites-available/default',
    path => '/bin/bash',
}

exec {'restart Nginx':
    command => 'sudo service nginx restart',
    path => '/bin/bash',
}
