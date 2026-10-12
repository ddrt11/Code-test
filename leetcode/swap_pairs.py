class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head):
        dummy = ListNode(0, head)
        pre = dummy
        while pre.next and pre.next.next:
            first = pre.next
            second = pre.next.next
            pre.next = second
            first.next = second.next
            second.next = first
            pre = first
        return dummy.next

def list2link(lst):
    if not lst:
        return None
    h = ListNode(lst[0])
    p = h
    for v in lst[1:]:
        p.next = ListNode(v)
        p = p.next
    return h

def link2list(node):
    arr = []
    while node:
        arr.append(node.val)
        node = node.next
    return arr

if __name__ == "__main__":
    sol = Solution()
    print(link2list(sol.swapPairs(list2link([1,2,3,4]))))
    print(link2list(sol.swapPairs(list2link([]))))
    print(link2list(sol.swapPairs(list2link([1]))))
