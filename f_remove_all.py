def remove_all(data, value):
    #delete the elements, that are equal in value
   
    if value not in data:
        raise ValueError("data.remove(x): x not in list")
    while value in data:
        data.remove(value)
    return data
    
print(remove_all([1, 2, 3, 4, 1, 4], 5))
