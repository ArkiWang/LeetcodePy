class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None or l2 == None:
            return l1 if l1 != None else l2
        resl = None
        pr = resl
        p1, p2 = l1, l2
        while p1 != None and p2 != None:
            if resl == None:
                resl = ListNode((p1.val + p2.val)%10)
                c = int((p1.val + p2.val)/10)
                pr = resl
            else:
                pr.next = ListNode((p1.val + p2.val + c)%10)
                c = int((p1.val + p2.val + c)/10)
            p1 = p1.next
            p2 = p2.next

        while p1 != None:
            pr.next = ListNode((p1.val + c)%10)
            c = int((p1.val + c) / 10)
            p1 = p1.next

        while p2 != None:
            pr.next = ListNode((p2.val + c) % 10)
            c = int((p2.val + c) / 10)
            p2 = p2.next

        if c != 0:
            pr.next = ListNode(c)

        return resl

sol = Solution()

