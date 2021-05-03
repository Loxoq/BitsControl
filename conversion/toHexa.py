#!/usr/bin/python
def toHexa(x):

    """
    This function convert a number from base2 (0b), 8(0o), 10 to base-16(0x).
    In order the function to work correctly, add the correct prefix if the number's base isn't 10.
    
    Parameters:

        x : The number to be converted

    Out : The x number in its hexadecimal form 
    """

    y = None

    #We convert x as a string to check its base
    leNombre = str(x)
    decalage = 0  #Will be useful in case the number is a negative one

    try:

        print("The number to convert :", x, end='\n')

        #We split each number composing x in a list
        numberTypeCheck = [ch for ch in leNombre]


        #We check if the number has a decimal part
        try:
            point = numberTypeCheck.index('.')
            dec = True

        except:
            
            dec = False

        if numberTypeCheck[0] == '-':

            decalage = 1

        #=== Is the number not in base-10 ?
        if numberTypeCheck[0+decalage] == '0':


            #=== Is the number in base-2 ?
            if numberTypeCheck[1+decalage] == 'b' :

                if dec == True:
                    
                    #We divide the number in two part to convert it

                    intPart = numberTypeCheck[:point]
                    decPart = numberTypeCheck[point+1:]

                    #Each part is converted to base10

                    intPart = int(intPart, base = 2)
                    decPart = int(decPart, base = 2)

                    #Then the parts are converted to base-16
                    intPart = hex(intPart)
                    decPart = hex(decPart)

                    #Pour que le nombre soit correctement affiché, on retire la partie "0x" de la décimale
                    decPart = decPart[2:]

                    y = intPart + '.' + decPart

                else:

                    #To convert an integer part in base-10, we convert the number from RIGHT to LEFT

                    number = int(x , base=2)
                    y = hex(number)


            #=== Is the number in base-8 ?
            elif numberTypeCheck[1+decalage] == 'o' :

                if dec == True:
                    
                    #We divide the number in two part to convert it

                    intPart = numberTypeCheck[:point]
                    decPart = numberTypeCheck[point+1:]

                    #Each part is converted to base10

                    intPart = int(intPart, base = 8)
                    decPart = int(decPart, base = 8)

                    #Then the parts are converted to base-16
                    intPart = hex(intPart)
                    decPart = hex(decPart)

                    y = intPart + '.' + decPart

                else:

                    number = int(x , base=8)
                    y = hex(number)

            
            elif numberTypeCheck[1]=='x':

                print("The number you are trying to convert is already in base-16.")

                return x
                    
            
        #The x parameter MAY be already a base-10 number
        elif dec == False: #If there's no decimal point, then the whole number can be directly converted

            try:

                y = hex(x)

            #If there is an error ==> x is not a number type
            except:

                print("You can't call this function with an effective parameter that is not a valid number form.")
        
        elif dec == True:
            
            try :

                #We divide the number in two part to convert it
                firstP = numberTypeCheck[:point]
                secP = numberTypeCheck[point+1:]

                #For the moment I use two for loop to concatenate the elements of firstP & secP arrays, a cast to a int type can't be done otherwise
                #The two String that will result from the concatenation of the two arrays
                pEntiere = ""
                pDec = ""

                for i in firstP:

                    pEntiere += i
                
                for j in secP:

                    pDec += j

                #We cast the two String to int type
                pEntiere = int(pEntiere)
                pDec = int(pDec)

                #Then the parts are converted to base-16
                intPart = hex(pEntiere)    
                decPart = hex(pDec)

                #A thing to remember with the hex() python method is that a "Ox" is added at the beginning, which is quite annoying in our case

                y = intPart + '.' + decPart[2:]

            
            except:

                print("You can't call this function with an effective parameter that is not a valid number form.")


    #We insure the code doesn't bug if the function is called with a string parameter
    except:

        print("ERROR - Can't convert this number in base-16. Please refer to the manual")
        #help()

    return y