# test_bond.py

from bond import *

def test_bond():
    b = Bond(par=1000000, coupon=0.1, frequency=12, maturity="2031-12-31")
    assert True
