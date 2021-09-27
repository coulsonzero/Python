from collections import Counter
with open(r'C:\Users\21059\Desktop\Tips\data.txt', 'r') as f:
    a = f.read().split()
d = Counter(a)
s = d.most_common(10)
c= {}
for i in s:
    c[i[0]] = i[1]
print(c)