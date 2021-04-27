#!/usr/bin/python

def evenParityCheck(bin):
    """
    This function perform an even parity check of a binary number, and add the parity bit at the end of the number.

    Parameter :

        bin : A binary number on which an even parity check will be done. The number must begin by "Ob".
    
    Out : The number put as a parameter with a parity bit.
    """
    
    ret = "null"

    #We check the format of bin
    if bin[1] == 'b' :
    
        leBin = bin[1:] #We remove the "Ob" identifier part of the parameter

        count = leBin.count('1')

        if count%2 == 0 :

            #There is an even number of 1, so the parity bit will be 0
            parityBit = '0'
        
        else :

            #There is an odd number of 1, so the parity bit will be 1
            parityBit = '1'
        
        ret = bin + parityBit
    
    else :

        print("Please use a binary number parameter of the form \"0b...\". ")
    
    return ret