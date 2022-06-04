# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def toString(l:List,a:str)->str:
    for i in l:
        a=a+str(i)
    return a
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list1=[]
        list2=[]
        while l1!=None:
            list1.append(l1.val)
            l1=l1.next
        while l2!=None:
            list2.append(l2.val)
            l2=l2.next
        del l1
        del l2
        list1.reverse()
        list2.reverse()
        a=""
        b=""
        a=toString(list1,a)
        b=toString(list2,b)
        del list1
        del list2
        c=int(a)+int(b)
        a=str(c)
        headNode=ListNode(0)
        l1=ListNode(0)
        headNode=l1
        i=1
        while(True):
            try:
                l1.val=int(a[-i])
                
                i+=1
                if i == len(a)+1:
                    break
                node=ListNode(0)
                l1.next=node
                l1=l1.next
            except(IndexError):
                break
        return headNode