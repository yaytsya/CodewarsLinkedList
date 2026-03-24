def stringify(node):
    values = []
    
    while node is not None:
        values.append(str(node.data))
        node = node.next
        
    values.append("None")
    
    return " -> ".join(values)
