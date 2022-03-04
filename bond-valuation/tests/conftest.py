import pytest
import random 
import datetime
from bond import *

@pytest.fixture
def bond():
    bond = Bond(
            par=random.randint(0,10e12), # Random par between 0 and 1 000 000 000 000 (0 qnd 10e12)
            coupon=random.random(), # Random coupon between 0,00 % and 100,00 % (0 and 1)
            frequency=random.choices([1, 2, 4, 12]), # Random frequency in 1, 2, 4 or 12 months
            maturity=(datetime.datetime.now() + datetime.timedelta(days=random.randint(0,36500))).strftime("%Y-%m-%d") # Random date in the next 100 years (100*365 days)
    )
    return bond
