#
# Module
# algtranseq.py
#   /* Numeric approaches to solve algebraic and transcendent equations */
# Version 1.1
#####

import utils as UT

def bisection(fun_str, x1, x2, precision):
    """(STR, FLOAT, FLOAT) -> FLOAT
    Resturns a numeric approach using the bisection method.
    Recursive method
    """
    x1 = float(x1)
    x2 = float(x2)
    # // Eval F(x1) & F(x2)
    Fx1 = UT.postfixeval(fun_str, x1)
    Fx2 = UT.postfixeval(fun_str, x2)
    # // Base case
    if round(x1, precision-1) == round(x2, precision-1):
        return round((x1 + x2) / 2, precision)
    else:
        pass
    if Fx1 * Fx2 < 0:
        xm = (x1 + x2) / 2
        Fxm = UT.postfixeval(fun_str, xm)
        if Fx1 * Fxm < 0:
            x2 = xm
        else:
            x1 = xm
        # // RECURSE
        return bisection(fun_str, x1, x2, precision)

    else:
        if Fx1 < Fx2:
            print "[ERROR!] - Not in a local minimum or maximum; Going upstears"
        else:
            print "[ERROR!] - Not in a local minimum or maximum; Going downstears"


def fixedpoint(fun_str, x1, precision):
    """(STR, FLOAT, INT) -> FLOAT
    Returns a numeric aproach of a continue or trascendenced function using the
    fixed point method. G(x) = fun_str argument
        F(x) = 0
        Summing x to both sides
        F(x) + x = x
        G(x) = F(x) + x
        x = G(x)
        x = G(xn-1)
    """
    x1 = float(x1)
    x = UT.postfixeval(fun_str, x1)
    while round(x1, precision) != round(x, precision):
        x1 = x
        x = UT.postfixeval(fun_str, x1)

    return round(x, precision)


def newrap(fun_str, dfun_str, xn, precision):
    """(STR, STR, FLOAT, INT) -> FLOAT
    Retruns the root using a numeric approach Newton-Raphson.
        Xn+1 = Xn - F(Xn) / F'(Xn)
        fun_str = F(Xn)
        dfun_str = F'(Xn)
    """
    xn = float(xn)
    x = xn - (UT.postfixeval(fun_str, xn) / UT.postfixeval(dfun_str, xn))
    while round(xn, precision) != round(x, precision):
        xn = x
        x = xn - (UT.postfixeval(fun_str, xn) / UT.postfixeval(dfun_str, xn))

    return round(x, precision)

def doublesynthdivision(fun_str, x0):
    """() -> 
    Returns the root of a algebraic equation of order n
    using a numeric approach.
        
        Xn+1 = Xn - (Rn / R*n)
        Rn = Residue of a synthetic double division of P(x)
        R*n = Residue of a synthetic double division of P'(X)
    """
    rr = UT.rationaleroots(fun_str)
    sdo = UT.SDO(x0, rr)
    sdo.computeDSD()
    print "[MESSAGE!] - First sdo"
    print sdo
    pivot = None
    while pivot != sdo.Result():
        pivot = sdo.Result()
        sdo.next()
        sdo.computeDSD()
        print sdo.Result()
    print "[MESSAGE!] - Final sdo"
    print sdo
    print "[MESSAGE!] - Resulted root"
    print sdo.Result()
    return sdo.Result()



