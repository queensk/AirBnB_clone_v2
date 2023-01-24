#!/usr/bin/env bash
# script that sets up your web servers for the deployment of web_static

sudo apt-get update -y
sudo apt-get upgrade -y
sudo apt-get install nginx
if [ ! -d "/data/web_static/releases/test" ] || [ ! -d "/data/web_static/shared" ]; then
    sudo mkdir -p /data/web_static/releases/test /data/web_static/shared
fi
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data/
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
sudo service nginx reload
