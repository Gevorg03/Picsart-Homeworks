def reverse(data):
    #invert list
    
    i = 0
    while i < len(data)//2:
        data[i],data[len(data)-i-1] = data[len(data)-i-1],data[i]
        i += 1    
    return data
    
print(reverse([1, 2, 3, 4, 5, 6, 7])) 
