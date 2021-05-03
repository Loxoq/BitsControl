#!/usr/bin/python
from complementUnity import complementUnityEnc
from toBin import toBin
from toOct import toOct
from toHexa import toHexa

def twoComplementEnc(x, base, n):
    """
    Give the two complement of a number.
    
    Parameter :
        
        x : The number of which the two complement will be returned
        base: The base of the number
        n : The length (or the number of bits) of the complement returned
    
    Out : The two complement of the number  
    """
    
    bases = [2, 8, 10, 16]
    twoCompl = None

    #We insure the base is correct
    if base in bases:

        complUnity = complementUnityEnc(x, base, n)

        #There is no error raised in complementUnityEnc atm, so we just check if complUnity isn't None

        if complUnity != None :

            complUnity = int(complUnity, base) #We need to add 1 to the complement of unity to get the two-complement, we simply add 1 to the base-10 value

            complUnity += 1

            #We convert the number in the base wanted before returning it
            if base == 2 :

                twoCompl = toBin(complUnity)
            
            elif base == 8 :

                twoCompl = toOct(complUnity)
            
            elif base == 10 :

                twoCompl = toHexa(complUnity)

            else :

                twoCompl = complUnity
        
        else :

            print("twoComplement - Error : Invalid complement to unity form.")
            return twoCompl
    
    else :

        print("twoComplement - Error : The base entered is incorrect. Returned None")
    
    return twoCompl