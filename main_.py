import requests
import time
from bs4 import BeautifulSoup
from selectolax.parser import HTMLParser

# import matplotlib.pyplot as plt

url = "https://www.bezorgdekrant.nl/en/all-jobs"
response = requests.get(url)
content = response.text
# print('content: ')
# print(content)


# BeautifulSoup
start_time_bs = time.time()

soup = BeautifulSoup(content, "lxml")
job_titles_bs = [
    el.contents[2].get_text().strip() for el in soup.select("a.vacancy-card > h4")
]
print("🚀 length:", len(job_titles_bs))

end_time_bs = time.time()
bs_time = end_time_bs - start_time_bs
# ---------------------------
# Selectolax
start_time_selectolax = time.time()
parser = HTMLParser(content)

job_titles_selectolax = [
    node.text().strip() for node in parser.css("#jobList > a:nth-child(1) > h4")
]


job_titles_selectolax = [
    el.text().strip() for el in parser.css("a.vacancy-card > h4:nth-of-type(2)")
]
print("🚀 length:", len(job_titles_selectolax))

end_time_selectolax = time.time()


selectolax_time = end_time_selectolax - start_time_selectolax

h4_elements = parser.css("h4")

# Extract text content from each <h4> element
h4_texts = [element.text().strip() for element in h4_elements]

# Print the extracted texts
for text in h4_texts:
    print(text)

#
# lxml
# start_time_lxml = time.time()
# tree = html.fromstring(content)
# job_titles_lxml = tree.xpath('//h3[@class="card-title"]/text()')
# end_time_lxml = time.time()
# lxml_time = end_time_lxml - start_time_lxml
#
# Results
print("BeautifulSoup results:")
print(job_titles_bs)
print(f"Time taken: {bs_time} seconds\n")

# print("Selectolax results:")
# print(job_titles_selectolax)
# print(f"Time taken: {selectolax_time} seconds\n")

# print("lxml results:")
# print(job_titles_lxml)
# print(f"Time taken: {lxml_time} seconds\n")


# Performance comparison
# print(f"Selectolax is {lxml_time / selectolax_time:.2f} times faster than lxml")
# print(f"Selectolax is {bs_time / selectolax_time:.2f} times faster than BeautifulSoup")

# Bar graph
# libraries = ['lxml', 'BeautifulSoup', 'Selectolax']
# times = [lxml_time, bs_time, selectolax_time]

# plt.bar(libraries, times, color=['blue', 'green', 'red'])
# plt.xlabel('Library')
# plt.ylabel('Time (seconds)')
# plt.title('Web Scraping Performance Comparison')
# plt.show()
