import math
from decimal import Decimal
from numpy import isnan

def check_is_equal(a,b,atol=10e-7, rtol=10e-7,is_equal=False):
    if is_equal and isnan(a) and isnan(b):
        return True
    return math.fabs(a - b) <= (atol + rtol * math.fabs(b))
