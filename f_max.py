def max(data):
    #return the maximum element of list
    
    i = 1
    max = data[0]
    while i < len(data):
        if max < data[i]:
            max = data[i]
        i += 1    
    return max
    
print(max([14, 20, 99, 30, 5, 8]))  
