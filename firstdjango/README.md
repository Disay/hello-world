apt-get install libmysqld-dev
pip3 install mysqlclient 
 apt-get install mysql-server-5.7  mysql-client-5.7 libmysqlclient-dev 
mysql 默认密码：cat /etc/mysql/debian.cnf
grant all privileges on *.* to "root"@"*" identified by '123456';
flush privileges;

python3 manage.py createsuperuser 
root root

error :
```
Incorrect string value: '\\xE5\\xB0\\x8F\\xE6\\x98\\x8E' for column 'name' at row 1
->>
dberr:
https://blog.csdn.net/qq503690160/article/details/90052257
查看表状态
show create table Student\G
表字符集和字段字符集都要修改
alter table person default character set utf8;
alter table person change name name varchar(255) character set utf8;

```

