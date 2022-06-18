def contain(data,val):
    #is val contained in list or no?
    
    i = 0
    while i < len(data):
        if data[i] == val:
            return True
        i += 1
    return False   
    
print(contain([1, 2, 3, 4], 3))    
