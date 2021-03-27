class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def build(self, nums:[]):
        if len(nums) <= 0:return None
        head = ListNode(nums[0])
        p = head
        i = 1
        while i < len(nums):
            p.next = ListNode(nums[i])
            p = p.next
            i += 1
        return head

    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if left >= right: return head
        leftis1 = False
        if left == 1:
            tmp = ListNode()
            tmp.next = head
            head = tmp
            left += 1
            right += 1
            leftis1 = True
        cnt = 1
        p = head
        while p is not None and cnt < left-1:
            cnt += 1
            p = p.next
        before_l = p
        while p is not None and cnt <= right:
            cnt += 1
            p = p.next
        after_r = p
        p = before_l.next
       # print(before_l.val, after_r.val)
        while p != after_r:
            tmp = p.next
            if before_l.next != p:
                p.next = before_l.next
            else:
                p.next = after_r
            before_l.next = p
            print("this p.val is {}".format(p.val))
            p = tmp
        #print(p.val)
        if leftis1:
            return head.next
        return head

def display(head):
    p = head
    while p is not None:
        print(p.val)
        p = p.next
sol = Solution()
nums = [1,2,3,4,5,6,7]
#nums = [3, 5]
head = sol.build(nums)
#display(head)
res = sol.reverseBetween(head, 2, 4)
display(res)
