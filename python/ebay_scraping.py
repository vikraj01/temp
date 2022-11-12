import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=telescope&_sacat=0'
page = requests.get(url)
soup = BeautifulSoup(page.text,'lxml')

posts = soup.find_all('li',class_ = 's-item s-item__pl-on-bottom s-item--watch-at-corner')

df = pd.DataFrame({'title':[''], 'imageUrl':[''],'description':[''],'price':['']})

for post in posts:
    name = post.find('h3',class_='s-item__title').text
    image = post.find('img',class_='s-item__image-img').get('src')
    price = post.find('span',class_='s-item__price').text
    description = post.find('span',class_='SECONDARY_INFO').text

    df2 = pd.DataFrame({'title':[name], 'imageUrl':[image],'description':[description],'price':[price]})
    df = pd.concat([df,df2],ignore_index=True,axis=0)

df.to_csv('D:\Web_Developement_Base\Python_web_scraping\Practise_Beautiful_soup/project_ebay_telescope.csv')
df.to_json('D:\Web_Developement_Base\Python_web_scraping\Practise_Beautiful_soup/project_ebay_telescope.json')
#df.to_json('D:\Web_Developement_Base\nodeJS\\5_ExpressJS\python/ebay_telescope.json')
