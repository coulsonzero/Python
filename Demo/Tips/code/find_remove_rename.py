import os


print(
    '''
         ——————————————————————————————   
        |                快速查找重复文件                           |
        |                快速移除重复文件                           |
        |                修改重复文件名及格式                       |
        |                C:/Users/21059/Desktop                     |
         ——————————————————————————————
    '''
)


site=input("文件位置<C:/Users/21059/Desktop/python code>：")


#查找重复名
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
        #print(key)


        # 查找重复名
        def file_name(file_dir):
            a = []
            for root, dirs, files in os.walk(file_dir):
                b = dirs
                a.extend(b)
                c = files
                a.extend(c)
            return a


        file_list = file_name(site)
        file_set_list = list(set(file_list))
        file_dic = {}
        for i in file_set_list:
            count = 0
            for m in file_list:
                if i == m:
                    count += 1
            file_dic[i] = count
        for key in file_dic:
            if file_dic[key] > 1:
                print(key)


        e = input("要移除的文件名及格式（如：资产负债表.xlsx)：")

        def deleteFiles():
            for root, dirs, files in os.walk(wanted_del_file_dir):  # 遍历目标文件位置
                for file_name in files:
                    file_path = os.path.join(root, file_name)  # 提取所有文件路径
                    # print(file_path)
                    if file_name in del_file_list:  # 如果文件在目标文件中
                        print(f'Deleted: {file_path}')
                        os.remove(file_path)  # 删除目标文件


        if __name__ == '__main__':
            wanted_del_file_dir = site
            del_file_list = [e,
                             ]
            deleteFiles()
            print('''
            删除完成！
            ————————————————————————————————————————————————————
            ''')

    #文件重命名
        d = site
        a = input("要修改的原文件名(如：资产负债表):" )
        c = input("新文件名：")
        b = input("原文件扩展名（如：xlsx/txt)：")

        def renameFiles():
            for root, dirs, files in os.walk(wanted_rename_file_dir):
                for file_name in files:
                    file_path = os.path.join(root, file_name)
                    #print(file_path)

                    if file_name in del_rename_list:
                        #print(f'renamed: {file_path}')
                        if file_name.endswith(b):                  #文件扩展名
                            src = os.path.join(root,file_name)
                            dst = os.path.join(root,c+'.'+b)        #想要的文件名
                            try:
                                os.rename(src, dst)
                                print(f'已经重命名的文件有：{src} --->>> {c}.{b}')
                            except:
                                continue

        if __name__ == '__main__':
            wanted_rename_file_dir = d
            del_rename_list = [a+'.'+b,                              #原文件名
                               ]
            renameFiles()
            print('''
            重命名完成！
            ————————————————————————————————————————————————————
            ''')
