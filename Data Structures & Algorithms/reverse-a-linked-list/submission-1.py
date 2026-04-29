# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        newEnd = ListNode(head.val)
        return self.reverseListHelper(head.next, newEnd)
        


    def reverseListHelper(self, currNode, prevNode):
        if currNode.next:
            tmpNext = currNode.next
            currNode.next = prevNode
            print(tmpNext.val, currNode.val, currNode.next.val)
            return self.reverseListHelper(tmpNext, currNode)

        currNode.next = prevNode
        return currNode