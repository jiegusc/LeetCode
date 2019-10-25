class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode((l1.val+l2.val)%10)
        start = result
        updater = (l1.val+l2.val)//10
        while result is not None:
            if l1.next is None and l2.next is None:
                if updater != 0:
                    result.next = ListNode(updater)
                return start
            elif l2.next is None:
                result.next = ListNode((l1.next.val+updater)%10)
                updater = (l1.next.val+updater)//10
                l1 = l1.next
                result = result.next
            elif l1.next is None:
                l2 = l2.next
                result.next = ListNode((l2.val+updater)%10)
                updater = (l2.val+updater)//10
                result = result.next
            else:
                l1 = l1.next
                l2 = l2.next
                result.next = ListNode((l1.val+l2.val+updater)%10)
                updater = (l1.val+l2.val+updater)//10
                result = result.next


