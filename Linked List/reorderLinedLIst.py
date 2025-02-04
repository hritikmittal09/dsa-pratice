class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorder_list(head):
    if not head or not head.next or not head.next.next:
        return  # No need to reorder if less than 3 nodes
    
    # Step 1: Find the middle using slow and fast pointers
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Step 2: Reverse the second half of the list
    prev, cur = None, slow.next
    slow.next = None  # Split the list into two halves
    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt

    # Step 3: Merge the two halves
    first, second = head, prev  # `first` points to first half, `second` to reversed second half
    while second:
        tmp1, tmp2 = first.next, second.next
        first.next = second
        second.next = tmp1
        first, second = tmp1, tmp2  # Move pointers forward

