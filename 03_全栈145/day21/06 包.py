x = 1

'''
包：文件夹中有一个__init__.py文件
包：是几个模块的集合
'''

# 从包中导入模块

# import
# import glance.api.my_module  # as my_module
#
# glance.api.my_module.get()

# from import
# from glance.api import my_module


''' 
直接导入包  需要通过设计 __init__.py文件，来完成导入包后的操作
绝对导入

优点：在执行一个py脚本的时候，这个脚本 以及和这个脚本之间同级的模块中只能用绝对导入

缺点：如果当前导入包的文件和被导入包的位置关系发生了变化，那么所有的__init__.py文件都应做出相应的调整
     所有的导入都要从一个根目录下往后解释文件夹之间的关系（设计__init__.py文件）
     
'''
# import glance
# sys.path = ['E:\Python\03_全栈145']
# 在__init__ 中from import

# 导入一个包不意味着这个包下面的所有的内容都是可以被使用的
# 导入一个包相当于执行了这个包下面的 __init__.py文件


'''
相对导入：
    from . import []
    
    优点：不需要反复修改路径，只要一个包中的所有文件夹和文件的相对位置不发生改变
    
    缺点：含有相对导入的文件不能被直接执行，必须放在包里被导入的调用
'''
