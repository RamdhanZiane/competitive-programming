# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        hp=[(l.val,idx) for idx,l in enumerate(lists) if l]
        heapq.heapify(hp)
        root=None
        prev=None
        while hp:
            _,idx=heapq.heappop(hp)
            if prev is None:
                root=lists[idx]
                prev=root
            else:
                prev.next=lists[idx]
                prev=lists[idx]
            lists[idx]=lists[idx].next
            if lists[idx]:
                heapq.heappush(hp,(lists[idx].val,idx))
        return root