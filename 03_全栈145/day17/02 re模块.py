import re

# findall  匹配所有

# ret = re.findall(r"\d+", "woshiagoi928你好")
# ret = re.findall(r"\d", "woshiagoi928你好")
# print(ret)

# search  只匹配第一个，返回的是内存地址(正则匹配的结果)，span是索引

# ret = re.search(r"\d+", "woshiagoi928你好")
# print(ret)
# print(ret.group())  # 通过ret.group()获取真正的结果

'''没有匹配到会返回None，不能再使用group,否则报错'''
# ret = re.search(r"\d", "dogijaojge")
# print(ret)

# match  相当于在search方法的正则表达式中加 ^, 即从头开始匹配

# ret = re.match(r"\d+", "323jaijfaojg172你好123")
# print(ret.group())

# 字符串处理的扩展： 替换，切割

# split 切割
# s = "alex83taibai40egon25"
# ret = re.split(r'\d+', s)
# print(ret)

# sub 替换: 对象，旧的，新的，次数
# ret = re.sub(r"\d+", "H", "alex23")
# print(ret)

# subn  会返回一个元组，第二个元素是替换的次数
# ret = re.subn(r"\d+", "H", "alex23")
# print(ret)

# re模块的进阶，：compile（节省时间） 和 finditer（节省空间）
# compile 把正则表达式编译成字节码，在多次使用的过程中不会多次编译
# ret = re.compile(r"\d+")
# print(ret)
# res = ret.findall("alex83taibai40egon25")  # 直接用编译的结果findall
# print(res)

# finditer
# ret = re.finditer(r"\d+", "alex83taibai40egon25")
# print(ret)  # 迭代器对象
# for i in ret:
#     print(i.group())
