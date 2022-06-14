# tuple 元组，特点：不可变的列表
# t = ('张无忌','zhao','jinmao')
# print(t)
# print(t[1:3])
# t[0] = 'qiaofu'  TypeError: 'tuple' object does not support item assignment
# 关于元组的不可变,内存地址不可变
# t = (1,2,3,['11','222',','])
# t[3].append('555')
# print(t)