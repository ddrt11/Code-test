class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head, x):
        # 新建两个哑节点，分别串起小于x和大于等于x的节点
        small = ListNode()
        big = ListNode()
        s = small
        b = big
        cur = head
        
        # 遍历原链表，按值分到两个链表
        while cur:
            if cur.val < x:
                s.next = cur
                s = s.next
            else:
                b.next = cur
                b = b.next
            cur = cur.next
        
        # 大链表尾部置空，避免成环
        b.next = None
        # 拼接两个链表：小链表尾接大链表头
        s.next = big.next
        return small.next

# 辅助：链表转列表
def link2list(head):
    res = []
    p = head
    while p:
        res.append(p.val)
        p = p.next
    return res

if __name__ == "__main__":
    s = Solution()
    # 构造 1->4->3->2->5->2
    head = ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2))))))
    print(link2list(s.partition(head, 3)))
