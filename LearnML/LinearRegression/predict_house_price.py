#!/usr/bin/python
# coding:utf8

import matplotlib.pyplot as plt
import pandas as pd
from sklearn import datasets, linear_model

def get_data(file_name):
    # 将CSV数据读入Pandas数据帧中
    data = pd.read_csv(file_name)
    X_parameter = []
    Y_parameter = []
    #  把Pandas数据帧转化为X_parameter和Y_parameter 并返回她们
    for single_square_feet, single_price_value in zip(data['square_feet'],data['price']):
        X_parameter.append([float(single_square_feet)])
        Y_parameter.append([float(single_price_value)])

    print X_parameter
    print Y_parameter
    return X_parameter,Y_parameter



# Function for Fitting our data to Linear model
# 把X_parameter和Y_parameter拟合为线性回归模型
def linear_model_main(X_parameters, Y_parameters, predict_value):

    # 创建一个线性模型 用我们的X_parameters和Y_patameter训练它
    regr = linear_model.LinearRegression()
    regr.fit(X_parameters, Y_parameters)
    predict_outcome = regr.predict(predict_value)
    # 创建一个名称为predicitions的字典
    predictions = {}
    predictions['intercept'] = regr.intercept_
    predictions['coefficient'] = regr.coef_
    predictions['predicted_value'] = predict_outcome # 预测值
    return predictions


#所以我们在这里调用一下我们的函数 要预测的平方英尺值为700
X,Y = get_data('house.csv')
predictvalue = 700
result = linear_model_main(X,Y,predictvalue)
print "Intercept value ", result['intercept']
print "coefficient ", result['coefficient']
print "Predicted value:", result['predicted_value']


#Function to show the results of linear fit model 画图表示
def show_linear_line(X_parameters, Y_parameters):

    regr = linear_model.LinearRegression()
    regr.fit(X_parameters, Y_parameters)
    plt.scatter(X_parameters, Y_parameters, color='blue')
    plt.plot(X_parameters, regr.predict(X_parameters), color='red',linewidth=4)
    plt.xticks(())
    plt.yticks(())
    plt.show()


show_linear_line(X,Y)

