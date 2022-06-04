# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def iterate(list1:Optional[ListNode],list2:List)->List:
    while(list1!=None):
        list2.append(list1.val)
        list1=list1.next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        liste=[]
        iterate(list1,liste)
        iterate(list2,liste)
        liste.sort()
        del list1
        del list2
        header=None
        for i in range(len(liste)):
            n=ListNode(liste[i])
            if(i==0):
                header=n
            else:
                temp.next=n
            temp=n
            del n
        return header