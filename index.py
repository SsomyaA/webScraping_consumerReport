from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent

# Setting-Up User-Agent
ua = UserAgent()
header = {'user-agent': ua.chrome}

review_page = requests.get('https://www.consumerreports.org/cro/a-to-z-index/products/index.htm', headers = header)

soup = BeautifulSoup(review_page.content, 'lxml')

all_divs = soup.find_all('div', attrs= {'class': "crux-body-copy"})

# for div in all_divs:
#     print(div.a.string)

products = [(div.a.string).replace('\n', '') for div in all_divs]

for product in products:
    print(product)