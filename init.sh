mkdir web
cd web
git clone https://github.com/kyuiva/9.git .
sudo ln -s /home/box/web/etc/hginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restrart
sudo ln -s /home/box/web/etc/hello.py /etc/gunicorn.d/hello.py