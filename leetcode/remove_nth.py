class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy
        for i in range(n):
            fast = fast.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next

def list2link(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    cur = head
    for v in lst[1:]:
        cur.next = ListNode(v)
        cur = cur.next
    return head

def link2list(node):
    res = []
    while node:
        res.append(node.val)
        node = node.next
    return res

if __name__ == "__main__":
    s = Solution()
    print(link2list(s.removeNthFromEnd(list2link([1,2,3,4,5]), 2)))
    print(link2list(s.removeNthFromEnd(list2link([1]), 1)))
    print(link2list(s.removeNthFromEnd(list2link([1,2]), 1)))
