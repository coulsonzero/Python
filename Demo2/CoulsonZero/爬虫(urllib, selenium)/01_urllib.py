from urllib import request
from urllib import parse
import re

# 1. 拼接URL地址
word = input('请输入必应搜索关键字:')
# parms = parse.urlencode({'q': word})
# url = 'http://cn.bing.com/search?{}'.format(parms)
parms = parse.quote(word)
url = 'http://cn.bing.com/search?q={}'.format(parms)
print(url)
headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'}

# 2. 发送请求获取响应内容
req = request.Request(url=url, headers=headers)
res = request.urlopen(req)
html = res.read().decode()

# 3. 保存到本地文件
filename = word + '.html'
with open(filename, 'w', encoding='utf-8') as f:
    f.write(html)
    pattern = re.compile('<title>(.*)</title>', re.S)
    r_list = pattern.findall(html)
    print(r_list)