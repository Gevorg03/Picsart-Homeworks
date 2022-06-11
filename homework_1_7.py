def pow(base, exp):
    #Consider, that exp can be negative,and when base = 0 exp < 0 is senseless
    
    res = 1
	  count = 0
  
	  if exp == 0:
	      return 1
	  if base == 0 and exp < 0:
	      return None  
	    
	  while count < abs(exp):
		    res = res * base
		    count = count + 1
	
	  if exp > 0:	
	      return res
	  return 1/res 
  
base = 5
exp = -2
print(f"""{base} ^ {exp} =""",pow(base,exp))
