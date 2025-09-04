def puissance(a,b):
  if not type(a) is int:
     raise TypeError("Only integers are allowed")
  if a== 0 and b < 0:
     raise Exception("mettre supérieur à 0")
  else:
     result = 1
     if b < 0: 
       for _ in range(-b):
         result *= a
       return 1/result
     else:
       for _ in range(b):
        result *= a
       return result



