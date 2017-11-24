# !/usr/bin/python
# coding:utf-8
import urllib2

tuple = ('a','b','c')
list = ['a','b','c']
dict = {'a':1, 'b': 'true', 'c':"name"}

list.append('d')
print list[0]


list.insert(2,'e')
print list

print list.count('a')


#哈希数组
dict_arr = {'a':100, 'b':'boy', 'c':['o','p','q']}
dict_arr['d'] = 'dog'

#输出所有的key
print  dict_arr.keys()

#输出所有的value
print dict_arr.values()

print dict_arr['a']
print dict_arr['c']

#遍历数组
print '*****************遍历数组********************'
for k in dict_arr:
    v = dict_arr.get(k)
    print v

