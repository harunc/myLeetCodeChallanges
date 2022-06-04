def iterate(list1:Optional[ListNode],list2:List)->List:
    while(list1!=None):
        list2.append(list1.val)
        list1=list1.next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        liste=[]
        liste1=[]
        iterate(list1,liste)
        iterate(list2,liste1)
        liste.extend(liste1)
        liste.sort()
        del list1
        del list2
        del liste1
        header=ListNode(0)
        temp=header
        for i in range(len(liste)):
            n=ListNode(liste[i])
            temp.next=n
            temp=n
            del n
        header=header.next
        del temp
        return header