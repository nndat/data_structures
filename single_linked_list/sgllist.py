class SingleLinkedListNode(object):
    def __init__(self, value, nxt):
        self.value = value
        self.next = nxt

    def __repr__(self):
        next_value = self.next and self.next.value or None
        return f"[{self.value}->{repr(next_value)}]"


class SingleLinkedList(object):
    def __init__(self):
        self.begin = None
        self.end = None

    def push(self, obj):
        """
        Appends a new value on the end of list.
        """
        pass

    def pop(self):
        """
        Removes the last item and return it.
        """
        pass

    def shift(self):
        """
        Another name for push.
        """
        pass

    def unshift(self):
        """
        Removes the first item and return it.
        """
        pass

    def remove(self, obj):
        """
        Finds a matching item and removes it from list.
        """
        pass

    def first(self):
        """
        Return a *reference* to the first item, does not remove.
        """
        pass

    def last(self):
        """
        Return a reference to the last item, does not remove.
        """
        pass

    def count(self):
        """
        Counts the number of elements in the list.
        """
        pass

    def get(self, index):
        """
        Get the value at index.
        """
        pass

    def dump(self, mark):
        """
        Debugging function that dumps the contents of the list.
        """
        pass

