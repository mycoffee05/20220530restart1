# # 定义：能装东西的东西
# # 在python中用[]来表示一个列表，列表元素用,隔开
# a = ['张三丰','zhangwuji',[1,2,3,4,True, ]]
# # # 特性：
# # # 1.索引和切片
# # print(a[0])
# # print(a[1:3])
# # lst = ['jinmaoshiwang','','1,2,3,4True']
# # # 列表的增删改查
# append（） 追加
lst = ['赵敏', '张绍刚', '赵本山', '张无忌', '武则天', '嬴政', '马超']
# lst.append('张绍刚')
# lst.append('赵本山')
# lst.append('张无忌')
# # insert() 插入
# lst.insert(0,'赵敏')
# print(lst)
# # extend() 合并连个列表
# lst.extend(['武则天','嬴政','马超'])
# print(lst)
# # 删除
# ret = lst.pop(3) #给出被删除的索引，返回被删除的元素
# print(ret)
# lst.remove('马超') #删除某个元素
# print(lst)
# #修改
# lst[4] = '恺' #直接用索引进行修改
# print(lst)
# #查询
# print(lst[3])
# #for item in lst:
# for i in range(len(lst)): #len(lst)列表的长度 ->可以直接拿到列表索引的for循环中
#     item = lst[i] #item依然是列表中的每一项
#     if item.startswith('张'):
#         # 张换王
#         new_name = '王'+item[1:]
#         # print(new_name)
#         # 把新名字放回列表
#         lst[i] = new_name
# print(lst)
# 列表的其他操作
# # 排序
# lst = [1,2,3,'马菊花台','武大郎0']
# print(lst)
# lst = [222,666,78,88,3,675,77,88243,8,]
# lst.sort()   #升序排序
# lst.sort(reverse=True)  #反转，降序
# print(lst)
#列表的嵌套
# lst = ['aa','fff',[111,222,333,['1','aaa','2','23'],44,55],'555','hhhh']
# lst[2][3][1] = lst[2][3][1].upper()
# print(lst[2][3][1])
# print(lst)
# 列表的循环删除（*）
temp = [] #创建临时列表存放要删除的内容
for item in lst: #循环列表中的元素
# for i in range(len(lst)): #len(lst)列表的长度 ->可以直接拿到列表索引的for循环中，循环列表中的索引
    if item.startswith('张'):
        temp.append(item) #把要删除的额内容放入临时列表
        print(temp)
for item in temp:
    lst.remove(item) #去源列表中进行删除操作
print(lst)
# 安全稳妥的循环删除方式：
# 将要删除的内容保存在一个新列表李，循环新列表，删除老列表内容。