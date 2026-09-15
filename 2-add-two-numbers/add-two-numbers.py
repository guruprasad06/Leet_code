# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dumy=ListNode(0)
        c=dumy
        carry=0
        while l1 or l2 or carry:
            v1=l1.val if l1 else 0  # 8
            v2=l2.val if l2 else 0  # 6
            total=v1+v2+carry # 14
            carry=total//10  #1 carry
            c.next=ListNode(total%10) # 4 node
            c=c.next
            if l1:l1=l1.next
            if l2:l2=l2.next
        return dumy.next