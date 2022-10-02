# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    # Time: O(n), Space: O(1)
    def reverseLinkedList(self, head, k):
        new_head, ptr = None, head
        while k:
            next_node = ptr.next
            # Insert node pointed to by "ptr" at beginning of reversed list
            ptr.next = new_head
            new_head = ptr
            # move on to next node
            ptr = next_node
            k -= 1
        return new_head # head of reversed list
        
    def reverseKGroup(self, head, k):
        ptr = head
        ktail = None
        # Head of final, modified linked list
        new_head = None
        # keep going until there're nodes in list
        while ptr:
            count = 0
            # start counting nodes from head
            ptr = head
            # Find head of next k nodes
            while count < k and ptr:
                ptr = ptr.next
                count += 1
            # If we counted k nodes, reverse them
            if count == k:
                # reverse k nodes & get new head
                revHead = self.reverseLinkedList(head, k)
                # new_head is head of final linked list
                if not new_head:
                    new_head = revHead
                # ktail is tail of previous block of reversed k nodes
                if ktail:
                    ktail.next = revHead
                ktail = head
                head = ptr
        # attach final, possibly un-reversed portion
        if ktail:
            ktail.next = head
        return new_head if new_head else head
