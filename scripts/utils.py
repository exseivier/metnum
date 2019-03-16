#
# Module
# utils.py
#   /* Utils module for numeric method approaches */
# Version 1.1
#####

import math

######################
###    CLASSESS    ###
######################

class SDO(object):
    """
        An object class of synthetic division for the double synthetic division
        method to find the rational root of a polynomial rational equation.
    """
    alone = None
    rrs = None
    first = None
    second = None
    fourth = None
    fifth = None
    def __init__(self, alone, rrs):
        """(CLASS->SDO, FLOAT, ARRAY[FLOAT]) -> SDO
            INITIALISER
        """
        self.alone = alone
        self.rrs = rrs
        self.first = [str(0) for x in xrange(len(rrs))]
        self.third = [str(0) for x in xrange(len(rrs)-1)]
        self.second = list(self.first)
        self.fourth = list(self.third)
        self.first[1] = str(self.alone)
        self.third[1] = str(self.alone)

    def __str__(self):
        """
            PRINT FUNCTION
        """
        self.first = [str(x) for x in self.first]
        self.second = [str(x) for x in self.second]
        self.third = [str(x) for x in self.third]
        self.fourth = [str(x) for x in self.fourth]
        return str(self.alone) \
                + "\t|" \
                + "\t".join([str(x) for x in self.rrs]) + "\n" \
                + "\t" \
                + "|" + "\t".join(self.first) \
                + "\n---------------------------------------------------" + "\n" \
                + "\t" + "|" + "\t".join(self.second) + "\n" \
                + "\t" + "|" + "\t".join(self.third) + "\n" \
                + "---------------------------------------------------" + "\n" \
                + "\t" + "|" + "\t".join(self.fourth) + "\n" \

    def computeDSD(self):
        """
            Computes the double synthetic division to find the positive root
            for a polynomial equation.
        """
        for i in xrange(1, len(self.rrs)):
            self.second[i] = float(self.rrs[i]) + float(self.first[i])
            self.second[i] = round(self.second[i], 4)
            if i < len(self.rrs) - 1:
                self.first[i+1] = self.second[i] * float(self.alone)
                self.first[i+1] = round(self.first[i+1], 4)
                self.fourth[i] = float(self.second[i]) + float(self.third[i])
                self.fourth[i] = round(self.fourth[i], 4)
            else:
                pass
            if i < len(self.rrs) - 2:
                self.third[i+1] = self.fourth[i] * float(self.alone)
                self.third[i+1] = round(self.third[i+1], 4)
            else:
                pass

    def getR(self):
        """
            Returns the Ro
        """
        return self.second[-1]

    def getRast(self):
        """
            Returns the Ro asterisk
        """
        return self.fourth[-1]

    def next(self):
        """
            Calculates the Next step in Double synthetic division method.
        """

        alone = self.alone - round((float(self.getR()) / float(self.getRast())), 4)
        self.alone = round(alone, 4)
        self.first[1] = str(self.alone)
        self.third[1] = str(self.alone)

    def Result(self):
        """
            Returns the positive root for a polynomial equation using the
            double synthetic division.
        """
        return self.alone


def pop(array):
    """(ARRAY) -> pop(ARRAY - 1)
    Pops the ARRAY and returns the last element and eliminates it
    from original array
    """
    return array[-1], array[:-1]

def postfixeval(fun_str, value):
    """(STR, FLOAT) -> FLOAT
    Evaluates the function in postfix notation fun_str, assigns the value to
    the variable and returns the result
    """
    fun_str = fun_str.split("|")
    result = []
    for element in fun_str:
        # // Binary operations
        if element in ["+", "-", "*", "/", "p"]:
            B, result = pop(result)
            A, result = pop(result)
            if element == "+":
                result.append(float(A) + float(B))
            elif element == "-":
                result.append(float(A) - float(B))
            elif element == "*":
                result.append(float(A) * float(B))
            elif element == "/":
                result.append(float(A) / float(B))
            elif element == "p":
                result.append(float(A) ** float(B))
            else:
                pass
        # // Unary operations
        elif element in ["sin", "cos", "tan", "neg"]:
            B, result = pop(result)
            if element == "sin":
                result.append(math.sin(float(B)))
            elif element == "cos":
                result.append(math.cos(float(B)))
            elif element == "tan":
                result.append(math.tan(float(B)))
            elif element == "neg":
                result.append(float(B) * -1)
            else:
                pass
        # // Reserved variable words
        elif element in ["X", "Y", "Z", "W"]:
            result.append(value)
        else:
            result.append(element)

    return float(result[0])


def isnum(str):
    """(STR) -> BOOL
    Returns True or False depending on if str can be converted to number or not.

    """
    try:
        float(str)
        return True
    except Exception:
        return False


def rationaleroots(fun_str):
    """(STR) -> ARRAY[FLOAT]
    Returns the possible rationale roots of a polinomial equation
    using a numerical approach.

    """
    # // rrs = rationale roots
    fun_str = fun_str.split("|")
    fun_str = fun_str[::-1]
    length = len(fun_str)
    rr = []
    signs = []
    i = 0
    while i < length:
        if fun_str[i] in ["X", "Y", "Z", "W"]:
            if i == length-1:
                rr.append("1")
                i += 1
            else:
                i += 1
                if isnum(fun_str[i]):
                    rr.append(fun_str[i])
                    i += 1
                else:
                    rr.append("1")
                   # i += 1
        elif fun_str[i] == "p":
            i += 2
        elif isnum(fun_str[i]):
            rr.append(fun_str[i])
            i += 1
        elif fun_str[i] in ["-", "+"]:
            signs.append(fun_str[i]+"1")
            i += 1
        else:
            i += 1
    if len(rr) == len(signs)+1:
        signs.append("+1")
    else:
        pass
    rr = [float(x) for x in rr]
    signs = [int(x) for x in signs]
    rr = [a*b for a,b in zip(rr, signs)]
    return rr[::-1]



