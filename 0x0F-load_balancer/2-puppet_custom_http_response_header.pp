# automate the task of creating a custom HTTP header response, but with Puppet.
exec { 'http header':
     command => 'sudo apt-get -y update;
     sudo sed -i '/server_name _/a add_header X-Served-By $HOSTNAME;' /etc/nginx/sites-available/default
     sudo service nginx restart',
     provider => shell,
}
