class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head):
        cur = head
        # 遍历链表，遇到重复就跳过下一个节点
        while cur and cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head

def link2list(head):
    res = []
    p = head
    while p:
        res.append(p.val)
        p = p.next
    return res

if __name__ == "__main__":
    s = Solution()
    n1 = ListNode(1, ListNode(1, ListNode(2)))
    print(link2list(s.deleteDuplicates(n1)))
    a1 = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
    print(link2list(s.deleteDuplicates(a1)))
