# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    

        curr1 = list1
        curr2 = list2
        start = None
        prev = None

        while curr1 or curr2:
            print(curr1.val if curr1 else 0, curr2.val if curr2 else 0)

            if curr1 and not curr2:
                if not start:
                    start = curr1
                if not prev:
                    prev = start
                else:
                    prev.next = curr1
                    prev = curr1
                curr1 = curr1.next
            
            elif curr2 and not curr1:
                if not start:
                    start = curr2
                if not prev:
                    prev = start
                else:
                    prev.next = curr2
                    prev = curr2
                curr2 = curr2.next

            elif curr1.val <= curr2.val:
                tmp1 = curr1.next
                if not start:
                    start = curr1
                if prev:
                    prev.next = curr1
                prev = curr1
                curr1 = tmp1
            
            elif curr2.val < curr1.val:
                tmp2 = curr2.next
                if not start:
                    start = curr2
                if prev:
                    prev.next = curr2
                prev = curr2
                curr2 = tmp2
            



            # if prev1 and not curr1:
            #     prev1.next = curr2
            #     curr2 = curr2.next
            # elif prev1 and not curr2:
            #     curr1 = curr1.next
            # elif curr1.val <= curr2.val:
            #     curr1 = curr1.next
            # elif prev1:
            #     prev1.next = curr2
            #     tmp2 = curr2.next
            #     curr2.next = curr1
            #     prev1 = curr1
            #     curr1 = curr1.next
            #     curr2 = tmp2

        return start

            





        