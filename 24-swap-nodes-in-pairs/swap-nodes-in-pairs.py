# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        node=head
        if node.next:
            head=node.next
        prev=None
        while node and node.next:
            tmp=node.next
            if prev:
                prev.next=tmp
            node.next=node.next.next
            tmp.next=node
            prev=node
            node=node.next
        return head