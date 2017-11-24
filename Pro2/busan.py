# !/usr/bin/python
# coding:utf-8
import jieba
import codecs
import jieba.posseg as pseg


names = {}			# 姓名字典
relationships = {}	# 关系字典
lineNames = []		# 每段内人物关系

# count names
jieba.load_userdict("C:\Users\I332487\Desktop\dict.txt")		# 加载字典
with codecs.open("C:\Users\I332487\Desktop\Busan.txt", "r", "utf-8") as f:
	for line in f.readlines():
		poss = pseg.cut(line)		# 分词并返回该词词性
		lineNames.append([])		# 为新读入的一段添加人物名称列表
		for w in poss:
			if w.flag != "nr" or len(w.word) < 2:
				continue			# 当分词长度小于2或该词词性不为nr时认为该词不为人名
			lineNames[-1].append(w.word)		# 为当前段的环境增加一个人物
			if names.get(w.word) is None:
				names[w.word] = 0
				relationships[w.word] = {}
			names[w.word] += 1					# 该人物出现次数加 1

# explore relationships
for line in lineNames:					# 对于每一段
	for name1 in line:					
		for name2 in line:				# 每段中的任意两个人
			if name1 == name2:
				continue
			if relationships[name1].get(name2) is None:		# 若两人尚未同时出现则新建项
				relationships[name1][name2]= 1
			else:
				relationships[name1][name2] = relationships[name1][name2]+ 1		# 两人共同出现次数加 1

# output
with codecs.open("C:\Users\I332487\Desktop\Busan_node.txt", "a+", "utf-8") as f:
	f.write("Id Label Weight\r\n")
	for name, times in names.items():
		f.write(name + " " + name + " " + str(times) + "\r\n")

with codecs.open("C:\Users\I332487\Desktop\Busan_edge.txt", "a+", "utf-8") as f:
	f.write("Source Target Weight\r\n")
	for name, edges in relationships.items():
		for v, w in edges.items():
			if w > 3:
				f.write(name + " " + v + " " + str(w) + "\r\n")