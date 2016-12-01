server {
    listen 100;
    server_name 127.0.0.1;

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/vagrant/Final/app.sock;

    }
 
}


