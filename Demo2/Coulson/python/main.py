def func(d):
    for k, v in d.items():
        if isinstance(v, int):
            d[k] = str(v)
        if isinstance(v, dict):
            func(v)
    return d


if __name__ == '__main__':
    d = {"a": 1, "b": {"aa": 2, "bb": 15}}
    print(func(d))





