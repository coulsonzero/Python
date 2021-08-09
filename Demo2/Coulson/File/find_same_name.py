import os

site=input("文件位置：")

def file_name(file_dir):
    a=[]
    for root,dirs,files in os.walk(file_dir):
        b=dirs
        a.extend(b)
        c=files
        a.extend(c)
    return a
file_list = file_name(site)
file_set_list = list(set(file_list))
file_dic={}
for i in file_set_list:
    count=0
    for m in file_list:
        if i == m:
            count+=1
    file_dic[i]=count
for key in file_dic:
    if file_dic[key]>1:
        print(key)


