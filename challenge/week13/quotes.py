import urllib.request as ur
from bs4 import BeautifulSoup as bs
import operator

# 웹페이지에서 text 가져오기. 
url = 'https://quotes.toscrape.com/'
html = ur.urlopen(url)
soup = bs(html.read(),'html.parser')
quotes = soup.find_all('div',{"class":"quote"})

lines = ""
for quote in quotes:
    quote = quote.find_all('span',{"class":"text"})
    for i in quote:
        lines+=i.text

tokens = [] 
lines = lines.replace("“","").split("”")
for line in lines:
    tokens.extend(line.split(" "))

# 단어별 빈도수 저장. 
tokens_freq ={}
for token in tokens:
    if token in tokens_freq: # 이미 나왔던 단어일 때 +1
        tokens_freq[token] += 1 
    else: # 없는 단어일 때 추가. 
        tokens_freq[token] = tokens.count(token)

# 많이 나온 빈도수별로 정렬 
sorted_freq = sorted(tokens_freq.items(),key=operator.itemgetter(1),reverse = True)

for i in range(5):
    print(i+1,*sorted_freq[i])