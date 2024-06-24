import requests
from bs4 import BeautifulSoup
from collections import defaultdict
import re
import urllib.parse


class WikiParser:
    @staticmethod
    def get_words_with_links(url):
        response = requests.get(url)
        # response.raise_for_status()

        soup = BeautifulSoup(response.text, 'lxml')

        words_with_links = {}

        body_content = soup.find('div', id='bodyContent')
        if body_content:
            for a_tag in body_content.find_all('a', href=True):
                link = a_tag['href']
                if link.startswith('/wiki/'):
                    word = a_tag.get_text()
                    clean_word = re.sub(r'\W+', '', word).lower()
                    if clean_word:
                        words_with_links[clean_word] = WikiParser.get_formatted_link(link)

        return words_with_links

    @staticmethod
    def get_all_words(url):
        response = requests.get(url)
        # response.raise_for_status()

        soup = BeautifulSoup(response.text, 'lxml')

        word_count = defaultdict(int)

        body_content = soup.find('div', id='bodyContent')
        if body_content:
            text_content = ' '.join(body_content.stripped_strings)
            words = re.findall(r'\b\w+\b', text_content.lower())
            for word in words:
                word_count[word] += 1

        return dict(word_count)

    @staticmethod
    def get_formatted_link(link: str):
        start, sep, end = link.partition("/wiki")
        return "https://en.wikipedia.org" + sep + end

    @staticmethod
    def get_wiki_url_name(url):
        wiki_index = url.find("/wiki/")
        cut_link = url[wiki_index + 6:]
        formatted_string = cut_link.replace('_', ' ')
        decoded_link = urllib.parse.unquote(formatted_string)
        return decoded_link
