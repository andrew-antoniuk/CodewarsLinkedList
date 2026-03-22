"""
Remove Duplicates LeetCode Lab 8
"""

from typing import Optional

class ListNode:

    """
    Docstring for ListNode
    """

    def __init__(self, val = 0, n = None):
        self.val = val
        self.next = n

class Solution:

    """
    Docstring for Solution
    """

    def delete_duplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        """
        Docstring for deleteDuplicates
        Input: head = [1,2,3,3,4,4,5]
        Output: [1,2,5]
        """

        current = head
        prev_head = ListNode(None, head)
        previous = prev_head

        while current is not None and current.next is not None:
            if current.val != current.next.val:
                previous = current
                current = current.next
                continue

            value = current.val
            while current is not None and current.val == value:
                current = current.next
            previous.next = current

        return prev_head.next
