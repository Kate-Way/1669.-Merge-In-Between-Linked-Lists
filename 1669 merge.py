# 1669. Merge In Between Linked Lists

# You are given two linked lists: list1 and list2 of sizes n and m respectively.
#
# Remove list1's nodes from the ath node to the bth node, and put list2 in their place.
#
# Build the result list and return its head.
# Input: list1 = [0,1,2,3,4,5], a = 3, b = 4, list2 = [1000000,1000001,1000002]
# Output: [0,1,2,1000000,1000001,1000002,5] - removed 3 and 4 and inserted list2 in its place

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def merge_in_between(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        pointer = 1
        curr = list1  # curr node = head of list 1
        while pointer < a:
            curr = curr.next
            pointer += 1
        list1_next = curr.next  # list1_next is the next node connection to which we are going to break
        curr.next = list2  # link the node before 'a' to the head of list2
        while curr.next:
            curr = curr.next  # proceed till the end of list2
        while (pointer >= a) and (pointer < b):
            list1_next = list1_next.next  # from list1 get the last node before 'b'
            pointer += 1

        curr.next = list1_next.next  # link the tail of list2 to b value of list1
        return list1