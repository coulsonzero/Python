
with open(r"C:\Users\21059\Desktop\Tips\data.txt", "r", encoding='utf-8') as fp:
    words = fp.readlines()
    for j in range(len(words)):
        if '\n' in words[j]:
            words[j] = words[j].replace('\n', '')
            j += 1
    print(words)
    for i in range(4):
        print('{0}{1}'.format(words[i][0], len(words[i])))
        i += 1