# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Iterative
    # Time: O(n)
    # Space: O(1)
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

    # Recursive
    # Time: O(n)
    # Space: O(n)
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        if not node or not node.next: # make sure linked list is greater than 2 nodes
            return node
        p = self.reverseList(node.next)
        node.next.next = node
        node.next = None
        return p

'''
All the values before it will be reversed.
1 -> 2 -> 3 to 1 -> 3 -> 2 to 3 -> 2 -> 1
Want to take value before in recursive call (node.next), take its next pointer, and set it to node
Then set node.next to None to prepare it for the next recursive call
'''
