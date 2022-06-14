# 字典是键值对形式存储数据的
# 字典的表示方式： {key:value,key2:value,key3:value}
# dic = {'jay':'周杰伦','金毛狮王':'谢逊'}
# val = dic['jay']
# print(val)
# 字典的key必须是可哈希的数据类型
# dic = {[]:123}
# print(dic) TypeError: unhashable type: 'list'
# dic = dict()
# dic['jay'] = '周杰伦'
# dic[1] = 123
# dic['jay'] = '昆凌' #此时，字典中已有key jay，执行的是修改操作
# # print(dic)
# dic.setdefault('tom','胡辣汤')
# dic.setdefault('tom','hhh') #设置默认值，如已有，不更改
# print(dic)
# dic.pop('jay') #通过key删除
# print(dic)
# #查询
# print(dic['tom']) #如果key不存在，程序报错，当你确定key没有问题，可以用
# print(dic.get('jayff11')) #如果key不存在，程序返回none，当不确定key，可用。
dic = {
    '11':'aa',
    '22':'bb',
    '33':'cc',
    '44':'dd'
 }
# name = input('tap ur num:')
# val = dic.get(name)
# if val is None:
#     print('not define')
# else:
#     print(val)
# for key in dic:
#     print(key,dic[key]) #拿出dict里所有键值对
# # 把所有key都保存在一个列表里
# print(list(dic.keys())) #所有key在列表中
# # 把所有value保存在一个列表
# print(list(dic.values()))
# 直接拿字典中的key和value
# print(dic.items())
# for item in dic.items():
#     # key = item(0)
#     # value = item(1)
#     print(item)
# for k,v in dic.items(): # a,b = (1,2) 元组解包过程，将dic.items直接赋值给k,v，直接拿到字典里的所有k和v
#     print(k,v)
# 嵌套
# shangyue = {
#     'name':'shang',
#     'age':22,
#     'wife':{
#         'name':'zhang',
#         'age': 22,
#         'assistant':{
#             'name':'jiu',
#             'age':22
#         }
#     }
# }
# name = shangyue['wife']['assistant']['name'] #一层一层的找，一层一层的算
# print(name)

# 循环删除
temp = [] #存放即将要删除的key
# for key in dic:
#     if key.startswith('1'):
#         temp.append(key)
# for t in temp:
#     dic.pop(t)
# print(dic)
for key in list(dic.keys()):
    if dic.keys()