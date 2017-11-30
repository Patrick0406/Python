#!/usr/bin/env python
#encoding: utf-8

from numpy import *
import operator
from os import listdir
from collections import Counter

def createDataSet():
    """
    创建数据集和标签

    调用方式
    import KNN
    group, labels = kNN.createDataSet()
    :return:
    """
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group, labels

def classify0(inX, dataSet, labels, k):
    """
    int[1,2,3]
    DS=[[1,2,3],[1,2,0]]
    :param inX: 用于分类的输入向量
    :param dataSet: 输出的训练样本集
    :param labels: 标签向量
    :param k: 选择最近邻居的数目
    :return:

    预测数据所在分类可在输入下列命令
    kNN.classify0([0,0], group, labels, 3)
    """

    #1.计算距离
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet
    #取平方
    sqDiffMat = diffMat ** 2
    #将矩阵的每一行相加
    sqDistances = sqDiffMat.sum(axis=1)
    #开方
    distances = sqDistances ** 0.5

    sortedDistIndicies = distances.argsort()

    #2.选择距离最小的k个点
    classCount = {}
    for i in range(k):
        #找到该样本的类型
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1

    #3. 排序并返回出现最多的那个类型
        sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
        return sortedClassCount[0][0]


def test1():
    group, labels = createDataSet()
    print str(group)
    print str(labels)
    print classify0([0.1, 0.1], group, labels, 3)



def file2matrix(filename):
    """
    导入训练数据
    :param filename: 数据文件路径
    :return: 数据矩阵returnMat和对应的类别classLabelVector
    """
    fr = open(filename)
    # 获得文件中的数据行的行数
    numberOfLines = len(fr.readlines())
    # 生成对应的空矩阵
    # 例如：zeros(2，3)就是生成一个 2*3的矩阵，各个位置上全是 0
    returnMat = zeros((numberOfLines, 3))  # prepare matrix to return
    classLabelVector = []  # prepare labels return
    fr = open(filename)
    index = 0
    for line in fr.readlines():
        # str.strip([chars]) --返回移除字符串头尾指定的字符生成的新字符串
        line = line.strip()
        # 以 '\t' 切割字符串
        listFromLine = line.split('\t')
        # 每列的属性数据
        returnMat[index, :] = listFromLine[0:3]
        # 每列的类别数据，就是 label 标签数据
        classLabelVector.append(int(listFromLine[-1]))
        index += 1
    # 返回数据矩阵returnMat和对应的类别classLabelVector
    return returnMat, classLabelVector


def autoNorm(dataSet):
    """
    归一化特征值，消除属性之间量级不同导致的影响
    :param dataSet: 数据集
    :return: 归一化后的数据集normDataSet, ranges和minVals即最小值与范围
    """
    #计算每种属性的最大值、最小值、范围
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)

    #极差
    ranges = maxVals - minVals
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    #生成与最小值之差组成的矩阵
    normDataSet = dataSet - tile(minVals, (m,1))
    #将最小值之差除以范围组成矩阵
    normDataSet = normDataSet / tile(ranges, (m,1)) #element wise divide
    return normDataSet, ranges, minVals


def datingClassTest():
    """
    对约会网站的测试方法
    :return:错误数
    """
    #设置测试数据的一个比例（测试数据集比例=1-hoRatio）
    hoRatio = 0.1  #测试范围，一部分测试一部分作为样本
    #从文件中加载数据
    datingDataMat, datingLabels = file2matrix('test.txt')
    #归一化数据
    normMat, ranges, minVals = autoNorm(datingDataMat)
    #m表示数据的行数，即矩阵的第一维
    m = normMat.shape[0]
    #设置测试的样本数量  numTestVecs: m表示训练样本的数量
    numTestVecs = int(m * hoRatio)
    print 'numTestVecs = ',numTestVecs
    errorCount = 0.0
    for i in range(numTestVecs):
        #对数据测试
        classifierResult = classify0(normMat[i, :], normMat[numTestVecs:m, :], datingLabels[numTestVecs:m], 3)
        print "the classifier came back with: %d, the real answer is : %d" % (classifierResult, datingLabels[i])
        if(classifierResult != datingLabels[i]): errorCount += 1.0
    print "the total error rate is: %f" % (errorCount / float(numTestVecs))
    print errorCount


def img2vector(filename):
    """
    将图像数据转换为向量
    :param filename: 图片文件 因为我们的输入数据的图片格式是 32 * 32的
    :return: 一维矩阵
    该函数将图像转换为向量：该函数创建 1 * 1024 的NumPy数组，然后打开给定的文件，
    循环读出文件的前32行，并将每行的头32个字符值存储在NumPy数组中，最后返回数组。
    """
    returnVect = zeros((1, 1024))
    fr = open(filename)
    for i in range(32):
        lineStr = fr.readline()
        for j in range(32):
            returnVect[0, 32 * i + j] = int(lineStr[j])
    return returnVect

def handwritingClassTest():
    #1.导入数据
    hwLabels = []
    trainingFileList = listdir('C:/Users/I332487/Desktop/trainingDigits')  #load the training set
    m = len(trainingFileList)
    trainingMat = zeros((m,1024))
    #hwLabels存储0~9对应的index位置 trainingMat存放的每个位置对应的图片向量
    for i in range(m):
        fileNameStr = trainingFileList[i]
        fileStr = fileNameStr.split('.')[0] #take off .txt
        classNumStr = int(fileStr.split('_')[0])
        hwLabels.append(classNumStr)
        #将32*32的矩阵---> 1*1024的矩阵
        trainingMat[i, :] = img2vector('C:/Users/I332487/Desktop/trainingDigits/%s' % fileNameStr)

    #2. 导入测试数据
    testFileList = listdir('C:/Users/I332487/Desktop/testDigits')  #iterate through the test set
    errorCount = 0.0
    mTest = len(testFileList)
    for i in range(mTest):
        fileNameStr = testFileList[i]
        fileStr = fileNameStr.split('.')[0] #take off .txt
        classNumStr = int(fileStr.split('_')[0])
        vectorUnderTest = img2vector('C:/Users/I332487/Desktop/testDigits/%s' % fileNameStr)
        classfierResult = classify0(vectorUnderTest, trainingMat, hwLabels, 3)
        print "the classifier came back with: %d, the real answer is: %d" % (classfierResult, classNumStr)
        if(classfierResult != classNumStr): errorCount += 1.0
    print "\nthe total number of errors is: %d" % errorCount
    print "\nthe total error rate is: %f" % (errorCount / float(mTest))


if __name__ == '__main__':
    test1()
    datingClassTest()
    handwritingClassTest()







