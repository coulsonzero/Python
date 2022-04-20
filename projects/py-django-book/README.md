# BookSystem

python3 + Django + mysql

## 快速开始

```shell
cd py-django-book

# 安装Django
pip install Django


# 创建数据库
$ mysql -u root -p
mysql> create database book;
# python manage.py makemigrations 
python manage.py migrate  


# 创建超级管理员账户
python manage.py createsuperuser 
# 运行Django项目
python manage.py runserver  
```


## 扩展库
```shell
pip install pymysql  
python -m pip install Pillow  
pip install cryptography  
# pip install --upgrade pip  
```

error

缺少安装包
```shell
# ModuleNotFoundError: No module named 'py-django-book'
# 需修改项目下的目录名，与项目名保持一致

# ModuleNotFoundError: No module named 'pymysql'
$ pip install pymysql

# ERRORS:book.author.header: (fields.E210) Cannot use ImageField because Pillow is not installed.HINT: Get Pillow at https://pypi.org/project/Pillow/ or run command "python -m pip install Pillow".
$ python -m pip install Pillow

# WARNING: You are using pip version 21.1.2; however, version 22.0.4 is available. You should consider upgrading via the '/Users/coulsonzero/Downloads/Python/venv/bin/python -m pip install --upgrade pip' command.
$ pip install --upgrade pip 

# RuntimeError: 'cryptography' package is required for sha256_password or caching_sha2_password auth methods
$ pip install cryptography
```

缺少数据库
```shell
# django.db.utils.ProgrammingError: (1146, "Table 'book.auth_user' doesn't exist")
$ mysql -u root -p  
mysql> create database book;
```

导入数据库中，并创建超级管理员账户
```shell
# django.db.utils.OperationalError: (1045, "Access denied for user 'root'@'localhost' (using password: YES)")
$ python manage.py migrate   
$ python manage.py createsuperuser
$ python manage.py runserver 
```

