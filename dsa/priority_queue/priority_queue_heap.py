import unittest

class Heap:
    def __init__(self):
        self._data = []

    def _parent(self, i):
        return (i - 1) // 2

    def _left(self, i):
        return (2 * i) + 1

    def _right(self, i):
        return (2 * i) + 2

    def _has_right(self, i):
        return self._right(i) < len(self._data)

    def _has_left(self, i):
        return self._left(i) < len(self._data)

    def _swap(self, i, j):
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _upheapify(self, i):
        parent = self._parent(i)
        if i > 0 and self._data[i] < self._data[parent]:
            self._swap(i, parent)
            self._upheapify(parent)

    def _downheapify(self, i):
        if self._has_left(i):
            left = self._left(i)
            small_child = left
            if self._has_right(i):
                right = self._right(i)
                if self._data[left] > self._data[right]:
                    small_child = right
            if self._data[i] > self._data[small_child]:
                self._swap(small_child, i)
                self._downheapify(small_child)

    def __len__(self):
        return len(self._data)

    def add(self, v):
        self._data.append(v)
        self._upheapify(len(self._data) - 1)

    def is_empty(self):
        return len(self._data) == 0

    def min(self):
        if self.is_empty():
            raise Empty('Heap is empty')
        return self._data[0]

    def pop(self):
        if self.is_empty():
            raise Empty('Heap is empty')

        self._swap(0, len(self._data) - 1)
        result = self._data.pop()
        self._downheapify(0)
        return result


    def print_heap(self):
        print([(self._parent(i), val) for i, val in enumerate(self._data) ])

class Test(unittest.TestCase):

    def test_ideal_case(self):
        h = Heap()
        h.add(5)
        h.add(2)
        h.add(8)
        h.add(9)
        h.print_heap()
        self.assertEqual(h.min(), 2)
        self.assertEqual(h.pop(), 2)
        h.print_heap()
        self.assertEqual(h.pop(), 5)

unittest.main(verbosity=2)
