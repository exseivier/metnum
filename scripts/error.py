#
# Module
# error.py
# Numeric methods
###
#

def abser(x, xa):
    """(FLOAT, FLOAT) -> FLOAT
    Returns the absolute error between x and xa: e = |x - xa|

    """
    return abs(x - xa)

def reler(x, xa):
    """(FLOAT, FLOAT) -> FLOAT
    Returns the relative error between x and xa: re = |(x - xa) / x|

    """
    return abs((x - xa) / x)

