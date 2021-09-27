with open(r'txt.txt','r',encoding='utf-8') as fp:
    words = fp.read().split()
aDict = dict()
for word in words:
    aDict[word] = aDict.get(word, 0) + 1
print(dict(sorted(aDict.items(), key=lambda x : x[1], reverse=True)[:10]))
