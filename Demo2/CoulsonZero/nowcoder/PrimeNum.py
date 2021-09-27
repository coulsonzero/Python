import math

n = int(input())
a = [i for i in range(2, n) if 0 not in [i % j for j in range(2, int(math.sqrt(i))+1)]]
print(a)