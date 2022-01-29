# Set up web server


exec {'update packages':
    command => 'apt-get -y update',
    path    => '/usr/local/bin/:/bin/',
}

exec {'installing Nginx':
    command => 'apt-get -y install nginx',
    path    => '/usr/local/bin/:/bin/',
}

exec {'set Nginx like web server':
    command => "ufw allow 'Nginx HTTP'",
    path    => '/usr/local/bin/:/bin/',
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
    command => 'ln -sf /data/web_static/releases/test/ /data/web_static/current',
    path    => '/usr/local/bin/:/bin/',
}

exec {'change own and group':
    command => 'chown -R ubuntu:ubuntu /data/',
    path    => '/usr/local/bin/:/bin/',
}


exec {'create new location':
    command => 'sed -i "/^\tlocation \/ {$/ i\\\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}" /etc/nginx/sites-available/default',
    path    => '/usr/local/bin/:/bin/',
}

exec {'restart Nginx':
    command => 'service nginx restart',
    path    => '/usr/local/bin/:/bin/',
}
