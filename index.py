from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent
from xlsxwriter import Workbook
import xlrd

# Setting-Up User-Agent
ua = UserAgent()
header = {'user-agent': ua.chrome}

# Setting up excel file
Wb = Workbook('scrap_file.xlsx')
Sh  = Wb.add_worksheet()



review_page = requests.get('https://www.consumerreports.org/cro/a-to-z-index/products/index.htm', headers = header)

soup = BeautifulSoup(review_page.content, 'lxml')

all_divs = soup.find_all('div', attrs= {'class': "crux-body-copy"})

# for div in all_divs:
#     print(div.a.string)

products = [(div.a.string).replace('\n', '') for div in all_divs]

# for product in products:
#     print(product)

all_links = soup.find_all('div', attrs= {'class': "crux-body-copy"})

links = ["https://www.consumerreports.org"+(link.a['href']) for link in all_links]


details = zip(products, links)
#
# for key, val in details:
#     print(key, val)

# Wb = xlrd.open_workbook('scrap_file.xlsx')


r = 0
Sh.write(r, 0, 'Product Name')
Sh.write(r, 1, 'Link')
for prod, lin in details:
    Sh.write(r+1, 0, prod)
    Sh.write(r+1, 1, lin)
    r = r +1

Wb.close()