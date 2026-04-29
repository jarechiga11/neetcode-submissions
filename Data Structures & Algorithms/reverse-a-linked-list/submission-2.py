# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     if not head or not head.next:
    #         return head

    #     newEnd = ListNode(head.val)
    #     return self.reverseListHelper(head.next, newEnd)
        


    # def reverseListHelper(self, currNode, prevNode):
    #     if currNode.next:
    #         tmpNext = currNode.next
    #         currNode.next = prevNode
    #         print(tmpNext.val, currNode.val, currNode.next.val)
    #         return self.reverseListHelper(tmpNext, currNode)

    #     currNode.next = prevNode
    #     return currNode

    ## Using Two Pointers (optimal)
        prevNode = None
        currNode = head

        while currNode:
            # temp store next node
            tmpNext = currNode.next
            # replace next with prev
            currNode.next = prevNode
            # make current new prev
            prevNode = currNode
            # move current to original next node
            currNode = tmpNext
        
        # while loop breaks once next is None (old end), so return prev
        return prevNode
