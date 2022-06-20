'''
函数的概念
函数的参数
函数的返回值
    1.定义 函数执行之后，会给调用方一个结果，这个结果就是返回值
python的内置函数
'''
# 函数定义 对某一个特定的功能或者代码进行封装，在使用该功能的时候直接调用即可
'''
定义：
def 函数名字（）：
    被封装的功能或者代码块->函数体
    
调用：
函数的名字（）

好处：
让程序简介，代码更加合理
'''
# def buy_cai(): # 定义函数 不执行
#     print('1')
#     print('2')
#     print('3')

# buy_cai()
# print('4')
# buy_cai()
# print('5')
# buy_cai()
# print('6')

'''
1.形参，在函数定义的时候，需要准备一些变量来接收实参
    1.位置参数
    2.默认值参数 在函数声明的时候给变量一个默认值，如果实参不传递信息，此事默认值生效，否则不生效
    位置—> *args ->默认值->**kwargs
    3.动态传参
        1.*args,接受所有位置的动态传参
        2. **kwargs,接收所有关键字的动态传参
2.实参 实际调用时候传递的信息
    1.位置实参，按照位置进行传参
    2.关键字传参，按照参数的名字进行传参
    3.混合参数，位置参数放前面，关键字参数放后面
实参在执行的时候必须保证形参有数据
'''
# 1.骂谁？ 2.骂什么程度？
# def maren(ren,lv): #形参
#     print('1.瞅他',ren)
#     print('2.交涉',ren)
#     if lv > 99:
#         print('3.不要脸')
#     else:
#         print('3.okok')
#     print('4.收工')
# maren('a',111) #在调用函数时候骂谁，骂什么程度
# maren('b',9)
# maren('c',99)

# 用函数编写一个计算器，能计算加减乘除
# def Caculator(a,opt,b):
#     if opt == '+':
#         print(a+b)
#     elif opt == '-':
#         print(a-b)
#     elif opt == '*':
#         print(a*b)
#     elif opt == '/':
#         print(a/b)
#     else:
#         print('fuoff')
#
# Caculator(99,'SSF',9)
# def chi(zhu,fu,tang,tian):
#     print(zhu,fu,tang,tian)
# chi('rice','tomato','egg','ice')
# chi(zhu='corn',tang='soup',fu='potato',tian='cream')
# chi('rice',fu='tomato',tian='egg',tang='ice')
# chi('1') #必须有4个数据
# open(file='1',mode='2',encoding='3')
# def luru(name,age,gender='male'):
#     print(name,age,gender)
# luru('z',18)
# luru('g',18)
# luru('r',18)
# luru('s',18,'female')

# def chi(*food): #*表示位置参数的动态传参，*接收到的值会被同意放在一个元组里
#     print(food)
# chi('rice','tome','soup','ice')
# import xml.sax
# def chi(**food): # ** 表示接收关键字的动态传参，接收到的所有参数都会被处理成字典
#     print(food)
# chi(zhu = 'a',fu = 'b')
# def chi(a,b,*args,c='haha',**kwargs):#正确的传参顺序
#     print(a,b,args,c,kwargs)
# def func(*args,**kwargs): #没有限制的接收任何参数
# stu_lst = ['a','b','c']
# def func(*args):
#     print(args)
# func(*stu_lst) # 在实参位置，把列表打散成位置参数进行传递。
#             # **在实参位置，可以把字典自动转化成关键字参数进行传递。
'''
关于return:
    函数只要执行到了return，函数就会立即停止并返回内容，函数内的return的后续代码不会执行
    1，如果函数内没有return,从实外界收到的是none
    2.如果写了return
        1.只写了return，后面不跟数据，此时接收到的依然是none
        2.return值，此时表示函数有一个返回值，外界能够收到一个数据
        3.return值1，值2，值3.。。此时函数有多个返回值，外界收到的是元组，并且该元组内存放所有返回值。
'''
# def func(a,b):
#     return a+b
# ret = func(10,20)
# print(ret*3)
# def func():
#     print(123)
#     return
#     print(456)
# ret = func()
# print(ret)
