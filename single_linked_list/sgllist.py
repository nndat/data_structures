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

    def __str__(self):
        current_node = self.begin
        values = []
        while current_node:
            values.append(current_node.value)
            current_node = current_node.next
        return '->'.join(values)

    def push(self, obj):
        """
        Appends a new value on the end of list.
        """
        new_node = SingleLinkedListNode(obj, None)
        if self.begin is None:
            self.begin = new_node

        if self.end is None:
            self.end = new_node
        else:
            self.end.next = new_node
            self.end = new_node

    def pop(self):
        """
        Removes the last item and return it.
        """
        last_node = self.end

        if self.begin is self.end:
            self.begin = self.end = None
        else:
            current_node = self.begin
            while current_node.next is not self.end:
                current_node = current_node.next

            self.end = current_node
            self.end.next = None

        return last_node and last_node.value or None

    def shift(self, obj):
        """
        Another name for push.
        """
        new_node = SingleLinkedListNode(obj, None)
        if self.begin is None:
            self.begin = self.end = new_node
        else:
            new_node.next = self.begin
            self.begin = new_node

    def unshift(self):
        """
        Removes the first item and return it.
        """
        first_node = self.begin
        if self.begin is None:
            return None
        elif self.begin is self.end:
            self.begin = self.end = None
        else:
            self.begin = self.begin.next
        return first_node.value

    def remove(self, obj):
        """
        Finds a matching item and removes it from list.
        """
        current_node = self.begin
        current_index = 0
        prev_node = None

        while current_node and current_node.value != obj:
            prev_node = current_node
            current_node = current_node.next
            current_index += 1

        if current_node is None:
            return

        if current_node is self.begin and current_node is self.end:
            self.begin = self.end = None
        elif current_node is self.begin:
            self.begin = current_node.next
        elif current_node is self.end:
            self.end = prev_node
            self.end.next = None
        else:
            prev_node.next = current_node.next

        return current_index

    def first(self):
        """
        Return a *reference* to the first item, does not remove.
        """
        return self.begin and self.begin.value or None

    def last(self):
        """
        Return a reference to the last item, does not remove.
        """
        return self.end and self.end.value or None

    def count(self):
        """
        Counts the number of elements in the list.
        """
        count = 0
        current_node = self.begin
        while current_node:
            count += 1
            current_node = current_node.next
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
        return current_node and current_node.value or None

    def dump(self, mark):
        """
        Debugging function that dumps the contents of the list.
        """
        pass
