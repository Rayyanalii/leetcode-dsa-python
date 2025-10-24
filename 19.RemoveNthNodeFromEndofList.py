from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self,head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None
        i=head
        length=0
        while i.next is not None:
            length+=1
            i=i.next
        length+=1
        
        curr=head
        prev=None
        for x in range(length-n):
            prev=curr
            curr=curr.next
        if prev:
            prev.next = curr.next
            return head
        else:
            return head.next

    
def build_linked_list(arr):
    dummy = ListNode(0)
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

def print_linked_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(result)

head = build_linked_list([1,2])
sol = Solution()
result = sol.removeNthFromEnd(head, 2)

print_linked_list(result)