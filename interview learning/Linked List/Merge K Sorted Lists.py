import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    
        heap=[]
        for i , node in enumerate(lists):
            if node is not None:
                heapq.heappush(heap , (node.val,i,node))
        dummy = ListNode()
        tail=dummy
        while heap:
            val,i,node =heapq.heappop(heap)
            tail.next=node
            tail=tail.next
            if node.next is not None:
                heapq.heappush(heap ,(node.next.val,i,node.next))
        return dummy.next