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
        
        while(cur):
            nxt=cur.next
            cur.next=prev
            prev=cur
            cur=nxt
        tail=prev
        print(head1.next.next.val)
        print(tail.next.val)
        head=head1
        first=head
        dummy=ListNode()
        dummy.next=head
        while(tail.val>first.val):
            temp=first.next
            temp1=tail.next
            first.next=tail
            tail.next=temp
            first=temp
            tail=temp1
            print(first.val)
        
        
        