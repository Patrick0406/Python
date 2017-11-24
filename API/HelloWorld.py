# !/usr/bin/python
# coding:utf-8
#引入文字识别OCR SDK
from aip import AipOcr
import json


#定义常量
APP_ID = '15850686158'
API_KEY = '7209bfd2e0914fb5a3a6c7ca6573365a'
SECRET_KEY = '73d19039db7d46f18235475060f9d4ad'

#初始化AipOcr对象
aipOcr = AipOcr(APP_ID,API_KEY,SECRET_KEY)

#读取图片
def get_file_content(filePath):
    with open('C:\Users\I332487\Desktop\Photo.jpg', 'rb') as fp:
        return fp.read()

#定义参数变量
options = {
    'detect_direction':'true',
    'language_type':'ENG',

}
#调用通用文字识别接口
result = aipOcr.basicGeneral(get_file_content('C:\Users\I332487\Desktop\Photo.jpg'),options)


#将返回的json格式化输出
json_list = json.dumps(result, indent=1)
print "result =", json_list


