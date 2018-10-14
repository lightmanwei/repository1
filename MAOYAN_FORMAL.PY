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
        return None
    except RequestException:
        return None





def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(\d*)</i>.*?data-src=\"(.*?)\".*?name.*?title=\"(.*?)\".*?'
                         '主演：(.*?)\n.*?上映时间：(.*?)</p>.*?integer\">(\d.).*?fraction\">(\d)', re.S)
    items = re.findall(pattern, html)
    list = []
    for item in items:
        yield[
            item[0]+',',
            item[1]+',',
            item[2]+',',
            item[3]+',',
            item[4]+',',
            item[5] + item[6]+' ,'
        ]
        list.append(item[2:6])




        url = item[1]
        path = '/Users/gikosei/PycharmProjects/spider/maoyan/' + item[0] +'.jpg'

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
    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)
    parse_one_page(html)
    for list in parse_one_page(html):
        print(list)
        write_list_csv(list[2:5], '/Users/gikosei/PycharmProjects/spider/maoyan/result.csv')

if __name__ == '__main__':
    for i in range(10):
        main(i*10)
