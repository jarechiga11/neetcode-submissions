# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    
        # My Solution
        # curr1 = list1
        # curr2 = list2
        # start = None
        # prev = None

        # while curr1 or curr2:
        #     # print(curr1.val if curr1 else 0, curr2.val if curr2 else 0)

        #     # if list2 empty or reached end
        #     if curr1 and not curr2:
        #         if not start:
        #             start = curr1
        #         if not prev:
        #             prev = start
        #         else:
        #             prev.next = curr1
        #             prev = curr1
        #         curr1 = curr1.next
            
        #     # if list1 empty or reached end
        #     elif curr2 and not curr1:
        #         if not start:
        #             start = curr2
        #         if not prev:
        #             prev = start
        #         else:
        #             prev.next = curr2
        #             prev = curr2
        #         curr2 = curr2.next

        #     elif curr1.val <= curr2.val:
        #         tmp1 = curr1.next
        #         if not start:
        #             start = curr1
        #         if prev:
        #             prev.next = curr1
        #         prev = curr1
        #         curr1 = tmp1
            
        #     elif curr2.val < curr1.val:
        #         tmp2 = curr2.next
        #         if not start:
        #             start = curr2
        #         if prev:
        #             prev.next = curr2
        #         prev = curr2
        #         curr2 = tmp2

        # return start

        #Optimal/simpler solution
        start = ListNode(0) # fake start but easy to append to
        tail = start # most recently appended

        # only loop while both have nodes (reason below)
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                tail = list1
                list1 = list1.next
            else:
                tail.next = list2
                tail = list2
                list2 = list2.next
        
        # now append any remaining lists
        if list1:
            # meaning list2 is now empty
            tail.next = list1
        else:
            # meaning list1 is now empty
            tail.next = list2
        
        # since start was fake, return the true start
        return start.next
            

            





        