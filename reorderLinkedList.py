# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        prev,cur=None,head
        tmp=head
        newL=ListNode()
        head1=newL
        while(tmp):
            newN=ListNode(tmp.val)
            newL.next=newN
            newL=newN
            tmp=tmp.next
        print(head1.next.val)
        while(cur):
            nxt=cur.next
            cur.next=prev
            prev=cur
            cur=nxt
        tail=prev
        head=head1
        dummy=ListNode()
        dummy.next=head
        while(tail.val>head.val):
            temp=head.next
            temp1=tail.next
            head.next=tail
            temp.next=tail.next
            tail.next=temp
            head=temp
            tail=temp1
        head=dummy.next