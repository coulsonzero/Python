import os

# path = r'C:\Users\21059\Desktop\python code'
# os.chdir(path)    # 切换当前工作目录为python code

# os.startfile(r'D:\Program Files (x86)\Cloud music\cloudmusic.exe')
# os.makedirs('./test')
# print(os.getcwd())    #显示工作目录是否正确

# os.rmdir(path+'./test')
# print(os.walk(top='Tips'))
# print(os.listdir())

class Visit:
    def visitDir(self,path):
        global dirNums,fileNums
        list_dirs = os.walk(path)
        for root, dirs, files in list_dirs:
            for d in dirs:
                dirNums += 1
                print(os.path.join(root, d))
            for f in files:
                if f.endswith('py'):
                    fileNums += 1
                    print(os.path.join(root,f))

    def output(self,path):
        print(f'The Total number of directories in {path} is: {dirNums}')
        print(f'The Total number of files  in {path} is: {fileNums}')

    def main(self,path):
        if not os.path.isdir(path):
            print('FileNotFoundError:', path, 'is not a directory or does not exist.')
            return
if __name__ == '__main__':
    dirNums, fileNums = 0, 0
    path = r'C:\Users\21059\Desktop\python code'
    a=Visit()
    a.visitDir(path)
    a.main(path)
    a.output(path)


# #列出子目录
# file_list = os.listdir(path)
# print(os.listdir(path))
# print("——————————————————————————————————————————————")
# #列出子文件
# for filename in file_list:
#     if filename.endswith("py"):
#
#         print(filename)     #,end="\t" 则并排显示
#
# print("——————————————————————————————————————————————")
# file_list2 = [filename for filename in os.listdir(path) if filename.endswith("py")]
# for f in file_list2:
#     print(f,end="\t")