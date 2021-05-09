def has_cycle(head):
    if not head.next:
        return 0
    
    current = head
    target = head.next
    
    while current != target:
        current = current.next
        target = target.next.next
        
        if not current.next or not target.next:
            return 0
    
    return 1
    