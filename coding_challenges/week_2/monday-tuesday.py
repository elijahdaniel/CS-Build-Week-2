# /**
#  * Definition for singly-linked list.
#  * function ListNode(val, next) {
#  *     this.val = (val===undefined ? 0 : val)
#  *     this.next = (next===undefined ? null : next)

#  Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

# Example:

# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4

#  * }
#  */
# /**
#  * @param {ListNode} l1
#  * @param {ListNode} l2
#  * @return {ListNode}
#  */

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        ptr = head
        while True:
            if l1 is None and l2 is None:
                break
            if l1 is None:
                ptr.next = l2
                break
            if l2 is None:
                ptr.next = l1
                break
            else:
                if l1.val < l2.val:
                    ptr.next = ListNode(l1.val)
                    l1 = l1.next
                    ptr = ptr.next
                else:
                    ptr.next = ListNode(l2.val)
                    l2 = l2.next
                    ptr = ptr.next
        return head.next


console.log(mergeTwoLists([1, 2, 4], [1, 3, 4]))

# Runtime: 24 ms, faster than 99.77% of Python3 online submissions for Merge Two Sorted Lists.
# Memory Usage: 13.6 MB, less than 96.34% of Python3 online submissions for Merge Two Sorted Lists.
