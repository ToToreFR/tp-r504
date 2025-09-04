import pytest
import fonctions as f
import test_exc_1

def test_1():
     assert f.puissance(2,3) == 8
     assert f.puissance(2,2) == 4

def test_2():
     assert f.puissance(-1,2) == 1
     assert f.puissance(-1,3) == -1
     assert f.puissance(-1,-1) == -1
     assert f.puissance(-1,-2) == 1
     assert f.puissance(-2,-1) == -0.5
     assert f.puissance(2, 2) == 4
     assert f.puissance(1,1) == 1
     assert f.puissance(0,-1) == 0
     assert f.puissance(0,2) == 0
