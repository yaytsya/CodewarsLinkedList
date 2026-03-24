def loop_size(node):
    slow = node.next
    fast = node.next.next
    
    while slow != fast:
        slow = slow.next
        fast = fast.next.next
        
    count = 1
    fast = fast.next
    while slow != fast:
        fast = fast.next
        count += 1
        
    return count
