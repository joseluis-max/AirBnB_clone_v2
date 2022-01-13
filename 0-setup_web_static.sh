#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static.
sudo apt -y update
sudo apt -y install nginx
ufw allow 'Nginx HTTP'
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared
echo "<h1>Html Testing Server</h1>" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sudo sed -i "/^\tlocation \/ {$/ i\\\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}" /etc/nginx/sites-available/default
sudo service nginx restart
