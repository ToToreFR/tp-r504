def puissance(a,b):
  if not type(a) is int:
     raise TypeError("Only integers are allowed")
  else:
    result = 1
    for _ in range(b):
       result *= a
    return result if b < 0 else 1/results
