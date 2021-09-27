from icecream import ic
import time



# 定义装饰器
def run_time(func):
    def print_time(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(end-start)
    return print_time()

# 使用装饰器
# @run_time
def func1(t):
    time.sleep(t)

if __name__ == '__main__':
    ic(func1(3))