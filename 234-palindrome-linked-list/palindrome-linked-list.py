# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        s1 = []
        s2 = []
        fast = slow
        slow = head
        while fast:
            s1.append(slow.val)
            s2.append(fast.val)
            fast = fast.next
            slow = slow.next
        s2.reverse()
        return s1==s2