python笔记，搭建web环境、数据库、发邮件等

## WEB部分
### 使用flask
pip install flask
编写server.py ww.py(注意文件名不能写成flask.py,否则无法导入包)
这里的pip是自带的命令，我这里已将：D:\Python\Python36\Scripts添加到环境变量PATH，所以可以直接使用~

### 使用模板
pip install jinja2(我这里不需要安装，自带的有)
目录结构:
web
|-templates
|   |-home.html
|   |-sign_form.html
|   |-sign_ok.html
|-server.py
|-ww.py

## 数据库部分
### 安装驱动
pip install mysql-connector-python --allow-external mysql-connector-python

//===========安装执行过程如下==================================

```bash
Microsoft Windows [版本 6.1.7601]
版权所有 (c) 2009 Microsoft Corporation。保留所有权利。
C:\Users\Administrator>e:
E:\>cd www\test\python\
E:\www\test\python>pip install mysql-connector-python --allow-external mysql-con
nector-python
DEPRECATION: --allow-external has been deprecated and will be removed in the fut
ure. Due to changes in the repository protocol, it no longer has any effect.
Collecting mysql-connector-python
  Downloading mysql_connector_python-8.0.5-py2.py3-none-any.whl (249kB)
    41% |█████████████▏                  | 102kB 193kB/s eta 0:00:
    45% |██████████████▌                 | 112kB 233kB/s eta 0:00
    49% |███████████████▊                | 122kB 255kB/s eta 0:0
    53% |█████████████████               | 133kB 281kB/s eta 0:
    57% |██████████████████▍             | 143kB 371kB/s eta
    61% |███████████████████▊            | 153kB 376kB/s eta
    65% |█████████████████████           | 163kB 367kB/s et
    69% |██████████████████████▍         | 174kB 435kB/s
    73% |███████████████████████▋        | 184kB 492kB/s
    78% |█████████████████████████       | 194kB 494kB/
    82% |██████████████████████████▎     | 204kB 572k
    86% |███████████████████████████▋    | 215kB 547
    90% |█████████████████████████████   | 225kB 71
    94% |██████████████████████████████▎ | 235kB
    98% |███████████████████████████████▌| 245kB
    100% |████████████████████████████████| 256k
B 875kB/s
Installing collected packages: mysql-connector-python
Successfully installed mysql-connector-python-8.0.5
E:\www\test\python>
```

可以看到上面报了一个警告：
> DEPRECATION: --allow-external has been deprecated and will be removed in the future.
> Due to changes in the repository protocol, it no longer has any effect.

--allow-external已经过时了，将来会移除，因为仓库协议改变，以后不会起作用~
那么OK，安装可以不用加这个参数了，以后直接`pip install mysql-connector-python`好了~
我的版本是Python3.6.3

### 测试一下链接
```bash
import mysql.connector
conn = mysql.connector.connect(user='root',password='root',database='finmall')
cursor = conn.cursor()
cursor.execute('select * from test where id between %s and %s', ('357','359'))
values = cursor.fetchall()
print(values)
```

## 邮件发送

### 安装库

