#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import with_statement
import codecs
from bs4 import BeautifulSoup
from urllib2 import urlopen
from time import sleep
 
BASE_URL = "http://www.imdb.com"
 
def get_title_links(section_url):
    html = urlopen(section_url).read()
    soup = BeautifulSoup(html, "lxml")
    items = soup.find("div", "list detail")
    title_links = [BASE_URL + b.a["href"] for b in items.findAll("b")]
    return title_links
 
def get_title(title_url):
    html = urlopen(title_url).read()
    soup = BeautifulSoup(html, "lxml")
    title = soup.find("span", "itemprop").string
    return {"Title": title,
            "Profile URL": title_url}
 
if __name__ == '__main__':
    top = ("http://www.imdb.com/best-of/2014/top-movies-of-2014?ref_=bo14_bolist_t7")
 
    links = get_title_links(top)
 
    data = []
    for link in links:
        title = get_title(link)
        data.append(title)
        sleep(1)
    print(data)   
    #with open("out.txt", "w") as stream:
    #    stream.write(data)
