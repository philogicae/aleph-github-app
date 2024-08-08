```bash
apt install nginx -y

rm /etc/nginx/conf.d/default.conf
rm /etc/nginx/sites-available/*
rm /etc/nginx/sites-enabled/*

nano /etc/nginx/nginx.conf
To comment:
sendfile
ssl_protocols
ssl_prefer_server_ciphers

ln -sf /root/aleph-github-app/setup/nginx/default.conf /etc/nginx/sites-enabled

nginx -t
systemctl daemon-reload
systemctl enable nginx
systemctl start nginx

chmod +x /root/aleph-github-app/setup/nginx/update.sh
```
