import heapq


class MaxHeap:
    """
    A MaxHeap implementation using Python's heapq library, which by default is a min-heap.
    This class inverts the values to simulate a max-heap.
    """

    def __init__(self):
        """Initialize an empty MaxHeap."""
        self._heap = []

    def push(self, item):
        """Add an item to the heap.

        The item is a tuple where the first element is a word and the second element is a rate.
        The rate is negated to maintain max-heap property.

        Parameters:
        item -- a tuple containing a word and a rate
        """
        heapq.heappush(self._heap, (-item[1], item[0]))

    def pop(self):
        """Remove and return the item with the highest rate from the heap.

        Returns a tuple containing the word and the original rate.

        Returns:
        tuple -- a tuple containing the word and the original rate
        """
        rate, word = heapq.heappop(self._heap)
        return word, -rate

    def peek(self):
        """Return the item with the highest rate without removing it from the heap.

        Returns a tuple containing the word and the original rate.

        Returns:
        tuple -- a tuple containing the word and the original rate
        """
        rate, word = self._heap[0]
        return word, -rate

    def __len__(self):
        """Return the number of items in the heap.

        Returns:
        int -- the number of items in the heap
        """
        return len(self._heap)