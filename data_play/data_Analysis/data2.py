import re
import requests
def crawler(url):
    try:
        # headers ={
        #     'Connection':'close',
        # }
        r=requests.get(url)
    except requests.exceptions.RequestException as err:
        return err
    r.encoding =r.apparent_encoding
    print(r)
    pattern =re.compile('<figure class="team">\s+<a id=.*?Link1_.*?"href="/en/vnl/women/teams/.*?"><img id=.*?/></a>\s+<figcaption><a id=.*?href="/en/vnl/women/teams/.*?">(.*?)<\/a><\/figcaption>\s+</figure>\s+</td>\s+<td>(.*?)</td>\s+<td class="table-td-bold">(.*?)</td>\s+<td class="table-td-rightborder">(.*?)</td>')
    p=re.findall(pattern,r.text)
    return p

if __name__ == '__main__':
    url="http://www.volleyball.world/en/vnl/women/results-and-ranking/round1"
    result=crawler(url)
    print(result)