import unittest

from sgllist import *


RED = "red"
BLUE = "blue"
GREEN = "green"


class TestSingleLinkedList(unittest.TestCase):

    def test_create_single_linked_list_node_without_next_node(self):
        one = SingleLinkedListNode("one", None)
        self.assertEqual(one.value, "one")
        self.assertEqual(one.next, None)
        self.assertEqual(repr(one), "[one->None]")

    def test_create_single_linked_list_with_next_node(self):
        two = SingleLinkedListNode("two", None)
        one = SingleLinkedListNode("one", two)
        self.assertEqual(one.value, "one")
        self.assertEqual(two.value, "two")
        self.assertEqual(one.next, two)
        self.assertEqual(two.next, None)
        self.assertEqual(repr(one), "[one->'two']")

    def test_push(self):
        colors = SingleLinkedList()
        colors.push("Pthalo Blue")
        self.assertEqual(colors.count(), 1)

        colors.push("Ultramarine Blue")
        self.assertEqual(colors.count(), 2)

    def test_pop(self):
        colors = SingleLinkedList()
        magenta = "Magenta"
        alizarin = "Alizarin"
        colors.push(magenta)
        colors.push(alizarin)
        self.assertEqual(colors.pop(), alizarin)
        self.assertEqual(colors.pop(), magenta)
        self.assertEqual(colors.pop(), None)
        self.assertEqual(colors.pop(), None)

    def test_shift(self):
        colors = SingleLinkedList()

        colors.shift(BLUE)
        self.assertEqual(colors.count(), 1)

        colors.shift(GREEN)
        self.assertEqual(colors.count(), 2)

        self.assertEqual(colors.pop(), BLUE)
        self.assertEqual(colors.count(), 1)

        self.assertEqual(colors.pop(), GREEN)
        self.assertEqual(colors.count(), 0)

    def test_first(self):
        colors = SingleLinkedList()

        colors.push(BLUE)
        self.assertEqual(colors.first(), BLUE)

        colors.push(GREEN)
        self.assertEqual(colors.first(), BLUE)

        colors.shift(RED)
        self.assertEqual(colors.first(), RED)

    def test_last(self):
        colors = SingleLinkedList()

        colors.push(RED)
        self.assertEqual(colors.last(), RED)

        colors.push(BLUE)
        self.assertEqual(colors.last(), BLUE)

        colors.shift(GREEN)
        self.assertEqual(colors.last(), BLUE)

    def test_get(self):
        colors = SingleLinkedList()
        colors.push("Vermillion")
        self.assertEqual(colors.get(0), "Vermillion")
        colors.push("Sap Green")
        self.assertEqual(colors.get(0), "Vermillion")
        self.assertEqual(colors.get(1), "Sap Green")
        colors.push("Cadmium Yellow Light")
        self.assertEqual(colors.get(0), "Vermillion")
        self.assertEqual(colors.get(1), "Sap Green")
        self.assertEqual(colors.get(2), "Cadmium Yellow Light")
        self.assertEqual(colors.pop(), "Cadmium Yellow Light")
        self.assertEqual(colors.get(0), "Vermillion")
        self.assertEqual(colors.get(1), "Sap Green")
        self.assertEqual(colors.get(2), None)
        colors.pop()
        self.assertEqual(colors.get(0), "Vermillion")
        colors.pop()
        self.assertEqual(colors.get(0), None)


class TestFromZedShaw(unittest.TestCase):

    def test_push(self):
        colors = SingleLinkedList()
        colors.push("Pthalo Blue")
        assert colors.count() == 1
        colors.push("Ultramarine Blue")
        assert colors.count() == 2

    def test_pop(self):
        colors = SingleLinkedList()
        colors.push("Magenta")
        colors.push("Alizarin")
        assert colors.pop() == "Alizarin"
        assert colors.pop() == "Magenta"
        assert colors.pop() == None

    def test_unshift(self):
        colors = SingleLinkedList()
        colors.push("Viridian")
        colors.push("Sap Green")
        colors.push("Van Dyke")
        assert colors.unshift() == "Viridian"
        assert colors.unshift() == "Sap Green"
        assert colors.unshift() == "Van Dyke"
        assert colors.unshift() == None

    def test_shift(self):
        colors = SingleLinkedList()
        colors.shift("Cadmium Orange")
        assert colors.count() == 1

        colors.shift("Carbazole Violet")
        assert colors.count() == 2

        assert colors.pop() == "Cadmium Orange"
        assert colors.count() == 1
        assert colors.pop() == "Carbazole Violet"
        assert colors.count() == 0

    def test_remove(self):
        colors = SingleLinkedList()
        colors.push("Cobalt")
        colors.push("Zinc White")
        colors.push("Nickle Yellow")
        colors.push("Perinone")
        assert colors.remove("Cobalt") == 0
        colors.dump("before perinone")
        assert colors.remove("Perinone") == 2
        colors.dump("after perinone")
        assert colors.remove("Nickle Yellow") == 1
        assert colors.remove("Zinc White") == 0

    def test_first(self):
        colors = SingleLinkedList()
        colors.push("Cadmium Red Light")
        assert colors.first() == "Cadmium Red Light"
        colors.push("Hansa Yellow")
        assert colors.first() == "Cadmium Red Light"
        colors.shift("Pthalo Green")
        assert colors.first() == "Pthalo Green"

    def test_last(self):
        colors = SingleLinkedList()
        colors.push("Cadmium Red Light")
        assert colors.last() == "Cadmium Red Light"
        colors.push("Hansa Yellow")
        assert colors.last() == "Hansa Yellow"
        colors.shift("Pthalo Green")
        assert colors.last() == "Hansa Yellow"

    def test_get(self):
        colors = SingleLinkedList()
        colors.push("Vermillion")
        assert colors.get(0) == "Vermillion"
        colors.push("Sap Green")
        assert colors.get(0) == "Vermillion"
        assert colors.get(1) == "Sap Green"
        colors.push("Cadmium Yellow Light")
        assert colors.get(0) == "Vermillion"
        assert colors.get(1) == "Sap Green"
        assert colors.get(2) == "Cadmium Yellow Light"
        assert colors.pop() == "Cadmium Yellow Light"
        assert colors.get(0) == "Vermillion"
        assert colors.get(1) == "Sap Green"
        assert colors.get(2) == None
        colors.pop()
        assert colors.get(0) == "Vermillion"
        colors.pop()
        assert colors.get(0) == None


if __name__ == "__main__":
    unittest.main()

