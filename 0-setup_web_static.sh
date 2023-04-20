#!/usr/bin/env bash
# sets up my web servers for the deployment of web_static

# Install Nginx if it not already installed
sudo apt-get -y update
sudo apt-get -y install nginx

# Create the directories if they don’t already exist
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared

# Test Nginx configuration
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" >/data/web_static/releases/test/index.html

# Create symbolic link or replace if it exists
if [ -d "/data/web_static/current" ]; then
  sudo rm -rf /data/web_static/current
fi

# Create symbolic link and change ownership
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data/

# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
printf %s "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root   /var/www/html;
    index  index.html index.htm;

    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }

    location /redirect_me {
        return 301 http://youtube.com/;
    }

    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
}" >/etc/nginx/sites-available/default

# Create symbolic link
sudo ln -sf '/etc/nginx/sites-available/default' '/etc/nginx/sites-enabled/default'

# Restart Nginx
sudo service nginx restart || sudo service nginx start
