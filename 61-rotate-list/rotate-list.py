# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        sz = 0
        node = head
        while node:
            prev = node
            node = node.next
            sz += 1
        if sz < 2:
            return head
        prev.next = head
        k = k%sz
        node = prev
        new_head = node.next
        for _ in range(sz-k):
            node = node.next
            new_head = node.next
        node.next = None
        return new_head