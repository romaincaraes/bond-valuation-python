# test_bond.py

from bond import *
import pandas as pd

def test_bond(bond):
    assert isinstance(bond, Bond)

def test_get_term_to_maturity(bond):
     assert isinstance(bond.get_term_to_maturity(), int) and bond.get_term_to_maturity() > 0

def test_get_coupon_dates(bond):
    assert isinstance(bond.get_coupon_dates(), list)

def test_get_price(bond):
    assert isinstance(bond.get_price(0.1), float)

def test_get_cashflows(bond):
    assert isinstance(bond.get_cashflows(0.1), pd.DataFrame)

def test_get_current_yield(bond):
    assert isinstance(bond.get_current_yield(0.1), float)