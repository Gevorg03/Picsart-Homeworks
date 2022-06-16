def remove_all(data,value):
    #delete the elements, that are equal in value
    
    size = len(data)
    i = 0
    while i < len(data):
        if data[i] == value:
            data.remove(value)
        i+=1   
    
    if(size == len(data)):
        raise ValueError("data.remove(x): x not in list")
    return data
print(remove_all([1,2,3,4,1,4],5))
