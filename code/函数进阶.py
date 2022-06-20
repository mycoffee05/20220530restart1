'''
递归 函数自己调用自己
递归如果没有任何东西拦截的话，他默认是个死循环
python默认有递归深度限制，默认最大是1000
变量的作用域
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
