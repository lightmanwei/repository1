import os
import requests
import re
from requests.exceptions import RequestException

headers = {'Accept': '*/*',
           'Accept-Language': 'en-US,en;q=0.8', 'Cache-Control': 'max-age=0', 'User-Agent':
               'Mozilla/5.0 (X11; Linux x86_64) '
               'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
           'Connection': 'keep-alive', 'Referer': 'http://www.baidu.com/'}


def get_one_page(url):
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return 'error'
    except RequestException:
        return 'error'





def parse_one_page_download(html):
    pattern = re.compile('.*?<em class="">(.*?)</.*?src="(.*?)".*?<span class="title">(.*?)<.*?'
                         '导演: (.*?)&.*?主演.*?;/&nbsp;(.*?)&.*?/&nbsp;(.*?)\n.*?'
                         '"v:average">(.*?)<.*?<span class="inq">(.*?)', re.S)

    items = re.findall(pattern, html)
    list = []
    for item in items:
        yield[
            item[1]+',',
            item[0]+',',
            item[2]+',',
            item[3]+',',
            item[4]+',',
            item[5]+',',
            item[6] + ',',
            item[7] + ','
        ]
        list.append(item[1:7])




        url = item[0]
        path = '/Users/gikosei/PycharmProjects/spider/douban/' + item[1] +'.jpg'

        try:
            if not os.path.exists(path):
                r = requests.get(url)
                with open(path, 'wb') as f:
                    f.write(r.content)
                    f.close()
                    print("ok")
            else:
                print('error')
        except:
            print("error")


def write_list_csv(list,filepath):
    try:
        file = open(filepath, 'a')
        for items in list:

            file.writelines(items)
            file.close
        file.write('\n')
    except Exception:
        print("writing error")



def main(offset):
    url = 'https://movie.douban.com/top250?start=' + str(offset) + '&filter='
    html = get_one_page(url)
    parse_one_page_download(html)
    for list in parse_one_page_download(html):
        print(list[1:7])
        write_list_csv(list[1:7], '/Users/gikosei/PycharmProjects/spider/douban/result2.csv')

if __name__ == '__main__':
    for i in range(10):
        main(i*25)
