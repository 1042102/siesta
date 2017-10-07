# encoding=utf-8

import urllib.request
from bs4 import BeautifulSoup

start_num = 1
finish_num = 10

# Define Naver Webtoon URL
resource_url_str = 'http://{Define Naver Webtoon URL}'

for no in range(start_num, finish_num):
    resource_url = resource_url_str.format(no)

    page_html = urllib.request.urlopen(resource_url)
    soup = BeautifulSoup(page_html, 'html.parser')

    for comic_image in soup.find_all('img'):
        if comic_image.get('alt') == 'comic content':
            comic_image_url = comic_image.get('src')
            current_file_name = 'D:\\webtoon\\{}_{}_{}'.format(comic_image.get('src').rsplit('/', 3)[1],
                                                               comic_image.get('src').rsplit('/', 2)[1].zfill(4),
                                                               comic_image.get('src').rsplit('/', 1)[1])

            req = urllib.request.Request(comic_image_url)
            req.add_header('Referer', resource_url)

            res = urllib.request.urlopen(req)

            output = open(current_file_name, 'wb')
            output.write(res.read())
            output.close()
