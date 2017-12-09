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
    return list_of_nameMax

onehero_links = []
list_of_nameMax = get_hero_name(url)


def main():
    for fn in list_of_nameMax:
        os.mkdir("G:\\PycharmProjects\\Spiders\\KingGlory\\pictures_lol_1\\"+fn)
        os.chdir("G:\\PycharmProjects\\Spiders\\KingGlory\\pictures_lol_1\\"+fn)
        for v in range(20):
            onehero_links='http://ddragon.leagueoflegends.com/cdn/img/champion/splash/'+fn+'_'+str(v)+'.jpg'
            im = requests.get(onehero_links)
            if im.status_code == 200:
               iv = re.split('/', onehero_links)
               open(iv[-1], 'wb').write(im.content)


if __name__ == '__main__':
    main()
