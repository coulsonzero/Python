import os

def deleteFiles():
    for root, dirs, files in os.walk(wanted_del_file_dir):   #遍历目标文件位置
        for file_name in files:
            file_path = os.path.join(root, file_name)        #提取所有文件路径
            #print(file_path)
            if file_name in del_file_list:                   #如果文件在目标文件中
                print(f'Deleted: {file_path}')
                os.remove(file_path)                         #删除目标文件

if __name__ == '__main__':
    wanted_del_file_dir = u'C:/Users/21059/Desktop/python code'
    del_file_list = ['.docx',
                     '.xlsx',
                     ]
    deleteFiles()
    print('删除完成！')