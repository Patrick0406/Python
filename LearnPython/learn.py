#!/usr/bin/python
# -*- coding: UTF-8 -*-

myvar = 3
myvar += 2
print myvar

myvar -= 1
print myvar

myString = "Hello"
myString += " world"
print myString


file = open('/Users/liuchang/Desktop/input.txt','w')
file.write('hello world')


num = 1
string = '1'
num2 = int(string)
print num + num2

words = 'words ' * 3
print words

name = "My name is Mike"
print name[0]
print name[-4]
print name[11:14]
print name[11:15]
print name[5:]
print name[:5]

word = 'friends'
find_the_evil_in_your_friends = \
    word[0]+word[2:4]+word[-3:-1]
print find_the_evil_in_your_friends


url = 'http://ww1.site.cn/14d2e8ejw1exjogbxdxhj20ci0kuwex.jpg'
file_name = url[-10:]
print file_name

phone_number = '1386-666-0006'
hidding_number = phone_number.replace(phone_number[:9], '*' * 9)
print hidding_number



