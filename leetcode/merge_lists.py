class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        cur = dummy
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        if list1:
            cur.next = list1
        else:
            cur.next = list2
        return dummy.next

def list2link(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    p = head
    for v in lst[1:]:
        p.next = ListNode(v)
        p = p.next
    return head

def link2list(node):
    arr = []
    while node:
        arr.append(node.val)
        node = node.next
    return arr

if __name__ == "__main__":
    s = Solution()
    print(link2list(s.mergeTwoLists(list2link([1,2,4]), list2link([1,3,4]))))
    print(link2list(s.mergeTwoLists(list2link([]), list2link([]))))
    print(link2list(s.mergeTwoLists(list2link([]), list2link([0]))))
