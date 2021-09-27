'''
input: 3 5 7 -1 -1 2 6
output: 3-7-2
     3
    / \
   5   7
      / \
     2   6
'''
class Soultion(object):
    def func(self, root, res):
        res = ''
        if root != None:
            res += root
        while root.right != None:
            res += root.right
        return self.func(root.right, res)
    if __name__ == '__main__':
        s = '3 5 7 -1 -1 2 6'
        a = list(map(int, s))
        print(a)
        print(func(a))
