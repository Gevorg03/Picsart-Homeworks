def pop(i):
    #if exist ith member, delete, otherwise the delete the last member
    
    lst = [1,5,12,4]
    if i == None:
        tmp = lst[len(lst)-1]
        del lst[len(lst)-1]
        return tmp
    _tmp = lst[i]    
    del lst[i]    
    return _tmp    
        
print(pop(2)) 
