
import urllib.request
import json
import os

response = urllib.request.urlopen("http://pvp.qq.com/web201605/js/herolist.json")

hero_json = json.loads(response.read())
hero_num = len(hero_json)

save_dir = r'C:\Users\21059\Desktop\Tips\wangzhe\\'
if not os.path.exists(save_dir):

    os.mkdir(save_dir)
for i in range(hero_num):
    skin_names = hero_json[i]['skin_name'].split('|')
    for cnt in range(len(skin_names)):
        save_file_name = save_dir + str(hero_json[i]['ename']) +'-'+hero_json[i]['cname']+'-'+skin_names[cnt]+'.jpg'
        skin_url = "https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/"+str(hero_json[i]['ename'])+'/'+str(hero_json[i]['ename'])+'-bigskin-'+str(cnt+1)+'.jpg'
        if not os.path.exists(save_file_name):
            urllib.request.urlretrieve(skin_url, save_file_name)
