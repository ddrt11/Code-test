
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()
        cur = dummy
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            total = v1 + v2 + carry
            carry = total // 10
            cur.next = ListNode(total % 10)
            cur = cur.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        return dummy.next

def list_to_linked(nums):
    dummy = ListNode()
    cur = dummy
    for num in nums:
        cur.next = ListNode(num)
        cur = cur.next
    return dummy.next

def linked_to_list(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res

if __name__ == "__main__":
    sol = Solution()
    print(linked_to_list(sol.addTwoNumbers(list_to_linked([2,4,3]), list_to_linked([5,6,4]))))
    print(linked_to_list(sol.addTwoNumbers(list_to_linked([0]), list_to_linked([0]))))
    print(linked_to_list(sol.addTwoNumbers(list_to_linked([9,9,9,9,9,9,9]), list_to_linked([9,9,9,9]))))
