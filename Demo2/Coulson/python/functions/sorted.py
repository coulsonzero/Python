from collections import Counter
from icecream import ic
from operator import itemgetter

s = "hello world1345123"
d = Counter(s)
# ic(sorted(d.items(), key=itemgetter(1), reverse = True))
print(sorted(d.items(), key=lambda x: x[1], reverse=True)[0][1])

# for i, v in enumerate(s):
#     print(i,v, sep= ':')
a = {v:i for i, v in enumerate(s)}
ic(a)