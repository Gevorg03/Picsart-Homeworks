def triple(data):
    #Calculate the cube of list members, add in a list and return the list
    
    res = []
    for num in data:
        res.append(num**3)
    return res    
print(triple([1, 2, 3, 4]))    
