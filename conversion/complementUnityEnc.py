#!/usr/bin/python
from .toBin import toBin
from .toHexa import toHexa
from .toOct import toOct

def complementUnityEnc(nb, base, n):
    """
    This function return the complement to unity of an integer negative number.

    Parameters:

        nb : The number of which the complement to unity will be given
        base : The base of the number
        n : The length (or the number of bits) of the complement returned
    
    Out : The complement of unity
    """
    
    bases = [2, 8, 10, 16]
    prefix = {2: "0b", 8 : "0o", 10 : "", 16 : "0x"}

    complU = "Null"
    
    #We insure the base is correct and the number is a negative one
    if (base in bases) and (str(nb)[0] == '-') :

        #Note : We are working with absolute values, so there is no need to handle the number's sign
        #To make this conversion & the calculations easier, I will work with integers in base 10 + the abs() function

        theNb = int(nb ,base)
        theNb = abs(theNb)

        toSubstract = '1' * n
        toSubstract = int(toSubstract, 2)
        
        #Ex : nb = -3, n = 4
        #3 = (11)2
        #ComplU = 1111 - 0011 = 1100
        complU = toSubstract - theNb

        #We now reconvert the complement in the right base

        if base == 2:

            return toBin(prefix.get(base) + complU)
        
        elif base == 8:

            return toOct(prefix.get(base) + complU)
        
        elif base == 16:

            return toHexa(prefix.get(base) + complU)
        
        else:

            return complU
    
    else:

        print("A number in this base can't be converted. This method can only give the Unity complement of bases 2 8 10 or 16.")
        print("There is no point in giving the complement to unity of a positive number, because it is exactly the same value.")
        return complU

