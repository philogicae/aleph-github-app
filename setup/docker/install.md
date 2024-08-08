```bash
update-alternatives --set iptables /usr/sbin/iptables-legacy
update-alternatives --set ip6tables /usr/sbin/ip6tables-legacy
update-alternatives --set arptables /usr/sbin/arptables-legacy
update-alternatives --set ebtables /usr/sbin/ebtables-legacy


apt install docker.io -y
usermod -aG docker $USER
mkdir -p /docker/portainer/data

curl -s https://api.github.com/repos/docker/compose/releases/latest | grep browser_download_url  | grep docker-compose-linux-x86_64 | cut -d '"' -f 4 | head -n 1 | wget -i - -O /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose

cp ~/aleph-github-app/setup/docker/portainer.service /etc/systemd/system/portainer.service
systemctl daemon-reload
systemctl enable portainer
systemctl start portainer
```