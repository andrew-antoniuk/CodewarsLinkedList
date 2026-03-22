"""
Docstring for CodewarsLinkedList.parse_from_string.parse_from_string
"""

from CodewarsLinkedList.preloaded import Node

def linked_list_from_string(list_repr: str) -> Node | None:

    """
    Convert string representation of the linked list into a real linked sequence
    """

    if not isinstance(list_repr, str) or list_repr.strip() == "None" or not list_repr:
        return None

    values = list_repr.strip().split(" -> ")

    if values[-1] == "None":
        values.pop()

    head = None

    for n in reversed(values):

        head = Node(int(n), head)

    return head
