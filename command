django-admin.py startproject ask
cd ask
django-admin startapp qa
gunicorn -b 0.0.0.0:8000 --pythonpath /home/sergey/projects/web/ask/ ask.wsgi:application 

sudo /etc/init.d/mysql start
mysql -u root -p123
create database stepik;
create user 'step'@'localhost' identified by '123';
grant all privileges on stepik.* to 'step'@'localhost';

# install modul mysqldb in virtualenv
sudo apt-get build-dep python-mysqldb
pip install mysql-python

# migration models django
# manage.py - file project django 
python manage.py makemigrations
python manage.py migrate

