def reverse_linked_list(head):
    pre = None
    cur = head
    
    while cur is not None:
        ne = cur.next  # Store the next node before modifying `cur.next`
        cur.next = pre  # Reverse the link
        pre = cur  # Move `pre` forward
        cur = ne  # Move `cur` forward
    
    return pre  # `pre` is the new head of the reversed linked list