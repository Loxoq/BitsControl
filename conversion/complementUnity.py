#!/usr/bin/python
from toBin import toBin
from toOct import toOct
from toHexa import toHexa

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

    complU = None
    
    #We insure the base is correct and the number is a negative one
    if base in bases :

        #A conversion is needed only if the number is a negative one
        if str(nb)[0] == '-' :

            #The parameter n is important to be checked : a base-8 number can't be represented on less than 3 bits.
            #Same thing for base-16 number : they can't be represented on less than 4 bits

            if base == 8 and n < 3 :

                n = 3
                print("Careful, a base-8 number can't be represented on less than 3 bits. n has been set on 3 by default")
            
            elif base == 16 and n < 4:

                n = 4
                print("Careful, a base-8 number can't be represented on less than 4 bits. n has been set on 4 by default")
            
            #Note : We are working with absolute values, so there is no need to handle the number's sign
            #To make this conversion & the calculations easier, I will work with integers in base 10 + the abs() function

            theNb = int(nb ,base)   #We put the number in base10
            theNb = abs(theNb)      #We take its absolute value

            toSubstract = '1' * n
            toSubstract = int(toSubstract, 2)
            
            #Ex : nb = -3, n = 4
            #3 = (11)2
            #ComplU = 1111 - 0011 = 1100
            complU = toSubstract - theNb

            #We now reconvert the complement in the right base (and we add the right prefix)

            if base == 2:

                return toBin(complU)
            
            elif base == 8:

                return toOct(complU)
            
            elif base == 16:

                return toHexa(complU)
            
            else:

                return complU
        
        else : 

            print("There is no point in giving the complement to unity of a positive number, because it is exactly the same value. The same value is returned.")
            complU = nb
            return complU
    
    else:

        print("complementUnityEnc - Error : \nA number in this base can't be converted. This method can only give the Unity complement of bases 2 8 10 or 16.")
        return complU