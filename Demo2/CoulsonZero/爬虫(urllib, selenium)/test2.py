
def twoSum(nums, target):
    dct = {}
    for k, v in enumerate(nums):
        if target - v in dct:
            print([dct[target - v], k])
        else:
            dct[v] = k
    return None
    # print(dict(enumerate(nums)))

if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    tagert = 16
    twoSum(nums, tagert)
