import requests
import time
from lxml import html
from bs4 import BeautifulSoup
from selectolax.parser import HTMLParser
import matplotlib.pyplot as plt
from urllib.parse import urlencode


html_content = '''
<a
  href="https://www.bezorgdekrant.nl/en/jobs/depot-holder-in-enkhuizen"
  class="vacancy-card icon-chevron-right"
  data-id="274476"
  data-category="Depot Holder"
  data-lat="52.7153849"
  data-long="5.2846831"
>
  <h4>
    <svg
      class="fill-current mt-0 mr-3"
      xmlns="http://www.w3.org/2000/svg"
      xmlns:xlink="http://www.w3.org/1999/xlink"
      width="18px"
      height="18px"
      viewBox="0 0 18 18"
    >
      <!-- Generator: Sketch 63 (92445) - https://sketch.com -->
      <title>Icons/Interface/castle</title>
      <desc>Created with Sketch.</desc>
      <g
        id="wlnwzvawot-Icons/Interface/castle"
        stroke="none"
        stroke-width="1"
        fill="none"
        fill-rule="evenodd"
      >
        <path
          d="M16.6543833,16.6790798 L12.1242812,16.6790798 L12.1242812,14.5992007 C12.1242812,12.9081325 10.7237413,11.5322603 9,11.5322603 C7.27731487,11.5322603 5.87571881,12.9081325 5.87571881,14.5992007 L5.87571881,16.6790798 L1.34667293,16.6790798 L1.34667293,7.37664939 L16.6543833,7.37664939 L16.6543833,16.6790798 Z M17.3271916,6.05572916 L12.9808708,6.05572916 L12.9808708,4.25372025 L15.8305363,3.17645485 C16.0713531,3.08521389 16.2371787,2.86644296 16.2593592,2.61449349 C16.2804835,2.36254403 16.1526816,2.1188892 15.9298204,1.9903224 L12.6502758,0.0918883772 C12.4422016,-0.0283837944 12.1844854,-0.0304574526 11.9742988,0.0867042318 C11.7651684,0.204902745 11.6352541,0.423673678 11.6352541,0.661107534 L11.6352541,6.05572916 L4.40124399,6.05572916 L4.40124399,4.24749927 L6.94038258,3.16608656 C7.16746861,3.06862462 7.32273207,2.85814832 7.34280014,2.61656715 C7.36498064,2.37394915 7.24879709,2.14169944 7.04283535,2.00794849 L4.09811055,0.108477642 C3.89109259,-0.0242364782 3.62703908,-0.036678427 3.40945898,0.0794464284 C3.19187889,0.194534455 3.05668349,0.418489533 3.05668349,0.661107534 L3.05668349,6.05572916 L0.672808356,6.05572916 C0.301021007,6.05572916 -5.68434189e-14,6.35122545 -5.68434189e-14,6.71618928 L-5.68434189e-14,17.3395399 C-5.68434189e-14,17.7034669 0.301021007,18 0.672808356,18 L6.54852717,18 C6.92031452,18 7.22133552,17.7034669 7.22133552,17.3395399 L7.22133552,14.5992007 C7.22133552,13.6370233 8.01983335,12.8531805 9,12.8531805 C9.98016665,12.8531805 10.7786645,13.6370233 10.7786645,14.5992007 L10.7786645,17.3395399 C10.7786645,17.7034669 11.0796855,18 11.4514728,18 L17.3271916,18 C17.698979,18 18,17.7034669 18,17.3395399 L18,6.71618928 C18,6.35122545 17.698979,6.05572916 17.3271916,6.05572916 L17.3271916,6.05572916 Z"
          id="wlnwzvawot-Fill-223"
          fill="#00263A"
        ></path>
      </g>
    </svg>

    Depot Holder in Enkhuizen
  </h4>
  <ul class="vacancy-card__usps">
    <li><strong>Available from:</strong> 26.03.2024</li>
    <li><strong>Earnings:</strong> €20 per hour</li>
  </ul>
  <ul class="vacancy-card__specs">
    <li class="vacancy-card__distance hidden">
      <i class="icon-location"></i>1.5km
    </li>
    <li class="">
      <i class="icon-flag"></i><span class="job-city">Enkhuizen</span>
    </li>
    <li><i class="icon-person"></i>18+</li>
  </ul>
</a>

<a
  href="https://www.bezorgdekrant.nl/en/jobs/bezorger-in-ekehaar-2"
  class="vacancy-card icon-chevron-right"
  data-id="243380"
  data-category="Deliverer"
  data-lat="52.9530557"
  data-long="6.6027332"
>
  <h4>
    <svg
      class="fill-current mt-0 mr-3"
      xmlns="http://www.w3.org/2000/svg"
      xmlns:xlink="http://www.w3.org/1999/xlink"
      width="18px"
      height="13px"
      viewBox="0 0 18 13"
    >
      <!-- Generator: Sketch 63 (92445) - https://sketch.com -->
      <title>Fill 102</title>
      <desc>Created with Sketch.</desc>
      <g
        id="cscsajgtku-Symbols"
        stroke="none"
        stroke-width="1"
        fill="none"
        fill-rule="evenodd"
      >
        <g
          id="cscsajgtku-Icons/Transport/bike"
          transform="translate(0.000000, -3.000000)"
          fill="#00263A"
        >
          <path
            d="M14.2576055,14.721 C12.8661534,14.721 11.734643,13.536 11.734643,12.079 C11.734643,10.623 12.8661534,9.437 14.2576055,9.437 C15.6500133,9.437 16.7824794,10.623 16.7824794,12.079 C16.7824794,13.536 15.6500133,14.721 14.2576055,14.721 Z M10.5706398,11.442 L8.08399257,11.442 L6.98210778,8.615 L12.5192461,8.615 C11.5024157,9.177 10.7636846,10.214 10.5706398,11.442 Z M3.74239448,14.721 C2.34998673,14.721 1.21847624,13.536 1.21847624,12.079 C1.21847624,10.623 2.34998673,9.437 3.74239448,9.437 C5.13480223,9.437 6.26726838,10.623 6.26726838,12.079 C6.26726838,13.536 5.13480223,14.721 3.74239448,14.721 Z M14.6341386,8.184 L12.1704274,3.338 C12.0643483,3.131 11.8579241,3 11.6323865,3 L9.72965224,3 C9.39325723,3 9.12089196,3.286 9.12089196,3.638 C9.12089196,3.99 9.39325723,4.275 9.72965224,4.275 L11.2663658,4.275 L12.8260154,7.341 L6.48516061,7.341 L5.53713831,4.91 C5.44443855,4.67 5.22081232,4.514 4.9732944,4.514 L3.29992036,4.514 C2.96256968,4.514 2.69020441,4.799 2.69020441,5.151 C2.69020441,5.502 2.96256968,5.788 3.29992036,5.788 L4.56426865,5.788 L5.72540483,8.764 C5.14913724,8.386 4.47156889,8.164 3.74239448,8.164 C1.67910804,8.164 0,9.92 0,12.079 C0,14.238 1.67910804,15.995 3.74239448,15.995 C5.59830104,15.995 7.13883727,14.573 7.43127157,12.716 L7.67209981,12.716 C7.67305548,12.716 7.67401115,12.716 7.67592248,12.716 C7.67687815,12.716 7.67783382,12.716 7.67878949,12.716 L10.5706398,12.716 C10.8630741,14.573 12.4026546,15.995 14.2576055,15.995 C16.320892,15.995 18,14.238 18,12.079 C18,10.053 16.5215822,8.381 14.6341386,8.184 L14.6341386,8.184 Z"
            id="cscsajgtku-Fill-102"
          ></path>
        </g>
      </g>
    </svg>

    DELIVERER IN EKEHAAR
  </h4>
  <ul class="vacancy-card__usps">
    <li><strong>Earnings:</strong> €&nbsp;14,34 per one-hour shift</li>
    <li><strong>+ Bonus:</strong> €1000,- start-up bonus!*</li>
  </ul>
  <ul class="vacancy-card__specs">
    <li class="vacancy-card__distance hidden">
      <i class="icon-location"></i>1.5km
    </li>
    <li class="">
      <i class="icon-flag"></i><span class="job-city">Ekehaar</span>
    </li>
    <li><i class="icon-person"></i>15+</li>
  </ul>
</a>
'''
# soup = BeautifulSoup(html_content,'lxml')
# texts = [el.contents[2].get_text().strip() for el in soup.select('a.vacancy-card > h4')]


parser = HTMLParser(html_content)

def get_text(html,selector,index=0):
  parser = HTMLParser(html)
  return parser.css(selector)[index].text(deep=False).strip()

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


def build_url(base_url, path, query_dict):
def build_url(base_url,path='',query_dict={}):
  mydict = {'search_query': 'as7ab lkahf'}
  return f"{base_url}{path}{urlencode(query_dict)}"

# https://www.youtube.com/results?/search_query=as7ab+lkahf
# https://www.youtube.com/results?search_query=as7ab+lkahf


print(build_url('https://www.youtube.com/results','search_query',{'search_query':'as7ab lkahf'}))