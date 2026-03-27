"""
Docstring for swap_nodes.swap_nodes
"""

from preloaded import Node

def swap_pairs(head):

    """
    Docstring for swap_pairs

    :param head: Description
    :return: Description
    :rtype: Any
    """

    prev_head = Node(0)
    prev_head.next = head
    previous = prev_head
    current = head


    while current is not None and current.next is not None: # pair check
        first = current
        second = current.next

        previous.next = second
        first.next = second.next

        # complete the swap
        second.next = first

        # move forward
        previous = first
        current = first.next

    return prev_head.next
