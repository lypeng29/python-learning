#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import mysql.connector

conn = mysql.connector.connect(user='root',password='root',database='finmall')
cursor = conn.cursor()

# cursor.execute('create table user(id int(11) primary key, name varchar(50))')
# cursor.execute('insert into test(text) values(%s)',['linan'])
# print(cursor.rowcount) #显示影响的记录数
# conn.commit() #如果是innodb需要提交

cursor.execute('select * from test where id between %s and %s', ('357','359'))
values = cursor.fetchall()
print(values)

cursor.close()
conn.close()
