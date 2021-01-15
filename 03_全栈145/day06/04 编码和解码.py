# -*- encoding:utf-8 -*-

# s = 'alex'
# print(s.encode('utf-8'))  # 编码
# # bytes  b'alex'

s = '饿了吗'
# print(s.encode()) # b'\xe9\xa5\xbf\xe4\xba\x86\xe5\x90\x97'  三个字节一个字
# print(s.encode('gbk'))  # b'\xb6\xf6\xc1\xcb\xc2\xf0'

'''
   encoding(编码方式)  -----拿到明文编码后对应的字节
   decoding(解码方式)  -----将编码后的字节解码成对应的明文
'''
