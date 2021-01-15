import re

# s = '<a>wahaha</a>'  # 标记语言HTML
# ret = re.search(r'>(\w+)<', s)
# print(ret.group(1))  # 取第一个分组，还可以有更多，第0个分组默认是所有


# 为了findall也可以顺利取到分组中的内容，有一个特殊的语法，就是优先显示分组中的内容
# s = '<a>wahaha</a>'
# # 分组优先
# ret = re.findall(r'>(\w+)<', s)
# print(ret)
#
# ret = re.findall(r'\d+(\.\d+)', '1.234*4.3')  # 优先显示问题
# print(ret)

# 取消分组优先：（？：正则表达式）
# ret = re.findall(r'\d+(?:\.\d+)', '1.234*4.3')
# print(ret)

# split
# ret = re.split(r'(\d+)', "alex83taibai40egon25")  # 加上分组后，分组中的内容会被保留
# print(ret)

# 分组命名  (?P<分组的名字>正则表达式) 不能用数字
# s = '<a>wahaha</a>'
# ret = re.search(r'>(?P<content>\w+)<', s)
# print(ret.group(1))
# print(ret.group('content'))

# 使用前面的分组名，要求使用这个名字的分组和前面同名分组中的内容匹配的必须一致
# 也可以用分组的索引，   \1
# s = '<a>wahaha</b>'
# pattern = r'<(?P<tap>\w+)>(\w+)</(?P=tap)>'
# ret = re.search(patte  rn, s)
# print(ret)
