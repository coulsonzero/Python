from numba import jit
from numpy import arange
import time

@jit(nopython=True)
# @jit()
def sum2d(arr):
    M,N =arr.shape
    result =0.0
    for i in range(M):
        for j in range(N):
            result += arr[i,j]
    return result
if __name__ == '__main__':
    start = time.process_time()
    a = arange(99999999).reshape(33333333, 3)
    sum2d(a)
    end = time.process_time()
    print(f'cpu执行用时: {(end - start) :.3f} s')
