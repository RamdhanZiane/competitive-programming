# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        prev = None
        while node and node.next:
            if node.val == node.next.val:
                v = node.val
                while node and node.val == v:
                    node = node.next
                if prev:
                    prev.next = node
                else:
                    head = node
                    prev = None
            else:
                prev = node
                node = node.next
        return head
        