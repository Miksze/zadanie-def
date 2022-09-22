def pali(a):
 #   x = a.lower()
    import re
    y = re.sub("[^a-zA-Z_0-9]", "", a.lower())
    return y == y[::-1]
   
    
print(pali("1Dom .od1"))