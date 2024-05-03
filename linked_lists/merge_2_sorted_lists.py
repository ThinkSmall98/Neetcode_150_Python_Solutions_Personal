# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # iterative 
    # Time: O(n + m)
    # Space: O(1)
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node = ListNode()
        start_pointer = node
        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next
        if list1:
            node.next = list1
        elif list2:
            node.next = list2
        return start_pointer.next

    # recursive 
    # Time: O(n + m)
    # Space: O(n + m)
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        # swap if list1 val bigger than list 2's
        if list1.val > list2.val:
            list1, list2 = list2, list1
        # get list1's next node
        list1.next = self.mergeTwoLists(list1.next, list2)
        return list1


