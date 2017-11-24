# !/usr/bin/python
# coding:utf-8
# 行驶证识别
from aip import AipOcr
import json


#定义常量
APP_ID = '15850686158'
API_KEY = '7209bfd2e0914fb5a3a6c7ca6573365a'
SECRET_KEY = '73d19039db7d46f18235475060f9d4ad'

#初始化AipOcr对象(AipOcr类提供给开发这一系列的图像识别方法)
aipOcr = AipOcr(APP_ID,API_KEY,SECRET_KEY)

#读取图片 使用with...as...能确保文件一定被关闭  read() 方法用于从文件读取指定的字节数，如果未给定或为负则读取所有
def get_file_content(filePath):
    with open('C:\Users\I332487\Desktop\VehicleLicense13.png', 'rb') as fp:
        return fp.read()

    # 定义参数变量
options = {
        'detect_direction': 'true',
        'accuracy': 'normal',
}


#调用驾驶证识别 API
result = aipOcr.vehicleLicense(get_file_content('C:\Users\I332487\Desktop\VehicleLicense13.png'),options)

#dict 字典类型
print result


#将返回dict字典类型的json格式化输出
jsondata= json.dumps( result, ensure_ascii = False, indent = 4 ).encode('utf-8')
print jsondata

#提取有用信息
str = result['words_result']
for key in str.keys():
   print key,':', str[key]['words']
