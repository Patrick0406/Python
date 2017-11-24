# !/usr/bin/python
# coding:utf-8
# 表格识别结果获取
from aip import AipOcr
import json


# 定义常量
APP_ID = '15850686158'
API_KEY = '7209bfd2e0914fb5a3a6c7ca6573365a'
SECRET_KEY = '73d19039db7d46f18235475060f9d4ad'

# 初始化AipOcr对象(AipOcr类提供给开发这一系列的图像识别方法)
aipOcr = AipOcr(APP_ID, API_KEY, SECRET_KEY)


# 读取图片 使用with...as...能确保文件一定被关闭  read() 方法用于从文件读取指定的字节数，如果未给定或为负则读取所有
def get_file_content(filePath):
    with open('C:\Users\I332487\Desktop\Table16.jpg', 'rb') as fp:
        return fp.read()

# 调用表格识别结果获取 接口
result = aipOcr.getTableRecognitionResult('10072484_16195', {
        'result_type': 'excel',
})
jsondata= json.dumps( result, ensure_ascii = False, indent = 4).encode('utf-8')
print jsondata


