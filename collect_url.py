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

dicts = {'beijing': '010', 'shanghai': '020', 'shenzhen': '050090'
    , 'guangzhou': '050020', 'hangzhou': '070020'}


class collect():
    def __init__(self, job):
        urls = []
        data = []
        for code in dicts.values():
            url = ["https://www.liepin.com/zhaopin/?key=" + job + "&dqs=" + code + "&curPage={}"
                .format(i) for i in range(0, 10)]
            urls = urls + url
        # 发起访问请求
        # print(len(urls)) 结果测试为50-->正常
        for url in urls:
            page = requests.get(url=url, headers={"User-Agent": random.choice(user_Agent)})
            time.sleep(1)
            soup = BeautifulSoup(page.text, "html.parser")
            soup = soup.find_all("h3")
            for i in soup:
                if i.has_attr("title"):
                    href = i.find_all("a")[0]["href"]
                    if re.match('http', href):
                        data.append(href)
                        print(href)

        # print(len(data))测试结果为1351条，结果正常
        f = open(job + ".txt", 'w')
        for i in data:
            f.write(i)
            f.write('\n')
        f.close()


if __name__ == '__main__':
    # job_1 = collect('数据挖掘test10_21')
    # job_2 = collect('图像算法工程师')
    job_3 = collect('java后端test10_21')
    # job_4 = collect('互联网产品经理')
