ln -sf /root/aleph-github-app/setup/nginx/default.conf /etc/nginx/sites-enabled
nginx -t
systemctl reload nginx