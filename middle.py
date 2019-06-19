def middle():
    even = False
    if self.size % 2 == 0: // even
        mid_ind = self.size / 2
        even = True
    else: 
        mid_ind = (self.size // 2) + 1
    
    counter = 1
    node = self.head

    while counter != mid_ind:
        counter += 1
        node = node.next 
    
    if even: 
        first = node.data
        second = node.next.data
        return (first, second)
    
    return node.data
