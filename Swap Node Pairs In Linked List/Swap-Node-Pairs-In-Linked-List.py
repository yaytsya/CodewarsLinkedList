from preloaded import Node

def swap_pairs(head):
    if head is None or head.next is None:
        return head
        
    second = head.next
    head.next = swap_pairs(second.next)
    second.next = head
    
    return second
