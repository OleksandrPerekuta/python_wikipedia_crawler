import requests
from bs4 import BeautifulSoup
from collections import defaultdict
import re
import urllib.parse


class WikiParser:
    @staticmethod
    def get_words_with_links(url: str):
        """
        Retrieve words and their corresponding Wikipedia links from the specified URL.

        Parameters:
        url (str) -- The URL of the Wikipedia page to parse.

        Returns:
        dict -- A dictionary where keys are cleaned words and values are the full Wikipedia links.
        """
        response = requests.get(url)

        soup = BeautifulSoup(response.text, 'lxml')

        words_with_links = {}

        body_content = soup.find('div', id='bodyContent')
        if body_content:
            for a_tag in body_content.find_all('a', href=True):
                link = a_tag['href']
                if link.startswith('/wiki/'):
                    word = a_tag.get_text()
                    clean_word = re.sub(r'\W+', '', word).lower()

                    if clean_word and re.match(r'^/wiki/\w+:.*', link) is None:
                        words_with_links[clean_word] = WikiParser.get_formatted_link(link)

        return words_with_links

    @staticmethod
    def get_all_words(url: str):
        """
        Retrieve all words and their frequencies from the specified Wikipedia page.

        Parameters:
        url (str) -- The URL of the Wikipedia page to parse.

        Returns:
        dict -- A dictionary where keys are words and values are their respective frequencies.
        """
        response = requests.get(url)

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
        """
        Retrieve all words and their frequencies from the specified Wikipedia page.

        Parameters:
        url (str) -- The URL of the Wikipedia page to parse.

        Returns:
        dict -- A dictionary where keys are words and values are their respective frequencies.
        """
        start, sep, end = link.partition('/wiki')
        return 'https://en.wikipedia.org' + sep + end

    @staticmethod
    def get_wiki_url_name(url: str):
        """
        Extract and decode the Wikipedia article name from the URL.

        Parameters:
        url (str) -- The full URL of the Wikipedia page.

        Returns:
        str -- The decoded Wikipedia article name.
        """
        wiki_index = url.find('/wiki/')
        cut_link = url[wiki_index + 6:]
        formatted_string = cut_link.replace('_', ' ')
        decoded_link = urllib.parse.unquote(formatted_string)
        return decoded_link
