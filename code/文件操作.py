'''
1.文件操作 找到个文件 双击打开

open(文件路径，mode='',encoding='')
    1.绝对路径
        d:/test/xxx.txt
    2.相对路径
        相对于当前程序所在的文件夹]
        ../上一层文件夹
    mode:
        r: read  读取
        w: write 写入
        a: append 追加写入
        b: 读写的是非文本文件
    encoding：
        utf-8
    with:
'''
# f = open('../葫芦娃.txt',mode = 'r',encoding='utf-8')
# # content = f.read() #全部读取
# # print(content)
# line = f.readlines()
# print(line)
# # line = f.readline()
# # print(line)
# # line = f.readline()
# print(line)

# 写入文件
# w模式如果文件不存在，自动创建一个，如果文件存在，每次open都会清空文件
# f = open('嫩模.txt',mode = 'w',encoding= 'utf-8' )
# f.write('胡辣汤')
# f.close() #每次操作后要关闭文件

# 将列表中的每项文件写入文件
# lst = ['zhang','wang','li','zhao']
# f = open('fight.txt',mode='w',encoding='utf-8')
# for item in lst:
#     f.write(item)
#     f.write('\n')
# f.close()

# with
# with open('fight.txt',mode='r',encoding='utf-8') as f: # f = open()
#     for line in f:
#         print(line.strip())

#读取图片
# # 在读取非文本文件时候要加b
# with open('杨开慧.jpg',mode='rb',) as f:
#     for line in f :
#         print(line)
#文件修改 把文件中的周->张
import os  
import time

with open('人名单.txt',mode='r',encoding='utf-8') as f1, \
     open('人名单_副本.txt',mode = 'w',encoding= 'utf-8') as f2:
    for line in f1:
        line = line.strip() # 去掉换行
        if line.startswith('周'):
            line = line.replace('周','张') #修改

        f2.write(line)
        f2.write('\n')
# time.sleep(3)
os.remove('人名单.txt') #删除源文件
# time.sleep(3)
os.rename('人名单_副本.txt','人名单.txt') #重命名

