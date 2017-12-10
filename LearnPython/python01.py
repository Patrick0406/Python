#!/usr/bin/python
# -*- coding: UTF-8 -*-
#文件名：python01.py

import sys

a = b = c = 1

str = 'Hello World!'
print str
print str[0]
print str[2:5]
print str[2:]
print str * 2
print str + " TEST"

list = ['runoob', 786, 2.23, 'john', 70.2]
tinylist = [123,'john']
print list
print list[0]
print list[1:3]
print list[2:]
print list + tinylist

tuple =  ('runoob', 786, 2.23, 'john', 70.2)
tinytuple = (123, 'john')
print tuple
print tuple[0]
print tuple[1:3]
print tuple[2:]
print tinytuple * 2
print tuple + tinytuple

dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"
tinydict = {'name': 'john', 'code':6734, 'dept': 'sales'}
print dict['one']
print dict[2]
print tinydict
print tinydict.keys()
print tinydict.values()

#变量赋值
a = 1
b = 'god'

#字符串赋值
str = 'this is string 1'

#列表串赋值
tuple = ('this', 'is', 'tuple', 3)

#字典赋值
dict = {1:'this', 2:'is', 3:'dictionary', 4:4}

print a,b
print str
print tuple[0]
print dict.keys()

#python的所有类型都是类 可以通过type()来查看该变量的数据类型
n = 1
print type(n)
n = 'runoob'
print type(n)
a = 111
print isinstance(a, int)


a = 10
b = 20
list = [1,2,3,4,5]
if (a in list):
    print "1 - 变量a在给定的列表中"
else:
    print "1 - 变量a不在给定的列表中"

if(b not in list):
    print "2 - 变量b不在给定的列表list"
else:
    print "2 - 变量b在给定的列表list中"

