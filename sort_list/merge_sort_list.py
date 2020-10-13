class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        l, head_copy = [], head
        while head:
            l.append(head.val)
            head = head.next
        dummy = ListNode(0, head_copy)
        l.sort()
        for i in l:
            head_copy.val = i
            head_copy = head_copy.next
        return dummy.next
