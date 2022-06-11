def sum_of_two_num(num1,num2):
    #Calculate the sum of integers from num1 to num2
    
    sum = 0
    if num1 < num2:
        while num1 < num2:
            sum+=num1
            num1+=1
        return sum 
    
    while num1 > num2:
        sum+=num1
        num1-=1
    return sum 
  
print("Sum =",sum_of_two_num(8,5))
