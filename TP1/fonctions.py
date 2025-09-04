def puissance(a,b):
  if not type(a) is int:
     raise TypeError("Only integers are allowed")
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

def test_exc_1():
    with pytest.raises(Exception):
        puissance(0,-1)

