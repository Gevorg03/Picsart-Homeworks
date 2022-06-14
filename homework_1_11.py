#f is set
#f(n) = n, եթե n < 3
#f(n) = f(n - 1) + f(n - 2) + f(n - 3), եթե n >= 3

def f_recursive(n):
    if n < 3:
        return n
    return  f_recursive(n - 1) + f_recursive(n - 2) + f_recursive(n - 3)    
print("Result =",f_recursive(8))

def f_iterative(n):
    num1,num2,num3 = 0,1,2
    sum = 0
    if n > 3:
        while n >= 3:
            sum = num1 + num2 +num3
            num1,num2,num3 = num2,num3,sum
            n-=1
        return sum 
    return n
print("Result =",f_iterative(8))    




