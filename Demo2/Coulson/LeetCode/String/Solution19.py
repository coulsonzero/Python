from icecream import ic

'''
lc 最长公共前缀
input: strs = ["flower", "flow", "flight"]
output: "fl"

分治法
时间复杂度：O(mn) m为数组中祖字符串的平均长度，n是字符串数量。时间复杂度递推式是T(n)=2*T(n/2)+O(m) => T(n)=O(mn)
空间复杂度：O(m logn) 最大递归层次为logn，每层需要m的空间存储返回结果
'''
class Solution:
    def longestCommonPrefix(self, strs):
        def lcp(start, end):
            if start == end:
                return strs[start]

            mid = (start + end) // 2
            lcpLeft, lcpRight = lcp(start, mid), lcp(mid+1, end)
            minLength = min(len(lcpLeft), len(lcpRight))
            for i in range(minLength):
                if lcpLeft[i] != lcpRight[i]:
                    return lcpLeft[:i]
            return lcpLeft[:minLength]
        return "" if not strs else lcp(0, len(strs)-1)

if __name__ == '__main__':
    strs = ["flower", "flow", "flight"]
    a = Solution()
    ic(a.longestCommonPrefix(strs))     # 'fl'



