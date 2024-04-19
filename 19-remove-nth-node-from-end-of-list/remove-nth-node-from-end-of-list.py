# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        sz = 1
        node = head.next
        while node:
            node = node.next
            sz += 1
        node = head
        prev = None
        for _ in range(sz-n):
            prev = node
            node = node.next
        if sz == n:
            return node.next
        prev.next = node.next
        return head