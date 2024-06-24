import math

from WikiParser import *
from crawler.MaxHeap import MaxHeap


class CrawlerBase:
    def __init__(self):
        self.__endpoint_data = None
        self.__start_page = None
        self.__end_page = None
        self.__endpoint_data = None
        self.__visited_links = None

    def crawl(self, start_link: str, endpoint_link: str, pages_depth: int, add_node: callable = None):
        self.__start_page = str(start_link)
        self.__end_page = str(endpoint_link)
        self.__endpoint_data = WikiParser.get_all_words(endpoint_link)
        self.__visited_links = [start_link]

        next_page = "Start", start_link
        print("Start: ", next_page[1])
        if add_node:
            add_node(next_page, to_paint=False)

        for _ in range(1, pages_depth + 1):
            next_page = self.__get_next(next_page[1])
            if add_node:
                add_node(next_page)
            print("\t--", next_page)
            if self.__end_page == next_page[1]:
                return self.__visited_links

        return []

    def __get_next(self, page_link: str):
        links_map = WikiParser.get_words_with_links(page_link)

        if len(links_map) == 0:
            for _ in range(0, 3):
                links_map = WikiParser.get_words_with_links(page_link)
                if len(links_map) != 0:
                    break

        if len(links_map) == 0:
            raise Exception("Something went wrong")

        max_heap = MaxHeap()
        for key, value in links_map.items():
            if self.__end_page in value:
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
    def __sigmoid_normalize(x):
        return 1 / (1 + math.exp(-x))

    def __similarity_rate(self, word_to_compare: str):
        result_map = {}
        for word in self.__endpoint_data:
            set_a = set(word_to_compare)
            set_b = set(word)
            intersection = set_a.intersection(set_b)
            union = set_a.union(set_b)
            result_map[word] = len(intersection) / len(union) * self.__endpoint_data[word]
            if word_to_compare in word or word in word_to_compare:
                result_map[word] = result_map[word] * math.sqrt(result_map[word])

            result_map[word] = self.__sigmoid_normalize(result_map[word])

        return sum(result_map.values()) / len(result_map) * 100
