# while True:
#     content = input("input ur content(q结束）:")
#     if content == "q":
#         break
#     print("发给下路:",content)
# i = 1
# %s 字符串占位
# %d 占位整数
# %f 占位小数
# f-string f'{}' 这样最好理解
# name = input("your name:")
# add = input("your address:")
# age = int(input("your age:"))
# hobby = input("your hobby:")
# s = 'My name is %s,I live in %s,I m %d years old,I like to %s' % (name,add,age,hobby)
# s1 = f'My name is {name},I live in {add},I m {age} years old,I like to {hobby}' #f-string 好用
# print(s1)

# # index
# # 按照位置提取元素
# s = '我叫周杰伦'
# # 可以采用index的方式来提取某一个字符
# print(s[3]) # 程序都是从0开始数
# # print(s[-1]) # -表示倒数
# # 切片:从一个str中提取一段内容
# s = '我叫周杰伦，你呢？你叫周润发吗？'
# print(s[3:6]) # 从索引3位置进行切片，切到6位置，不含6
# # 前闭后开 s[start:end] 从start开始，但取不到end,[start,end)
# print(s[:5])
# print(s[6:])
# # # : 如果左右空白，表示开头或结尾
# # print(s[-3:-1]) #目前只能从左往右切片
# s = '我爱你'
# # 可以给切片添加步长来控制切片的方向
# print(s[::-1]) # 第三个位置表示步长 -表示从右往左
# # s[start:end:step]从start切到end，每个step个元素取一个元素
# s = 'abcdefghijklmnopqrst'
# print(s[3:8:2])
# print(s[-1:10:-3])
# 字符串常规操作
# # 字符串的操作一般不对源字符串产生影响，会返回一个新的字符串
# s = 'python'
# s1 = s.capitalize() #首字母大写
# print(s1)
# s = 'i have a dream.'
# s1 = s.title() #单词首字母大写
# print(s1)
# s = 'I HAVE A DREAM!'
# s1 = s.lower() #所有字母小写
# print(s1)
# s = 'i have a dream!'
# s1 = s.upper() #所有字母大写
# print(s1)
# # 如何忽略大小写进行判断 => upper()
# verify_code = 'xAd1'
# user_input = input(f'plz input code({verify_code}):')
# if verify_code.upper() == user_input.upper():
#     print('pass')
# else:
#     print('incrorrect')
# 字符串的替换和切割
# # strip() 去掉字符串左右两边的空白（空格，\t \n）
# s = '   你好，    我叫    周杰伦   '
# s1 = s.strip()
# print(s1)
# 案例
# username = input('plz tap ur name:').strip()
# passwd = input('plz tap ur pswd:').strip()
# if username == 'admin':
#     if passwd == '123456':
#         print('login in successful')
#     else:
#         print('failed')
# else:
#     print('failed')

# 我 今天 很 郁 闷
# # replace(old,new) 字符串替换
# s = '你好啊，我叫赛利亚'
# s1 = s.replace('赛利亚','shang')
# print(s1)
# split(用什么切割) 字符串切割,用什么切，就会损失掉谁
# a = 'python_java_c_c#'
# a1 = a.split('_')
# print(a1)
# lst = a.split('_java_')
# print(lst)
# replace(), split(), strip()
# 查找和判断
# 查找
# s = '你好啊，我叫周杰伦'
# s1 = s.find('周杰伦111')
# print(s1)
# s2 = s.index('周杰伦')
# print(s2)
# print('周杰伦' in s) #in可以做条件上的判断
# # for c in s:
# #     print(c)
# print('周杰伦' not in s)
# # 判断
# name = input('plz tap ur name:')
# # if name.startswith('张'):
# #     print('你姓张')
# # else:
# #     print('你不姓张')
# money = input('plz tap ur money:')
# if money.isdigit():
#     money = int(money)
#     print('u have money')
# else:
#     print('u dont have money')
# # startwith(),isdigit(),in,not in,find ,index
# # str 补充和总结
# s = 'hello'
# print(len(s))
# # join()
# lst = ['aba','xcx','ggg','trwet']
# #用_连起来lst中字符串
# s = '_'.join(lst)
# print(s)

#总结
'''
1.f{变量} 格式化一个字符串
2.索引和切片：
    索引：从0开始 []
    切片：s[start:end:step] end位置拿不到
3.相关操作
    字符串操作对原字符串是不发生改变的
    1.upper() 在需要忽略大小写时候
    2.strip() 去掉字符串左右两端的空白（空格,/t,/n)
    3.replace（） 字符串替换
    4.split（） 对字符串切割
    5.join（）列表中的内容 字符串拼接
    6.startswith() 判断字符串是否已xx开头
    7.len() 字符串长度 内置函数
    字符串的循环和遍历
    for c in s:
        print(c) 字符串中的每一个字符
    关于in：
        1.判断xxx是否在xxxx中出现了
        2.for循环
'''
