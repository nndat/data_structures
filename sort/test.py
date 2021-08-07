import unittest
from random import randint

from dllist import DoubleLinkedList
from sort import bubble_sort


def random_list(count):
    numbers = DoubleLinkedList()
    for _ in range(count):
        numbers.push(randint(0, 1000))
    return numbers


def is_asc_sorted(numbers):
    node = numbers.begin
    while node.next:
        if node.value > node.next.value:
            return False
        node = node.next
    return True


def is_desc_sorted(numbers):
    node = numbers.begin
    while node.next:
        if node.value < node.next.value:
            return False
        node = node.next
    return True


class TestBubbleSort(unittest.TestCase):

    def test_sort_asc(self):
        numbers = random_list(100)
        bubble_sort(numbers)
        self.assertTrue(is_asc_sorted(numbers))

    def test_sort_desc(self):
        numbers = random_list(100)
        bubble_sort(numbers, reverse=True)
        self.assertTrue(is_desc_sorted(numbers))


if __name__ == "__main__":
    unittest.main()
