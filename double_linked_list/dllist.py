class DoubleLinkedListNode(object):
    def __init__(self, value, nxt=None, prev=None):
        self.value = value
        self.next = nxt
        self.prev = prev

    def __repr__(self):
        nval = self.next and self.next.value or None
        pval = self.prev and self.prev.value or None
        return f"{repr(self.value)}, {repr(nval)}, {repr(pval)}"


class DoubleLinkedList(object):
    def __init__(self):
        self.begin = None
        self.end = None

    def push(self, obj):
        """
        Appends a new value on the end of the list.
        """
        new_node = DoubleLinkedListNode(obj)
        if self.begin is None:
            # list is empty
            self.begin = self.end = new_node
        else:
            new_node.prev = self.end
            self.end.next = new_node
            self.end = new_node

        assert self.begin.prev is None
        assert self.end.next is None

    def pop(self):
        """
        Removes the last item and return it value.
        """
        value = self.end.value if self.end else None
        if self.end is None:
            return value
        elif self.begin is self.end:
            self.begin = self.end = None
        else:
            self.end = self.end.prev
            self.end.next = None
            assert self.end.next is None
        return value

    def shift(self, obj):
        """
        Appends a new value on the begin of the list.
        """
        new_node = DoubleLinkedListNode(obj)
        if self.begin is None:
            self.begin = self.end = new_node
        else:
            new_node.next = self.begin
            self.begin.prev = new_node
            self.begin = new_node
        assert self.begin.prev is None
        assert self.end.next is None

    def unshift(self):
        """
        Removes the first item (from begin) and returns it.
        """
        value = self.begin.value if self.begin else None
        if self.begin is None:
            return None
        if self.begin.next:
            self.begin = self.begin.next
            self.begin.prev = None
            assert self.begin.prev is None
            assert self.end.next is None
        else:
            self.begin = self.end = None
        return value

    def detach_node(self, node):
        pass

    def remove(self, obj):
        """
        Finds a matching item and removes it from the list.
        """
        current_node = self.begin

        while current_node and current_node.value != obj:
            current_node = current_node.next

        if current_node is None:
            return None

        prev_node = current_node.prev
        next_node = current_node.next

        if prev_node and next_node:
            prev_node.next = next_node
            next_node.prev = prev_node
        elif next_node:
            next_node.prev = None
        elif prev_node:
            prev_node.next = None
        else:
            self.begin = self.end = None
        return current_node.value

    def first(self):
        """
        Returns a reference to the first item, does not remove.
        """
        if self.begin:
            return self.begin.value
        return None

    def last(self):
        """
        Return the last item, does not remove.
        """
        if self.end:
            return self.end.value
        return None

    def count(self):
        """
        Counts the number of elements in the list.
        """
        count = 0
        node = self.begin
        while node:
            count += 1
            node = node.next
        return count

    def get(self, index):
        """
        Get the value at index.
        """
        current_index = 0
        current_node = self.begin

        while current_node and current_index != index:
            current_node = current_node.next
            current_index += 1
        if current_node:
            return current_node.value
        return None
