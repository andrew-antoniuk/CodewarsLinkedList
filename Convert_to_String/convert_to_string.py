"""
Convert to String Lab 8
"""

class Node:

    """
    Docstring for Node
    """

    def __init__(self, data, n = None):
        self.data = data
        self.next = n

    def stringify(self, node) -> str:

        """
        Docstring for stringify

        Examples:
        >>> Node(0, Node(1, Node(4, Node(9, Node(16)))))
        "0 -> 1 -> 4 -> 9 -> 16 -> None"
        """

        s = []

        current = node

        # while

        return " -> ".join(s)
