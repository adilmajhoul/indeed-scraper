
from urllib import request
import requests
import time
from lxml import html
from bs4 import BeautifulSoup
from selectolax.parser import HTMLParser
import matplotlib.pyplot as plt
from urllib.parse import urlencode
from myhtml import html_content

# soup = BeautifulSoup(html_content,'lxml')
# texts = [el.contents[2].get_text().strip() for el in soup.select('a.vacancy-card > h4')]



def get_text(html,selector,index=0):
  parser = HTMLParser(html)
  return parser.css(selector)[index].text().strip()

# def build_url(base_url, path, query_dict):
#     # Returns a list in the structure of urlparse.ParseResult
#     url_parts = list(urllib.parse.urlparse(base_url))
#     url_parts[2] = path
#     url_parts[4] = urllib.parse.urlencode(args_dict)
#     return urllib.parse.urlunparse(url_parts)

# titles=[]
# for node in parser.css('a'):
  # titles.append(get_text(node.html,"h4")) 
# 
# print(titles)




def build_url(base_url,path='',query_dict={}):
  url = f"{base_url}/{path}{urlencode(query_dict)}"
  return url

# https://www.youtube.com/results?/search_query=as7ab+lkahf
# https://www.youtube.com/results?search_query=as7ab+lkahf


# url = 'https://www.indeed.co.in/jobs?q=' + skill + \
  
#   '&l=' + place + '&start=' + str(page * 10)
            

# search_query = input('Enter Your Search Query: ').strip()
# location = input('Enter Your location: ').strip()
# pages = int(input('Enter Pages To Scrape: ').strip())


# url = build_url('https://ma.indeed.com','jobs?',{'q': search_query,'l':location,'sort':'date','start':str(pages * 10) - 10 if pages > 1 else ''})
# pages = 1
# url = build_url('https://ma.indeed.com','jobs?',{'q': 'backend developer','l':'rabat','sort':'date','start':str(pages * 10) - 10 if pages > 1 else ''})
# print('url: ', url)


# headers = {
    # "User-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"}



header={"User-Agent": "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"}

# r = requests.get('http://httpbin.org/headers', headers=header)
# headers = r.json()['headers']
# 
# url = 'https://ma.indeed.com/jobs?q=backend%20developer&l=rabat&from=searchOnHP'
# response = requests.get(url, headers=header)
# html = response.text
# print('html: ', html)

# res= requests.get(url, headers=headers)
# html_content = res.text
# print('html_content: ', html_content)


# parser = HTMLParser(html_content)
titles = []

pages = 3
for page in range(pages):
    print('page: ', page)
    
    
    url = f'https://ma.indeed.com/jobs?q=developer&l=rabat&start={str(page * 10)}'
    print('url: ', url)
    html = requests.get(url, headers=header).text
    parser = HTMLParser(html)

    for node in parser.css('ul.css-zu9cdh > li'):
        if len(node.css("h2.jobTitle > a")) >= 1:
            titles.append(get_text(node.html,"h2.jobTitle > a")) 
        

    
print('titles: ', titles)
print('titles length: ', len(titles))
# print('nodes: ', parser.css('ul.css-zu9cdh > li'))


  
# nodes = parser.css("h2.jobTitle > a")
# print('nodes: ', nodes)



# job = {
#   "tite":'',
#   "company":'',
#   "location":'',
#   'date':''
#   }


# for page in range(10):
#   url = build_url('https://ma.indeed.com','jobs?',{'q': 'développeur','l':'Rabat','sort':'date','start':str(page * 10) if page > 1 else ''})
#   print('url: ', url)

