#first, run "pip install lxml requests" on cmd

#!/usr/bin/python
import lxml.html
import requests
page = requests.get('http://quotes.toscrape.com')
tree = lxml.html.fromstring(page.content)
authors = tree.xpath('//small[@class="author"]/text()') #THIS IS THE IMPORTANT LINE
        #small indicates the <tag> you want to target
        #class="author" indicates that you want to add a condition of the tag having a certain class; if you just want a tag, delete the [] brackets and everything in them
        #/text() indicates that what you want is the text that comes after each of the matching tags
print ('Authors: ',authors)
