# set集合
# s = {1,2,3,[]}
# print(type(s))
# print(s) TypeError: unhashable type: 'list'
# 不可哈希：python中的set集合进行数据存储的时候，需要对数据进行哈希计算，根据计算出来的哈希值进行存储数据
#         可变的数据类型： lst ,dict,set
# 可哈希： 不可变的数据类型，int,str,tuple,bool.

s = set() # 创建孔集合
t = tuple()
lst = list()
s.add('111')
s.add('222')
s.add('333')
print(s)
s.pop() #集合无序，无法验证扔出去最后一个。
print(s)
s.remove('333')
print(s)
#想要修改，先删除，后新增