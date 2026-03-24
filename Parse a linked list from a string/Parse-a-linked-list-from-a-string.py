from preloaded import Node

def linked_list_from_string(list_repr: str) -> Node | None:
    if list_repr == "None":
        return None
    
    values = list_repr.split(" -> ")
    
    head = None
    
    for val in reversed(values[:-1]):
        head = Node(int(val), head)
        
    return head
