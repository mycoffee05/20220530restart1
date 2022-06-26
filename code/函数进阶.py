'''
递归 函数自己调用自己
递归如果没有任何东西拦截的话，他默认是个死循环
python默认有递归深度限制，默认最大是1000
变量的作用域
    变量的访问权限
函数可以作为返回值进行返回
函数可以作为参数进行传递
函数实际上就是一个变量名，都表示一个内存地址
闭包
装饰器
    def wrapper(fn):
        def inner(*args,**kwargs)
            ret = fn(*args,**kwargs)
            return ret
        return inner

    @wrapper
    def fun():
        pass

迭代器
生成器
    yield

    g =
推导式
匿名函数
python的内置函数_下 sorted,filter,map
'''
# def func():
#     print(123)

#     func()
# func()
# import sys
# print(sys.getrecursionlimit()
#sys.getrecursionlimit() 调整递归深度
# a = 10 #全局变量
# def func():
#     b = 20 #局部变量 ，局部作用域
#     return b
# b1 = func()
''' 
函数的嵌套
'''
# def func1():
#     def func2(): #局部变量，嵌套
#         pass
#     func2() #局部的额东西，一般都是在局部内访问使用的
# def fun1():
#     print(123)
#     def fun2():
#         print(456)
#         def fun3():
#             print(789)
#         print(1)
#         fun3()
#         print(2)
#     print(3)
#     fun2()
#     print(4)
# fun1()
# def fun():
#     def inner():
#         print(123)
#     print(inner)
#     return inner #返回的是一个函数，此时我们把一个函数当一个变量进行返回的
# b1 = fun() #b1是fun内部的inner
# print(b1)
# b1()
# def an():
#     print(123)
# bn = an
# an()
#代理模式
# def func(an): #此时an接收的是一个函数
#     an() #执行这个函数
# def targer():
#     print('im target')
# func(targer) #实参可以是函数
# a = 10
# def func():
#     #修改全局变量
#     global a #把外部全局变量引入局部
#     a = 20
# func()
# def func():
#     a = 10
#     def func1():
#         nonlocal a #引入外层变量a ,向外找一层，如果有就引入，没有继续向外一层，直到全局（但不包括）
#         a = 20
#     func1()
#     print(a)
# func()
'''
闭包 内层函数对外层函数的局部变量的使用，此时内层函数被称为闭包
    1.可以让变量常驻内存
    2.可以避免全局变量被修改
'''
# def func():
#     a = 10
#     def inner():
#         nonlocal a
#         a += 1
#         return a
#     return inner
# ret = func()
# # inner -> ret -> 什么时候执行
# r1 = ret()
# print(r1)
# r2 = ret()
# print(r2)
# f1 = func()
# print(f1())
# f2 = func()
# print(f2())
'''
内容回顾
    1.函数可以作为参数进行传递
    2.函数可以作为返回值进行返回
    3.函数名称可以当成变量一样进行赋值操作
装饰器：->记住结论
    本质上是一个闭包
    在不改变原目标函数源代码的前提下增加功能。
    通用装饰器写法：：
        def wrapper(fn): wrapper是装饰器，fn目标函数
            def inner(*args,**kwargs):
                #在函数前执行。。。。
                ret = fn(*args,**kwargs)
                #函数后执行啥
                :return = ret
            return inner
        @wrapper
        def target():
            pass
        target() # ->inner()
    一个函数可以被多个装饰器装饰
    @wraper1
    @wraper2
    def target():
        print('im target')
    规则和规律：wraper1 wraper2 target wraper2 wraper1
'''
# def func():
#     print('imfunc')
# def gggg(fn):
#     fn()
# gggg(func)
# def func():
#     def inner():
#         print(123)
#     return inner
# ret = func()
# ret()
# def func1():
#     print(1)
# def fun2():
#     print(2)
# func1 = fun2
# func1()
# def guanjia(game):
#     def inner():
#         print(1)
#         game()
#         print(2)
#     return inner
# @guanjia #相当于执行了 play_dnf=guanjia(play_dnf)
# def play_dnf():
#     print('hello im salia')
# @guanjia
# def play_lol():
#     print('demaxia')
#
#
# play_dnf()
# play_lol()
# def guanjia(game):
#     def inner(*args,**kwargs): #传入任意参数，元组或字典
#         print(1)
#         game(*args,**kwargs) #将元组或字典打散
#         print(2)
#     return inner
# @guanjia #相当于执行了 play_dnf=guanjia(play_dnf)
# def play_dnf(user,pswd):
#     print('hello im salia',user,pswd)
# @guanjia
# def play_lol(user,pswd,hero):
#     print('demaxia',user,pswd,hero)
#
#
# play_dnf('shang',111)
# play_lol('zhang',222,'fff')
# def guanjia(game):
#     def inner(*args,**kwargs): #传入任意参数，元组或字典
#         print(1)
#         game(*args,**kwargs) #将元组或字典打散
#         print(2)
#     return inner
# @guanjia #相当于执行了 play_dnf=guanjia(play_dnf)
# def play_dnf(user,pswd):
#     print('hello im salia',user,pswd)
# @guanjia
# def play_lol(user,pswd,hero):
#     print('demaxia',user,pswd,hero)
#
#
# play_dnf('shang',111)
# play_lol('zhang',222,'fff')
# login_flag = False
# def login_verify(fn):
#     def inner(*args,**kwargs):
#         global login_flag
#         if login_flag == False:
#             #这里完成登录校验
#             print('请登录')
#             while 1:
#                 username = input('>>>')
#                 password = input('>>>')
#                 if username == 'admin' and password == '123' :
#                     print('sucss')
#                     login_flag = True
#                     break
#                 else:
#                     print('failed,again')
#         ret = fn(*args,**kwargs)
#         return ret
#     return inner
# @login_verify
# def add():
#     print('添加员工信息')
# @login_verify
# def delete():
#     print('删除信息')
# add()
# delete()
'''
可迭代的数据类型都会提供迭代器，可以把数据类型中的所有数据逐一取出
获取迭代器的两种方案：
    1.iter() 内置函数可以直接拿到迭代器
    2.__iter__() 
从迭代器中拿数据：
    1.next（）内置函数
    2.__next__() 特殊方法
for里面一定是要拿地带器的，所以所有不可迭代的东西不能用for循环
for循环里一定有__next__出现

总结：迭代器统一了不同数据类型的遍历工作
迭代器本身也是可迭代的
    1.只能顺序向前，不能反复
    2.节省内存
    3.惰性机制
'''
# it = iter('呵呵哒')
# #it = '呵呵哒'.__iter__()
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# for循环的工作原理
# s = '我是数据'
# it = s.__iter__() #拿数据
# while 1:
#     try:
#         date = it.__next__()
#         print(date) #for循环体
#     except StopIteration:
#         break
# s = 'im salia'
# for mm in s:
#     print(mm)
'''
生成器：
    本质就是迭代器
    创建的方案
        1.生成器函数
            有一个关键字yield
            生成器函数执行的时候，并不会执行函数，
            yield:只要函数出现，他就是个生成器函数
                作用：
                    1.可以返回数据
                    2.可以分段执行函数中的内容，通过__next__()可以执行到下一个yield位置
            adv：
                节省内存
        2.生成器表达式 ->一次性的
            语法：（数据 for循环 if判读）
'''
# def func():
#     print(123456)
#     yield 999 # yield也有返回意思
#     print(244)
#     yield 666
# ret = func()
# # print(ret) #<generator object func at 0x000001E08080D9E0>
# print(ret.__next__()) #yield只有执行next才会返回数据
# print(ret.__next__())# stopiteration
# diy 1w件衣服
# def order():
#     lst = []
#     for i in range(10000):
#         lst.append(f'衣服{i}')
#     return lst
# lst = order()
# print(lst)
# def order():
#     lst = []
#     for i in range(10000):
#         lst.append(f'cloth{i}')
#         if len(lst) == 50:
#             yield lst #下一次拿数据
#             lst = []
# gen = order()
# print(gen.__next__())
# print(gen.__next__())
'''
推导式
    简化代码
    语法：
        列表推导式：[数据 for循环 if判断]
        集合推导式：{数据 for循环 if判断}
        字典推导式：{k:v for循环 if判断}
    不要什么都写推导式
    （数据 for循环 if判断） ->不是元组推导式，这叫生成器表达式
'''
# lst = [i for i in range(10)]
# print(lst)
#创建一个列表  1 3 5 7 9
# lst = [i for i in range(1,10,2)]
# lst1 = [i for i in range(10) if i % 2 == 1]
# print(lst)
# print(lst1)
#生成50衣服
# lst = [f'cloth{i}' for i in range(50)]
# print(lst)
#将如下列表中所有英文字母修改成大写
# lst1 = ['shang','yue','zhang','ye']
# lst2 = [item.upper() for item in lst1]
# print(lst2)
#4.列表修改成字典，要求索引为key，数据为value
# lst = ['shang','yue','zhang','ye']
# dic = {i:lst[i] for i in range(len(lst))}
# print(dic)
# gen = (i**2 for i in range(10))
# lst = list(gen) #list ->for -> next
# print(lst)
# for item in gen:
#     print(item)