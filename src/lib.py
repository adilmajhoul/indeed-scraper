import json
from selectolax.parser import HTMLParser
from urllib.parse import urlencode


def jrint(*args):
    """print any data as json (for formated output)"""
    for item in args:
        print(json.dumps(item, indent=8))


def get_text(html, selector, index=0):
    parser = HTMLParser(html)
    return parser.css(selector)[index].text().strip()


def build_url(base_url, path="", query_dict={}):
    url = f"{base_url}/{path}{urlencode(query_dict)}"
    return url
