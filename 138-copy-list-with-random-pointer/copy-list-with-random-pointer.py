"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        node = head
        mp = {}
        mp2 = {}
        i = 0
        prev = None
        while node:
            new_node = Node(node.val)
            if prev:
                prev.next = new_node
            else:
                new_head = new_node
            prev = new_node
            mp[node] = i
            mp2[i] = new_node
            node = node.next
            i += 1
        mp2[-1] = None
        rands = {}
        node = head
        i = 0
        while node:
            rands[i] = mp[node.random] if node.random else -1
            i += 1
            node = node.next
        node = new_head
        i = 0
        while node is not None:
            print(node is None)
            node.random = mp2[rands[i]]
            node = node.next
            i += 1
        return new_head