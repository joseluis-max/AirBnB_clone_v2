#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static.
sudo apt -y update
sudo apt -y install nginx
ufw allow 'Nginx HTTP'
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "<h1>Html Testing Server</h1>" > touch /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -Rh ubuntu /data
chgrp -Rh ubuntu /data
sed -i "/^\tlocation \/ {$/ i\\\tlocation /\hbnb_static { \n\t\talias \/data\/web_static\/current\/;\n\t\tautoindex off;\n}\n" /etc/nginx/sites-available/default
sudo service nginx restart
