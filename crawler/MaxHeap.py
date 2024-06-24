import heapq


class MaxHeap:
    def __init__(self):
        self._heap = []

    def push(self, item):
        heapq.heappush(self._heap, (-item[1], item[0]))

    def pop(self):
        rate, word = heapq.heappop(self._heap)
        return word, -rate

    def peek(self):
        rate, word = self._heap[0]
        return word, -rate

    def __len__(self):
        return len(self._heap)
