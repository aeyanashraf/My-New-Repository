from urllib.request import urlopen
from bs4 import BeautifulSoup

url = input('Enter - ')
count=int(input('Enter count'))
position=int(input('Enter position'))

for x in range(count):
    html = urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")
    tags=soup('a')
    pil=list()
    kil=list()
    for t in tags:
        a = t.get('href', None)
        pil.append(a)
        y = t.text
        kil.append(y)


    print(pil[position-1])
    print(kil[position-1])
    url=pil[position-1]
