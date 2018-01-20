# sudo /etc/init.d/mysql start
mysql -u root
create database stepik;
create user 'step'@'localhost' identified by '123';
grant all privileges on stepik.* to 'step'@'localhost';

