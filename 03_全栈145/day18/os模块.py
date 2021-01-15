import os

# os是和操作系统打交道的模块
'''
import os
print(os.getcwd())获取当前工作目录
 os.chdir()改变当前脚本工作目录
print(os.curdir#返回当前目录 .
print(os.pardir)获取当前目录的父目录字符串名 ..

os.makedirs() 生成多层递归目录
os.removedirs() 若目录为空，则删除，并递归到上一级目录，若也为空，则删除，以此类推
os.mkdir()生成单级目录
os.rmdir()删除单级空目录
os.listdir()列出指定目录下的所有文件和子文件，并以列表的形式打印
os.remove()删除一个文件
os.rename() 重命名文件/目录
os.stat()获取文件/目录
os.sep 输出操作系统特定的路径分隔符
os.linesep 输出当前平台使用的行终止符
os.pathsep 输出用于分割文件路径的字符串
os.name 输出字符串指示当前使用平台
os.system(‘bbb’) 运行shell命令，直接显示
os.popen(‘bbb’).read()运行shell命令，获取执行结果
os.environ 获取系统环境变量


os.path
os.path.abspath(path)返回path规范化的绝对路径

os.path.split(path） 将path分割成目录和文件名二元制组返回

os.path.dirname(path)返回path的目录 就是os.path.split(path）的第一个元素， os.path.basename（path）返回path最后的文件名。如果path以/或\结尾，那么返回空值
os.path.exists(path) 如果path存在，返回True,，不存在，返回False
os.path.isabs(path) 判断是否是绝对路径
os.path.isfile(path) 判断path是否是一个存在的文件
os.path.isdir(path) 判断path是否是一个存在的目录
os.path.join(path1[...],path2[..]) 将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
os.path.getatime(path) 返回path所执行的文件或目录的最后访问时间
os.path.getmtime(path) 返回path所执行的文件或目录最后修改时间
os.path.getsize(path) 返回path大小
'''
ret = os.listdir("./")
rs = os.path.join(ret[0], './')
print(rs)

