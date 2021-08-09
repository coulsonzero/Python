from icecream import ic
import os

class FileVisit(object):
    def visitDir(self, path):
        if not os.path.isdir(path):
            ic(f"Error: {path} is not a directory or does not exist!")
            return
        list_dirs = os.walk(path)
        for root, dirs, files in list_dirs:
            for d in dirs:
                ic(os.path.join(root, d))
            for f in files:
                ic(os.path.join(root, f))

if __name__ == '__main__':
    a = FileVisit()
    p = r"C:\Users\21059\Desktop\python code"
    # ic.disable()
    a.visitDir(p)
    