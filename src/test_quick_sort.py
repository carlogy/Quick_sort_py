import unittest

from quick_sort import (
    quick_sort,
    partition
)

class TestQuickSort(unittest.TestCase):
    def test_reverse_sorted_list(self):
            array = list(range(100, 0, -1))
            sorted_array = sorted(array)
            quick_sort(array, 0, len(array) - 1)
            self.assertEqual(sorted_array,array)

    def test_sorted_list(self):
        array = list(range(0,100))
        quick_sort(array, 0, len(array) - 1)
        self.assertEqual(
            array,
            list(range(0, 100))
        )

    def test_empty_list(self):
        array = []
        quick_sort(array, 0 , 0)
        self.assertEqual(array, [])
