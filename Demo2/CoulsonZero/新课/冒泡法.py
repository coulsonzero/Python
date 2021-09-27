import time
import random
from numba import jit

# @jit(nopython=True)
def bubble_sort(nums):

    s = len(nums)
    for i in range(s):
        for j in range(1, s-i):
            if nums[j-1] > nums[j]:
                nums[j-1], nums[j] = nums[j], nums[j-1]
                return nums

if __name__ == '__main__':
    start = time.process_time()
    # nums = []
    # for i in range(20000):
    #     nums.append(random.randint(1,50000))
    # nums = sorted(nums)
    nums = sorted([random.randint(1, 5000000) for i in range(2000000)])

    # print(nums)
    bubble_sort(nums)
    end = time.process_time()
    print(f'cpu执行用时: {(end - start):.3f} s')