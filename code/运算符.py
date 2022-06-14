'''
1.算数运算 + — * / %
2.比较运算 > < >= <= == !=
3.赋值运算 = +=
4.逻辑运算
    1. and 并且，左右两端同时成立，结果才能成立
    2. or  或者,左右两端有一个成立，结果就能成立
    3. not 非，非真既假，非假既真

    当 and 和 or 以及not同时用，加（）
    如果没有括号 先算括号->算not->算and->算or
5.成员运算
    in
    not in
'''
# a = 10
# b = 3
# c = a%b
# print(c)

# 让用户输入一个数字，判断是否是35的倍数
# n = int(input('num:'))
# if n % 35 == 0 :
#     print('yes')
# else:
#     print('no')
# a = 20
# b = 20
# print(a == b)
# a = 20
# b = 30
# temp = a #需要个中间量 或者 a,b = b,a
# a = b
# b = temp
# a,b = b,a
# print(a)
# print(b)
# n = 1
# sum = 0
# while n <= 100:
#     sum = sum + n  # sum += n
#     n = n + 1      # n += 1
# print(sum)
# 逻辑运算
# print(True and True and False)
# print(False or True)
# print(not false)
# usrname = input('用户名：')
# pswd = input('密码')
# if usrname == 'admin' and pswd == '1234':
#     print('suc')
# else:
#     print('failed')
#
# print(True and False or True)
lst = [1,23,54,56]
print(3 in lst)
print(3 not in lst)