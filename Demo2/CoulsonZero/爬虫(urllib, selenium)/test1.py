import re

s = '<title>python - 国内版 Bing</title>'

def re_text(text):
    pattern = re.compile(f'<title>{text}</title>', re.S)
    r_list = pattern.findall(s)
    print(r_list)
if __name__ == '__main__':
    re_text('.*')
    re_text(text='(.*)')




c = """<em class="tb-rmb">¥</em><em class="tb-rmb-num">998.00</em>"""
pattern = re.compile('<em class="tb-rmb">(.*)</em><em class="tb-rmb-num">(.*?)</em>', re.S)
r_list = pattern.findall(c)
print(''.join(list(r_list[0])))
# print(r_list)



a = 'A B C D E F G'
pattern = re.compile('\w+\s+\w+')
r_list = pattern.findall(a)
print(r_list)