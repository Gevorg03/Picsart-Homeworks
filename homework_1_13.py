#fast_pow with iterative

def pow_iterative(base,exp):
    degree = base
    while exp > 1:
        base*=degree;
        exp-=1
    return base    
print("Result =",pow_iterative(3,5))        
