import math

from crawler.WikiParser import *
from crawler.MaxHeap import MaxHeap


class CrawlerBase:
    """
    A base class for crawling wiki pages to find path from source to target link.
    """

    def __init__(self):
        """
        Initialize the CrawlerBase with default attributes.
        """
        self.__endpoint_data = None
        self.__start_page = None
        self.__end_page = None
        self.__endpoint_data = None
        self.__visited_links = None
        self.most_frequent_word = None

    def crawl(self, start_link: str, endpoint_link: str, pages_depth: int, add_node: callable = None):
        """
        Start crawling from the start_link to the endpoint_link up to a certain depth.

        Parameters:
        start_link (str) -- The starting URL for the crawl.
        endpoint_link (str) -- The target URL to reach.
        pages_depth (int) -- The depth of pages to crawl.
        add_node (callable) -- An optional function to add a node in the crawl ui (default is None).

        Returns:
        list -- Traveled path (a list of visited links).
        """
        self.__start_page = str(start_link)
        self.__end_page = str(endpoint_link)
        self.__endpoint_data = WikiParser.get_all_words(endpoint_link)
        self.__visited_links = [start_link]
        self.most_frequent_word = max(self.__endpoint_data.values())

        next_page = 'Start', start_link
        print('Source: ', start_link)
        print('Target: ', endpoint_link)
        print('--------------------------------------------------------------')
        print('\tStart: ', next_page[1])
        if add_node:
            add_node(next_page, to_paint=False)

        for _ in range(1, pages_depth + 1):
            next_page = self.__get_next(next_page[1])
            if add_node:
                add_node(next_page)
            print('\t\t--', next_page)
            if self.__end_page == next_page[1]:
                print('--------------------------------------------------------------')
                return self.__visited_links

        print('--------------------------------------------------------------')
        return []

    def __get_next(self, page_link: str):
        """
        Retrieve the next page to visit based on the links found on the current page.

        Parameters:
        page_link (str) -- The URL of the current page.

        Returns:
        tuple -- A tuple containing the word and the URL of the next page.
        """
        links_map = WikiParser.get_words_with_links(page_link)

        if len(links_map) == 0:
            for _ in range(0, 3):
                links_map = WikiParser.get_words_with_links(page_link)
                if len(links_map) != 0:
                    break

        if len(links_map) == 0:
            raise Exception('Something went wrong')

        max_heap = MaxHeap()
        for key, value in links_map.items():
            if self.__end_page == value:
                self.__visited_links.append(value)
                return key, value

            max_heap.push((key, self.__similarity_rate(key)))

        first_word = max_heap.peek()[0]
        for _ in range(0, len(max_heap)):
            max_word = max_heap.pop()[0]
            if links_map[max_word] not in self.__visited_links:
                self.__visited_links.append(links_map[max_word])
                return max_word, links_map[max_word]

        return first_word, links_map[first_word]

    @staticmethod
    def __sigmoid_normalize(x: float):
        """
        Normalize a value using the sigmoid function.

        Parameters:
        x (float) -- The value to normalize.

        Returns:
        float -- The normalized value.
        """
        return 1 / (1 + math.exp(-x))

    def __similarity_rate(self, word_to_compare: str):
        """
        Calculate the similarity rate between a given word and the target page.

        Parameters:
        word_to_compare (str) -- The word to compare against the target page.

        Returns:
        float -- The calculated similarity rate.
        """
        result_map = {}
        alpha = 1
        for word in self.__endpoint_data:
            set_a = set(word_to_compare)
            set_b = set(word)
            intersection = set_a.intersection(set_b)
            union = set_a.union(set_b)
            result_map[word] = len(intersection) / len(union) * self.__endpoint_data[word]
            if word in word_to_compare or word_to_compare in word:
                alpha += math.log10(result_map[word] if result_map[word] > 0 else 1)

            result_map[word] = self.__sigmoid_normalize(result_map[word])

        return sum(result_map.values()) * alpha / len(result_map) * 100
