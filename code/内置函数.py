'''
内置函数 直接拿来用的func
zip


'''
# a = 18
# print(bin(a)) #2进制
# print(oct(a)) #8进制
# print(hex(a)) #16进制
#
# b = 0b10010
# print(int(b))
# print(int(0x12))
# sum min max pow
# a = 10
# b = 3
# print(pow(10,3))
# print(a ** b)
# lst = [12,456,32,18,64,57]
# print(max(lst))
# print(min(lst))
# print(sum(lst))
# s = {1,2,3,}
# lst = list('hhd') #内部一定有一个for循环
# print(lst)
# s = slice(1,4,3)

# format() ord chr
# a = 18
# print(format(a,'b')) #b,二进制 o,八进制  x,十六进制
# print(format(a,'o'))
# print(format(a,'x'))
# a = '中' # python的内存中使用的是Unicode
# print(ord(a))  # 中国的中字Unicode的码位是20013
# print(chr(20013))

# for i in range(65536):
#     print(chr(i)+' ',end='')
# enumerate \all\ any
# print(all([0,'hh','doushabao'])) # 当and来看
# print(any([0,'',' '])) # 当or来看
# lst = ['张无忌','张三丰','张翠山','张学友']
# for index,item in enumerate(lst):
#     print(index,item)
# for i in range(len(lst)):
#     print(i,lst[i])
# s = '呵呵哒'
# print(hash(s)) #一定是一个数字 ->想办法转化成内存地址，然后进行数据的存储 ->字典（集合
# print(id(s))
# print(help(str)) #按住ctrl可查命令源码
# s = '呵呵哒'
# print(dir(s))
# lst1 = ['zhang','ye','shang','yue']
# lst2 = [40,20,30,70]
# lst3 = ['a','b','c','d']
# result = []
# for i in range(len(lst1)):
#     fir = lst1[i]
#     sec = lst2[i]
#     third = lst3[i]
#     result.append((fir,sec,third))
# print(result)
# result = zip(lst1,lst2,lst3)
# # for item in result:
# #     print(item)
# lst = list(result)
# print(lst)
# a = 188
# print(locals()) #此时locals被写入全局作用域范围内，显示全局内容。
# def func():
#     a = 44
#     print(locals())
# func()
c = 12
print(globals())
