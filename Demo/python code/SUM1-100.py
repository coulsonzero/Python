#用while来计算1到1000的总和
n=1000
sum=0
counter=1
while counter<=n:
    sum+=counter
    counter+=1    
    print("Sum of 1 until %d: %d" % (n,sum)) 
