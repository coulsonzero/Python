'''
input:
AABCCC
2
output: 2
{(C:3), (A:2), (B:1)}
'''

s = input().upper()
k = int(input())
# s = 'AAAAHHHBBCDHHHH'
# k = 3

# 双指针法
a = dict()
l = r = 0
while r < len(s):
    if s[r] == s[l]:
        r += 1
        if r == len(s)-1:
            a[s[l]] = max(a.get(s[l], 0), r-l+1)
    else:
        a[s[l]] = max(a.get(s[l], 0), r-l)
        l = r
print(sorted(a.items(), key=lambda x: x[1], reverse=True)[k-1][1])