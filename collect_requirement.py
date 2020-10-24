import requests
from bs4 import BeautifulSoup
import re
import time
import random

user_Agent = ['Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) '
              'Chrome/61.0.3163.100 Safari/537.36', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, '
                                                    'like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60',
              'Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50', 'Mozilla/4.0 ('
                                                                                                       'compatible; '
                                                                                                       'MSIE 6.0; '
                                                                                                       'Windows NT '
                                                                                                       '5.1; en) '
                                                                                                       'Opera 9.50',
              'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0', 'Mozilla/5.0 (X11; U; Linux '
                                                                                          'x86_64; zh-CN; '
                                                                                          'rv:1.9.2.10) '
                                                                                          'Gecko/20100922 '
                                                                                          'Ubuntu/10.10 (maverick) '
                                                                                          'Firefox/3.6.10',
              'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 '
              'Safari/534.57.2', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                 'Chrome/39.0.2171.71 Safari/537.36', 'Mozilla/5.0 (X11; Linux x86_64) '
                                                                      'AppleWebKit/537.11 (KHTML, like Gecko) '
                                                                      'Chrome/23.0.1271.64 Safari/537.11',
              'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) '
              'Chrome/10.0.648.133 Safari/534.16', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, '
                                                   'like Gecko) Chrome/30.0.1599.101 Safari/537.36', 'Mozilla/5.0 ('
                                                                                                     'Windows NT 6.1; '
                                                                                                     'WOW64; '
                                                                                                     'Trident/7.0; '
                                                                                                     'rv:11.0) like '
                                                                                                     'Gecko',
              'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 '
              'Safari/537.1 LBBROWSER', 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; '
                                        '.NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC '
                                        '6.0; .NET4.0C; .NET4.0E; LBBROWSER)', 'Mozilla/5.0 (compatible; MSIE 9.0; '
                                                                               'Windows NT 6.1; WOW64; Trident/5.0; '
                                                                               'SLCC2; .NET CLR 2.0.50727; .NET CLR '
                                                                               '3.5.30729; .NET CLR 3.0.30729; Media '
                                                                               'Center PC 6.0; .NET4.0C; .NET4.0E; '
                                                                               'QQBrowser/7.0.3698.400)',
              'Mozilla/4.0 ('
              'compatible; '
              'MSIE 6.0; '
              'Windows NT '
              '5.1; SV1; '
              'QQDownload '
              '732; '
              '.NET4.0C; '
              '.NET4.0E)',
              'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 '
              'SE 2.X MetaSr 1.0', 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload '
                                   '732; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0)']


class CollectRequirement():
    def __init__(self, filename):
        f = open('java后端test10_21.txt')
        url = f.readline()

        # n = 10
        while url:
            try:
                page = requests.get(url=url, headers={"User-Agent": random.choice(user_Agent)})
            except:
                print("Connection refused by the server..")
                print("Let me sleep for 5 seconds")
                print("ZZzzzz...")
                time.sleep(5)
                print("Was a nice sleep, now let me continue...")
                continue
            # time.sleep(1)
            # start=time.time()
            soup = BeautifulSoup(page.text, "html.parser")

            soup = soup.find('div', class_="content content-word")
            # require_content=soup.get_text()
            # print(soup)
            if soup is None:
                continue
            require_content = soup.get_text()
            require_content = require_content.replace('；', '\n')  # 把中文“分号”替换为换行符
            require_content = require_content.replace('。', '\n')
            require_content = require_content.replace('：', '\n')
            fw = open(filename, 'a', encoding='utf-8')
            fw.write(require_content)
            fw.close()
            # print(require_content)
            print(require_content)
            print(url)
            url = f.readline()
            # end=time.time()
            # if end-start>3000:
            #     continue
            # n = n - 1

        f.close()


if __name__ == '__main__':
    # CollectRequirement('java后端职位要求.txt')
    # CollectRequirement('图像算法工程师职位需求.txt')
    # CollectRequirement('互联网产品经理职位需求.txt')
    CollectRequirement('java后端职位要求test10_21.txt')
