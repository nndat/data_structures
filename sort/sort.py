def gt(v1, v2):
    """
    Check if value v1 is greater than v2
    """
    return v1 > v2


def lt(v1, v2):
    """
    Check if value v1 is less than v2
    """
    return v1 < v2


def bubble_sort(dllist, reverse=False):
    is_swap = lt if reverse else gt

    while True:
        is_sorted = True
        node = dllist.begin
        while node.next:
            if is_swap(node.value, node.next.value):
                node.value, node.next.value = \
                        node.next.value, node.value
                is_sorted = False
            node = node.next

        if is_sorted:
            break

    return dllist


def merge_sort(ddlist, reverse=False):
    pass


def merge(left, right):
    pass

