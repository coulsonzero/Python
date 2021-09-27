#创建迭代器对象
#迭代器：iter()、next()

list=[1, 2, 3, 4]
it=iter(list)    #创建迭代器对象
for x in it:
    print(x, end="")
