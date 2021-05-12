import time
import random
from numba import jit

'''
相对于冒泡排序法极大地提高了运算效率
numba.jit可实现科学运算加速，当计算量巨大时可明显提高效率，当计算量小时反而出现增加耗时
'''
# @jit(nopathon = True)
# @vectorize()
def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums)//2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
#     return merge(left, right)
#
# def merge(left, right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    if left:
        result += left
    if right:
        result += right
    return result

if __name__ == '__main__':
    start = time.time()
    nums = []
    for i in range(2000000):
        nums.append(random.randint(1, 5000000))
    nums = sorted(nums)
    # new_nums = sorted([random.randint(1,50000) for i in range(20000)])
    # new_nums = merge_sort(new_nums)

    # print(new_nums)
    # print(len(new_nums))
    end = time.time()
    print(f'cpu执行用时: {(end - start) :.3f} s')



