from preloaded import Node

def get_nth(node, index):
    if node is None or index < 0:
        raise ValueError
        
    current = node
    for _ in range(index):
        if current.next is None:
            raise ValueError
        current = current.next
        
    return current
