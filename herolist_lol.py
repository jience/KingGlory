import requests
from bs4 import BeautifulSoup
import re
import os

url = 'http://ddragon.leagueoflegends.com/cdn/6.24.1/data/en_US/champion.json'


def get_hero_name(url):
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}
    html = requests.get(url, headers=head)
    html_json = html.json()
    hero_name = html_json['data'].keys()
    list_of_nameMax = list(hero_name)

    list_of_nameMin = []
    for ii in list_of_nameMax:
        name = ii.lower()
        list_of_nameMin.append(name)
    return list_of_nameMax


def get_onehero_img(name):
    """
    返回一个英雄的所有皮肤图片链接
    """
    url2 = 'http://gameinfo.na.leagueoflegends.com/en/game-info/champions/' + name + '/'
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}
    html = requests.get(url2, headers=head)
    contents = html.text
    soup = BeautifulSoup(contents, 'lxml')
    hero_img = soup.findAll('img')
    reg = re.compile(r'"http://ddragon.leagueoflegends.com/cdn/img/.*?.jpg"', re.S)
    hero_img_links = re.findall(reg, str(hero_img))
    return hero_img_links


def main():
    """
    下载并保存图片
    """
    list_name = list_of_name
    for i in list_name:
        os.mkdir("G:\\PycharmProjects\\Spiders\\KingGlory\\pictures_lol\\" + i)
        os.chdir("G:\\PycharmProjects\\Spiders\\KingGlory\\pictures_lol\\" + i)
        ashe = get_onehero_img(i)
        for j in ashe:
            im = re.sub('"', '', j)  # 替换j中的"为空
            ir = requests.get(im)
            if ir.status_code == 200:
                # ip = re.sub('"', '', j)
                iu = re.split('/', im)
                open(iu[-1], 'wb').write(ir.content)


if __name__ == '__main__':
    list_of_name = get_hero_name(url)
    main()
