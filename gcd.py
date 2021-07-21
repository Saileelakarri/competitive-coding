def gcd(a,b):
    if a==0:
        return b
    else:
        if b>a:
            a,b=b,a
        return gcd(a%b,b)
    
        
        
        
    
