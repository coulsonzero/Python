#用walk（）遍历所有子目录和子文件

import os

all_files = []
path = "C:/Users/21059/Desktop/python code"
os.chdir(path)         #改变当前工作目录为：
print(os.getcwd())   #获取当前工作目录
list_files = os.walk(path)

for dirpath, dirnames, filenames in list_files:
    for dir in dirnames:
        all_files.append(os.path.join(dir))
    for file in filenames:
        all_files.append(os.path.join(file))

#打印所有子目录和子文件
#for file in all_files:
#    print(file)

#列出子文件
for filename in all_files:
    if filename.endswith("ps"):

        print(filename)     #,end="\t" 则并排显示
