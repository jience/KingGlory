import requests
import re
import os

"""
爬取王者荣耀英雄图片
"""

url = 'http://pvp.qq.com/web201605/js/herolist.json'
head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}
# html = requests.get(url, headers=head)
html = requests.get(url)
html_json = html.json()


hero_name = list(map(lambda x: x['cname'], html_json))
hero_number = list(map(lambda x: x['ename'], html_json))


def main():
    """
    下载并保存图片
    """
    ii = 0
    for v in hero_number:
        os.mkdir("G:\\PycharmProjects\\Spiders\\KingGlory\\pictures\\" + hero_name[ii])
        os.chdir("G:\\PycharmProjects\\Spiders\\KingGlory\\pictures\\" + hero_name[ii])

        ii += 1
        for u in range(12):
            onehero_link = 'http://game.gtimg.cn/images/yxzj/img201606/' \
                           'skin/hero-info/'+str(v)+'/'+str(v)+'-bigskin-'+str(u)+'.jpg'
            im = requests.get(onehero_link)
            if im.status_code == 200:
                iv = re.split('-', onehero_link)
                open(iv[-1], 'wb').write(im.content)


if __name__ == '__main__':
    main()
