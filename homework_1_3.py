def three_num_max(num1,num2,num3):
    #Find two max numbers and calculate the sum of that numbers sqaures
    
    if num1 > num2:
        num1,num2 = num2,num1
    if num1 > num3:
        num1,num3 = num3,num1
    return num2**2 + num3**2
print("Sum =",three_num_max(3,4,7))
