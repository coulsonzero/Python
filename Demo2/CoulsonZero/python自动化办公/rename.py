import os

d = input("文件总目录位置（如：C:/Users/21059/Desktop/python code）：")
a = input("要改的原文件名(如：资产负债表):" )
b = input ("要改的原文件的扩展名（如：xlsx/txt)：" )
c = input("想要的文件名：")


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
    print('重命名完成！')

