def pop(data, i=None):
    #if exist ith member, delete, otherwise the delete the last member
    
    if i == None:
        el = data[len(data)-1]
        del data[len(data)-1]
        return el
    _el = data[i]    
    del data[i]    
    return _el   
        
print(pop([1, 2, 3, 4])) 
