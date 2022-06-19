def map3(func, data1, data2, data3):
    #Calculate the sum of list's members
    
    lst = []
    for i in range(len(data1)):
        res = func(data1[i], data2[i], data3[i])
        lst.append(res)
    return lst    
    
def sum(num1, num2, num3):
    return num1 + num2 + num3

data1 = [1, 2, 3]
data2 = [10, 20, 30]
data3 = [100, 200, 300]
print(map3(sum, data1, data2, data3))    
