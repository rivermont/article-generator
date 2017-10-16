from bs4 import BeautifulSoup
import markovify
import requests

link = "https://www.washingtonpost.com/news/acts-of-faith/wp/2017/10/13/trump-violates-core-conservative-" \
       "values-yet-most-conservatives-still-refuse-to-condemn-him"
# Possibly something like:
# https://www.reddit.com/r/politics/search.rss?q=subreddit%3Apolitics+site%3Awashingtonpost.com&sort=new&t=day

page = requests.get(link).text

# with open('test.html') as file:
#     soup = BeautifulSoup(file, 'lxml')

soup = BeautifulSoup(page, 'lxml')

content = ''''''

# for x in soup.find_all('article', {'class': 'paywall'}):
#     for y in x.find_all('p'):
#         content += y.text
for x in soup.find_all('p'):
    content += x.text

model = markovify.Text(content, retain_original=False)

with open('markov1_nl.html', 'w+') as f:
    for i in range(100):
        f.write(model.make_sentence(tries=100) + '<br>')
