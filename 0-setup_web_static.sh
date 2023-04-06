#!/usr/bin/env bash
#script that sets up your web servers for the deployment of web_static
#create folders
#fist installation of nginx
sudo apt-get update
sudo apt-get install nginx -y

#create folders in the specified path
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

#create a dummy html file
echo "Holberton School" | sudo tee /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

#changing ownership of the folder data
sudo chown -R ubuntu:ubuntu /data/

#configuration of nginx location to hbtn static

sudo sed -i '/server_name _;/a \ \tlocation /hbnb_static {    \n\talias /data/web_static/current;\n\t}\n' /etc/nginx/sites-available/default

#restating ngix to update changes
sudo service nginx restart

