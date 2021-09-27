#请求网页
import requests
import json
if __name__ == "__main__":
    url = 'https://movie.douban.com/j/search_subjects'
    param = {
        'type': 'tv',
        'tag': '热门',
        'page_limit': '50',
        'page_start': '0',
    }
    headers = {
        'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36'
    }
    response = requests.get(url=url, params =param, headers=headers)
    list_data = rasponse.json()
    fp = open('./douban.json','w',encoding='utf-8')
    json.dump(list_data,fp=fp,ensure_ascil=False)

    print('over!!!')


