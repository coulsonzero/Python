from icecream import ic

def func(A, B, X):
    d = sum(A)
    for i in range(len(B)):
        if B[i] == 0:
            A[i] = 0
    # 计算子数组最大连续和
    res = 0
    for i in range(len(A)):
        if A[i] != 0:
            res = max(sum(A[i:i+X]), res)
    return (d-sum(A)+res)

if __name__ == '__main__':
    # A = [1, 1, 1, 1, 1, 1, 1, 1]
    # B = [0, 0, 0, 0, 1, 0, 0, 0]
    # X = 2
    A = [1, 2, 3, 4, 3, 2, 4, 5, 10, 1, 6]
    B = [0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0]
    X = 2
    ic(func(A, B, X))

