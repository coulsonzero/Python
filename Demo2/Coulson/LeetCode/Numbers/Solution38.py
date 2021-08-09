'''
lc 计数质数

统计所有小于非负整数 n 的质数的数量。


输入：n = 10
输出：4
解释：小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
'''


# 埃氏筛选法
class Solution:
    def countPrimes(self, n: int) -> int:
        isNumPrimes = [True] * n   #将所有数标记为质数
        count = 0  # 质数计数器 因为1不是质数 所以 0
        for i in range(2, n):
            if isNumPrimes[i]:
                count += 1
                # 使用埃拉托斯特尼 筛选法进行过滤 将合数去除
                for j in range(i*i, n, i): #遍历 i*i  2倍i值 开始，结束n, 步数i (倍数递增)
                    isNumPrimes[j] = False # 把合数置为 False
        return count

# 执行用时：1112 ms, 在所有 Python3 提交中击败了59.99%的用户

'''
# 常规方法
class Solution:
    def countPrimes(self, n: int) -> int:
        cnt = 0
        for i in range(2,n):
            if self.isPrime(i):
                cnt += 1  
            # else:
            #     cnt += 0
        return cnt

    def isPrime(self, x:int) -> bool: 
        i = 2
        while i*i <= x:
            if x % i == 0:
                return False
            i += 1
        return True
# 超出时间限制
'''


'''
# 时间复杂度：O(n)
def isPrime(n):
    if n <= 3:
        return n > 1
    for i in range(2, n+1):
        if n%i == 0:
            return False
    return True
'''

'''
# 时间复杂度：O(n**0.5)
def isPrime(n):
    if n <= 3:
        return n > 1
    for i in range(2, n**0.5+1):
        if n%i == 0:
            return False
    return True
'''


'''
# 时间复杂度：O((n**0.5)/2)
def isPrime(n):
    if n <= 3:
        return n > 1
    for i in range(3, n**0.5+1, 2):
        if n%i == 0 or n%2 == 0:
            return False
    return True
'''
