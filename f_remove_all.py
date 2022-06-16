def remove_all(data,value):
    #delete the elements, that are equal in value
    
    i = 0
    while i < len(data):
        if data[i] == value:
            data.remove(value)
        i+=1    
            
    return data
print(remove_all([1,2,3,4,1,4],4))  
