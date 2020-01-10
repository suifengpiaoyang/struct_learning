import struct
import binascii

'''
这个脚本的例子在[廖雪峰的Python3.x教程]
(https://www.kancloud.cn/smilesb101/python3_x/298874)
的 struct 模块教学里面。
给出来的例子是：

无符号整数变字节数
在Python中，比方说要把一个32位无符号整数变成字节，
也就是4个长度的bytes，你得配合位运算符这么写：

>>> n = 10240099
>>> b1 = (n & 0xff000000) >> 24
>>> b2 = (n & 0xff0000) >> 16
>>> b3 = (n & 0xff00) >> 8
>>> b4 = n & 0xff
>>> bs = bytes([b1, b2, b3, b4])
>>> bs
b'\x00\x9c@c'

>>其实 python 内置了 binascii 模块，里面有个函数
可以直接将十六进制数转换成二进制 ascii 。也不算需要
这么麻烦。

最后，引入目标，将要学习的 struct 模块。
'''

def demo():
    # “&” 符号是 “与” 的含义；“>>” 是“右移”
    # b1 到 b4 的意思就是，将 n 值划分成 4 个字节，
    # 并将每个字节的值都提取出来成十进制数。
    # 用于 bytes 函数的转换。高位的需要右移以取消
    # 二进制数右边的 0
    n = 10240099
    b1 = (n & 0xff000000) >> 24
    b2 = (n & 0xff0000) >> 16
    b3 = (n & 0xff00) >> 8
    b4 = n & 0xff
    bs = bytes([b1, b2, b3, b4])
    print(bs)                                   # b'\x00\x9c@c'

def demo_extendsion_1():

    # {:08x} 对于十六进制而言，每个数占据 4 个比特，
    # 2个数为一个字节。所以 8 位的十六进制数，共 4
    # 个字节。
    n = 10240099
    format_n = '{:08x}'.format(n)               # '009c4063'
    result = binascii.unhexlify(format_n)       # b'\x00\x9c@c'
    print(result)

def demo_extendsion_2():

    # 使用 struct 模块
    # pack 打包，'>I' 格式化，> 号表示大端存储，I 表示转换成
    # 4 字节的数，对应 C 语言的 unsigned int
    n = 10240099
    result = struct.pack('>I', n)               # b'\x00\x9c@c'
    print(result)

def demo2():

    # unpack把bytes变成相应的数据类型
    # 对于下面的 n 而言，每一个类似 \xf0 的为一个字节，
    # 所以不难看出，n 有 6 个字节
    # I 解析出 4 个字节，H 解析 2 个字节
    # 所以结果就是解析出前面 4 个字节合成的十进制数和
    # 后面两个字节合成的十进制数
    # H 表示2个字节的数字
    n =  b'\xf0\xf0\xf0\xf0\x80\x80'
    result = struct.unpack('>IH', n)            # (4042322160, 32896)
    print(result)

def demo2_extendsion_1():

    # 写一个函数来证明以上的结论
    n = b'\xf0\xf0\xf0\xf0\x80\x80'
    hex_n = binascii.hexlify(n).decode()                # 'f0f0f0f08080'
    front_4_bytes_num = int(hex_n[:8], 16)              # 4042322160
    behind_2_bytes_num = int(hex_n[8:], 16)             # 32896
    print((front_4_bytes_num,behind_2_bytes_num))       # (4042322160, 32896)

if __name__ == '__main__':

    # The following three demo can get the same result.
    demo()
    demo_extendsion_1()
    demo_extendsion_2()

    # The following two demo can get the same result.
    demo2()
    demo2_extendsion_1()
    