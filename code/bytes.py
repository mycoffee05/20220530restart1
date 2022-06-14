'''
    1.字符和编码
    0 1 <=> 二进制转化成十进制 <=> 1
    电脑如何存储文字信息
    10000000 <=> a
    ascii =>编排了128个文字符号 含操作符，只需要7个01就可以表示了 01111111 => 1 byte => 8bit
    ANSI => 一套标准 每个字符占16bit，2bytes
    00000000 01111111 2的16次方编码
    中国 GB2312编码，GBK编码 国标扩（win默认），GB18030，
    01000000 01010101
    台湾 big5编码
    日本 JIS编码

    游戏DNF 台服 韩服切换文字标准

    Unicode 万国码
    早期 ucs-2 2个字节
    扩充后 UCS-4 4个字节
    00000000 00000000 00000000 00000001

    utf:可变长度的unicode，可以进行数据传输和存储 ->行书、草书、隶属
    utf-8 最短字节长度是8
        英文：8bit 1byte
        欧洲文字： 16bit 2byte
        中文： 24bit 3byte
    utf-16

    总结：
        1.ascii 8bit 1byte
        2.gbk 16bit 2byte win默认
        3.Unicode 32bit 4byte
        4.utf-8 mac默认

        gbk和utf-8不能直接进行转化
        我军 <-> 文字 <-> 敌军
    2.bytes
        所有的数据最终单位都是字节byte

'''
# print(2**16)
# s = '周杰伦'
# bs = s.encode('gbk') #b'xxx' bytes类型
# bs1 = s.encode('utf-8')
# print(bs)
# print(bs1)
# gbk转化为utf-8
# bs = b'\xd6\xdc\xbd\xdc\xc2\xd7'
# s = bs.decode('gbk')
# bs1 = s.encode('utf-8')
# print(s)
# print(bs1)
# 1.str.encode('编码') 进行编码
# 2.bytes.decode('编码') 进行解码
s = '您好aaa哈哈哈'
print(s.encode('gbk'))