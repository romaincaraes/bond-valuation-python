# test_bond.py

from bond import *

def test_bond(bond):
    assert isinstance(bond, Bond)

def test_get_term_to_maturity(bond):
     assert isinstance(bond.get_term_to_maturity(), int) and bond.get_term_to_maturity() > 0

def test_get_coupon_dates(bond):
    assert isinstance(bond.get_coupon_dates(), list)
