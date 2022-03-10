# test_bond.py

from bond import *
import pandas as pd

def test_bond(bond):
    assert isinstance(bond, Bond)

def test_get_term_to_maturity(bond):
     assert isinstance(bond.get_term_to_maturity(), int)
     assert bond.get_term_to_maturity() > 0

def test_get_coupon_dates(bond):
    assert isinstance(bond.get_coupon_dates(), list)

def test_get_price(bond, ytm):
    assert isinstance(bond.get_price(ytm), float)

def test_get_cashflows(bond, ytm):
    assert isinstance(bond.get_cashflows(ytm), pd.DataFrame)

def test_get_current_yield(bond, ytm):
    assert isinstance(bond.get_current_yield(ytm), float)