from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import requests


ua = UserAgent()
header = {'user-agent': ua.chrome}


print(ua.chrome)

myPage= requests.get('http://www.google.com', headers= header)


soup = BeautifulSoup(myPage.content, 'lxml')
print(soup)