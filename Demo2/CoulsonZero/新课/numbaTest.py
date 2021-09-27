from numba import jit
import time

@jit(nopython=True)
def computeSum(size: float) -> int:
    sum = 0
    for i in range(size):
        sum += 1
        return sum

@jit(nopython=True)
def main():
    size = 100000
    for _ in range(size):
        sum = computeSum(size)

if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print(f'cpu执行用时: {(end - start) * 1000:.3f} ms')
