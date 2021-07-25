import unittest

from dllist import DoubleLinkedList


BLUE = "blue"
GREEN = "green"
RED = "red"
BLACK = "black"
WHITE = "white"


class TestDoubleLinkedList(unittest.TestCase):

    def test_count(self):
        colors = DoubleLinkedList()
        self.assertEqual(colors.count(), 0)

        colors.push(BLUE)
        self.assertEqual(colors.count(), 1)

        colors.push(RED)
        self.assertEqual(colors.count(), 2)

        colors.pop()
        self.assertEqual(colors.count(), 1)

        colors.pop()
        self.assertEqual(colors.count(), 0)

        colors.pop()
        self.assertEqual(colors.count(), 0)

    def test_push(self):
        colors = DoubleLinkedList()

        colors.push(BLUE)
        self.assertEqual(colors.count(), 1)

        colors.push(BLACK)
        self.assertEqual(colors.count(), 2)

    def test_pop(self):
        colors = DoubleLinkedList()

        colors.push(BLUE)
        colors.push(GREEN)

        self.assertEqual(colors.pop(), GREEN)
        self.assertEqual(colors.pop(), BLUE)
        self.assertEqual(colors.pop(), None)

    def test_shift(self):
        colors = DoubleLinkedList()

        colors.shift(BLUE)
        self.assertEqual(colors.count(), 1)

        colors.shift(GREEN)
        self.assertEqual(colors.count(), 2)

        self.assertEqual(colors.pop(), BLUE)
        self.assertEqual(colors.pop(), GREEN)

    def test_unshift(self):
        colors = DoubleLinkedList()

        colors.push(BLUE)
        colors.push(GREEN)
        colors.push(RED)

        self.assertEqual(colors.unshift(), BLUE)
        self.assertEqual(colors.count(), 2)

        self.assertEqual(colors.unshift(), GREEN)
        self.assertEqual(colors.count(), 1)

        self.assertEqual(colors.unshift(), RED)
        self.assertEqual(colors.count(), 0)

        self.assertEqual(colors.unshift(), None)
        self.assertEqual(colors.count(), 0)

    def test_first(self):
        colors = DoubleLinkedList()

        colors.push(BLUE)
        self.assertEqual(colors.first(), BLUE)

        colors.push(GREEN)
        self.assertEqual(colors.first(), BLUE)

        colors.shift(RED)
        self.assertEqual(colors.first(), RED)

        colors.unshift()
        self.assertEqual(colors.first(), BLUE)

    def test_last(self):
        colors = DoubleLinkedList()

        colors.push(BLUE)
        self.assertEqual(colors.last(), BLUE)

        colors.push(GREEN)
        self.assertEqual(colors.last(), GREEN)

        colors.shift(BLACK)
        self.assertEqual(colors.last(), GREEN)

        colors.pop()
        self.assertEqual(colors.last(), BLUE)

    def test_get(self):
        colors = DoubleLinkedList()

        colors.push(BLUE)
        colors.push(BLACK)
        colors.push(RED)

        self.assertEqual(colors.get(0), BLUE)
        self.assertEqual(colors.get(1), BLACK)
        self.assertEqual(colors.get(2), RED)
        self.assertEqual(colors.get(-1), None)
        self.assertEqual(colors.get(3), None)

    def test_remove(self):
        colors = DoubleLinkedList()

        colors.push(BLUE)
        colors.push(RED)
        colors.push(BLACK)

        self.assertEqual(colors.remove(GREEN), None)
        self.assertEqual(colors.remove(RED), RED)
        self.assertEqual(colors.count(), 2)
        self.assertEqual(colors.remove(RED), None)
        self.assertEqual(colors.remove(BLACK), BLACK)
        self.assertEqual(colors.count(), 1)
        self.assertEqual(colors.remove(BLUE), BLUE)
        self.assertEqual(colors.count(), 0)
        self.assertEqual(colors.remove(BLUE), None)
        self.assertEqual(colors.count(), 0)


if __name__ == "__main__":
    unittest.main()
