#first, run "pip install lxml requests" on cmd

#!/usr/bin/python
import lxml.html
import requests
page = requests.get('http://quotes.toscrape.com')
tree = lxml.html.fromstring(page.content)
authors = tree.xpath('//small[@class="author"]/text()')
print ('Authors: ',authors)