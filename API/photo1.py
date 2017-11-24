# !/usr/bin/python
# coding:utf-8
#通用文字识别（含位置信息版）

#引入文字识别OCR SDK
import json
from aip import AipOcr

#定义常量
APP_ID = '15850686158'
API_KEY = '7209bfd2e0914fb5a3a6c7ca6573365a'
SECRET_KEY = '73d19039db7d46f18235475060f9d4ad'

#读取图片
def get_file_content(filePath):
    with open(filePath,'rb') as fp:
        return fp.read()

#初始化ApiOcr对象
aipOcr = AipOcr(APP_ID,API_KEY,SECRET_KEY)

# 定义参数变量
options = {
  'detect_direction': 'true',
  'language_type': 'CHN_ENG',
}

#调用通用文字识别接口
result = aipOcr.general(get_file_content('C:\Users\I332487\Desktop\photo1.jpg'),options)

#将返回的json格式化输出
json_list1 = json.dumps(result, indent=1)
print json_list1


