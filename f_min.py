def min(data):
    #return the minimum element of list
    
    i = 1
    min = data[0]
    while i < len(data):
        if min > data[i]:
            min = data[i]
        i += 1    
    return min
    
print(min([14, 20, 99, 30, 5, 8])) 
