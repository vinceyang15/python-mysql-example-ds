# python-mysql-example-ds
This is an example to show how to start working with python and mysql.

1. Install mysql via the installer, you can download the installer [here](https://dev.mysql.com/downloads/mysql/).
2. Add following lines into your `~/.bash_profile`. If you don't have it yet, you should create one.
```bash
export PATH=/usr/local/mysql/bin:$PATH
export MYSQL_HOME=/usr/local/mysql
alias start_mysql='sudo $MYSQL_HOME/support-files/mysql.server start'
alias stop_mysql='sudo $MYSQL_HOME/support-files/mysql.server stop'
```
3. Load the `~/.bash_profile`, using `source ~/.bash_profile`
4. Now you can start your mysql database via command `start_mysql` or stop it using `stop_mysql`. You can also use `mysql -uroot -p` to access your MySQL database as well.
5. If you want to dump in a file, say the file is `~/Downloads/dbsql.sql`, the following instructions will be useful.
    1. create a database first, `create database sample-db`
    2. run command, `mysql -uroot -p sample-db < ~/Downloads/dbsql.sql`, your dump will be imported.
6. Download the [mysql_connect.py](https://github.com/vinceyang15/python-mysql-example-ds/blob/master/mysql_connect.py).
7. Run `pip install mysqlclient` in commandline.
8. Run `python mysql_connect.py`, and it will print out the first row of the users table.

## Links
[Mysql Client Document](https://mysqlclient.readthedocs.io)
