html = requests.get(url, headers=get_header()).text
parser = HTMLParser(html)

print("next button ->", parser.css('a[aria-label="Next Page"]'))