#!/usr/bin/python
# coding:utf8

import csv
import sys
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import datasets, linear_model

# 我们需要把数据拟合为两个不同的线性回归模型——先是闪电侠，然后是绿箭侠。
# 接着我们需要预测两个电视节目下一集的观众数量。 然后我们可以比较结果，推测哪个节目会有更多观众。

#function to get data
# 写一个函数，把我们的数据集作为输入，返回flash_x_parameter、flash_y_parameter、arrow_x_parameter、arrow_y_parameter values。
def get_data(file_name):
    data = pd.read_csv(file_name)
    flash_x_parameter = []
    flash_y_parameter = []
    arrow_x_parameter = []
    arrow_y_parameter = []
    for x1,y1,x2,y2 in zip(data['flash_episode_number'],data['flash_us_viewer'],data['arrow_episode_number'],data['arrow_us_viewer']):
        flash_x_parameter.append([float(x1)])
        flash_y_parameter.append([float(y1)])
        arrow_x_parameter.append([float(x2)])
        arrow_y_parameter.append([float(y2)])
        print flash_y_parameter,flash_y_parameter,arrow_x_parameter,arrow_y_parameter
        return flash_x_parameter,flash_y_parameter,arrow_x_parameter,arrow_y_parameter


# function to know which Tv show will have more viewers
# 现在我们有了我们的参数，来写一个函数，用上面这些参数作为输入，给出一个输出，预测哪个节目会有更多观众。
def more_viewers(x1,y1,x2,y2):
    regr1 = linear_model.LinearRegression()
    regr1.fit(x1, y1)
    predicted_value1 = regr1.predict(9)
    print predicted_value1
    regr2 = linear_model.LinearRegression()
    regr2.fit(x2, y2)
    predicted_value2 = regr2.predict(9)
    print predicted_value2

    if predicted_value1 > predicted_value2:
        print "The Flash Tv Show will have more viewers for next week"
    else:
        print "Arrow Tv Show will have more viewers for next week"

x1, y1, x2, y2 = get_data('FilmAudience.csv')
print x1,y1,x2,y2
more_viewers(x1,y1,x2,y2)


