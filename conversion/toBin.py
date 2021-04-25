#!/usr/bin/python
def toBin(x):

    """
    This function convert a number from base-8, 10, 16 to base-2.
    
    Parameters:

        x : The number to be converted

    Out : The x number in its binary form 
    """

    y = "Null"

    #We convert x as a string to check its base
    leNombre = str(x)
    decalage = 0  #Will be useful in case the number is a negative one

    try:

        print("The number to convert :", x, end='\n')

        #We split each number of x in a list
        numberTypeCheck = [ch for ch in leNombre]


        #We check if the number has a decimal part
        try:
            point = numberTypeCheck.index('.')
            dec = True

        except:
                    
            print("No decimal point.")
            dec = False

        if numberTypeCheck[0] == '-':

            decalage = 1

        #=== Is the number not in base-10 ?
        if numberTypeCheck[0+decalage] == '0':


            #=== Is the number in base-8 ?
            if numberTypeCheck[1+decalage] == 'o' :

                if dec == True:
                    
                    #We divide the number in two part to convert it

                    intPart = numberTypeCheck[:point]
                    decPart = numberTypeCheck[point+1:]

                    #Each part is converted to base10

                    intPart = int(intPart, base = 8)
                    decPart = int(decPart, base = 8)

                    #Then the parts are converted to base-2
                    intPart = bin(intPart)
                    decPart = bin(decPart)

                    #Pour que le nombre soit correctement affiché, on retire la partie "0b" de la décimale
                    decPart = decPart[2:]

                    y = intPart + '.' + decPart

                else:

                    number = int(x , base=8)
                    y = bin(number)


            #=== Is the number in base-16 ?
            elif numberTypeCheck[1+decalage] == 'x' :

                if dec == True:
                    
                    #We divide the number in two part to convert it

                    intPart = numberTypeCheck[:point]
                    decPart = numberTypeCheck[point+1:]

                    #Each part is converted to base10

                    intPart = int(intPart, base = 16)
                    decPart = int(decPart, base = 16)

                    #Then the parts are converted to base-2
                    intPart = bin(intPart)
                    decPart = bin(decPart)

                    #Pour que le nombre soit correctement affiché, on retire la partie "0b" de la décimale
                    decPart = decPart[2:]

                    y = intPart + '.' + decPart

                else:

                    number = int(x , base=16)
                    y = bin(number)

            
            elif numberTypeCheck[1]=='o':

                print("The number you are tryhing to convert is already in base-16.")

                return x
                    
            
        #The x parameter MAY be already a base-10 number
        elif dec == False:  #If there's no decimal point, then the whole number can be directly converted

            try:

                y = bin(x)

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

                #Then the parts are converted to base-2
                intPart = bin(pEntiere)    
                decPart = bin(pDec)

                #A thing to remember with the bin() python method is that a "Ob" is added at the beginning, which is quite annoying in our case

                y = intPart + '.' + decPart[2:]

            
            except:

                print("You can't call this function with an effective parameter that is not a valid number form.")


    #We insure the code doesn't bug if the function is called with a string parameter
    except:

        print("ERROR - Can't convert this number in base-16. Please refer to the manual")
        #help()

    return y