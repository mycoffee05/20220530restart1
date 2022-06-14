'''
1.文件操作 找到个文件 双击打开

open(文件路径，mode='',encoding='')
    1.绝对路径
        d:/test/xxx.txt
    2.相对路径
        相对于当前程序所在的文件夹]
        ../上一层文件夹
    mode:
        r: read 读取

    encoding：
        utf-8
'''
f = open('../葫芦娃.txt',mode = 'r',encoding='utf-8')
# content = f.read() #全部读取
# print(content)
line = f.readlines()
print(line)
# line = f.readline()
# print(line)
# line = f.readline()
# print(line)