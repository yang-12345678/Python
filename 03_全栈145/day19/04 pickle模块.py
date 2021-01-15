import pickle

'''pickle和json的不同
    1. dumps序列化的结果只能是字节
    2.pickle 支持在python中几乎所有的数据类型
    3.pickle看不见结果, 只有字节
    4.pickle只能在python中使用
    5.pickle在和文件进行操作的时候，需要使用 rb wb 模式打开文件
    6.pickle可以多次dump，多次load
'''

dic = {'1': '2', '3': '4'}

ret = pickle.dumps(dic)
print(ret)  # bytes
res = pickle.loads(ret)
print(res)