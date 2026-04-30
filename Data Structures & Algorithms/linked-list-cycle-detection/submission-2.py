# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # track nodes visited (with their next node vals)
        nodeMap = {}

        while head:
            if head.val in nodeMap and head.next == nodeMap[head.val]:
                # check if same node (val+next) is in map, if yes, then node was already visited = cycle
                return True
            else:
                # add node to map and goto next node
                nodeMap[head.val] = head.next
                head = head.next
        
        return False