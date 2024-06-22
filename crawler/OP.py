import urllib.request
import ssl
import re


def find_links(text):
    url_regex = r'https?://\S+'
    urls = re.findall(url_regex, text)
    #remove "> from links
    cleaned_urls = [url.rstrip('">') for url in urls]
    #todo: optimisation (not include .jpg, .png and others)
    return cleaned_urls

page="https://en.wikipedia.org/wiki/Peter_Higgs"
context = ssl._create_unverified_context()
html_contents_of_page=urllib.request.urlopen(page, context=context)
html_contents_of_page=html_contents_of_page.read().decode('utf-8')
list_of_links=find_links(html_contents_of_page)
print(list_of_links)
