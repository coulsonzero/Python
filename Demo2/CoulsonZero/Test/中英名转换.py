from pypinyin import lazy_pinyin


def __getattr__(name):
    CN_Name = lazy_pinyin(name)
    if len(CN_Name) <= 3:
        fastname = CN_Name.pop(0)
        lastname= ''.join(CN_Name)
        Eng_Name = lastname + ' ' + fastname
    elif len(CN_Name) > 3:
        fastname1 = CN_Name.pop(0)
        fastname2 = CN_Name.pop(0)
        print(CN_Name)
        lastname= ''.join(CN_Name)
        Eng_Name = lastname + ' ' + fastname1+fastname2
    print(Eng_Name.title())
if __name__ == '__main__':
    name = input("姓名：")
    __getattr__(name)
