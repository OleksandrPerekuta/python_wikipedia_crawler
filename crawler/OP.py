import urllib.request
import ssl
import re
from bs4 import BeautifulSoup
from collections import defaultdict


class Parser:
    @staticmethod
    def get_words_with_links(url):
        context = ssl._create_unverified_context()
        html_contents_of_page = urllib.request.urlopen(url, context=context).read().decode('utf-8')
        soup = BeautifulSoup(html_contents_of_page, 'html.parser')

        words_with_links = {}

        body_content = soup.find('div', id='bodyContent')
        if body_content:
            for a_tag in body_content.find_all('a', href=True):
                link = a_tag['href']
                if link.startswith('/wiki/'):
                    word = a_tag.get_text()
                    clean_word = re.sub(r'\W+', '', word).lower()
                    if clean_word:
                        words_with_links[clean_word] = link

        return words_with_links

    @staticmethod
    def get_all_words(url):
        context = ssl._create_unverified_context()
        html_contents_of_page = urllib.request.urlopen(url, context=context).read().decode('utf-8')
        soup = BeautifulSoup(html_contents_of_page, 'html.parser')

        word_count = defaultdict(int)

        body_content = soup.find('div', id='bodyContent')
        if body_content:
            for text in body_content.stripped_strings:
                words = re.findall(r'\b\w+\b', text.lower())
                for word in words:
                    word_count[word] += 1

        return dict(word_count)


url = "https://en.wikipedia.org/wiki/Peter_Higgs"
words_with_links = Parser.get_words_with_links(url)
all_words = Parser.get_all_words(url)

print("Words with Links:", words_with_links)
# мапа слова и количества появлений
print("All Words:", all_words)
