
# coding: utf-8

# In[ ]:

"""
While taking a class on the culture of China, you have learned about the Chinese zodiac in which people fall into 1 of 12 categories, depending on the year of their birth. The categories, numbered 0 to 11, correspond to the following animals:

(0) monkey
(1) rooster
(2) dog
(3) pig
(4) rat
(5) ox
(6) tiger
(7) rabbit
(8) dragon
(9) snake
(10) horse
(11) goat

Those who believe in this zodiac think that the year of a person's birth influences both their personality and fortune in life.

Your task is to build a program that will ask a user for their birth year and tell them their zodiac sign.  If the user does not enter a number that can be interpreted as a year then an error message must be shown and the user given another chance.  If the user types "quit" then the program halts.

For extra credit: save each year that is input to a file and print a chart showing how many of each type or animal have been returned.

To find your zodiac sign, divide the year of your birth by 12. The remainder then determines your sign. For example: The remainder when we divide 1985 by 12, is 5; therefore, a person born in 1985 is an ox according to the Chinese zodiac.
"""


# In[ ]:

# There should be a description here of what is in this code

# ZodiacSetup will all the opening, loading, and closing of files/data. 
# It will return ZodiacListTemp
def ZodiacSetup():  
    # Open the zodiac description file
    ZodiacText = open('zodiacDescriptions.txt', 'r')
    
    # Read the file. Make a list with each line of the file as a list item.
    ZodiacListTemp= []
    for animal in ZodiacText:
        if animal != '\n':
            ZodiacListTemp.append(animal)
        
    # Close the file as soon as we're done with it
    ZodiacText.close()
    
    return ZodiacListTemp  # return ZodiacList from the function


# ZodiacCalculation will collect a birth year and determine the Chinese zodiac animal and then display it.  
# It will return 
def ZodiacCalculation():
    
    birthYear = input("What year were you born? ")  
    
    # Ask the user for input
    try:
        birthYear = int(birthYear)    
        # Do some fancy figuring stuff out (little bit of math)
        #  % is the "modulus" operator; gives remainder
        # John lied to us and gave us the wrong list
        # to fix this, we need to offset birthyear by 4
        ZodiacIndex = (birthYear - 4) % 12      

        # Tell user the result
        print("Your Chinese Zodiac Animal is a", ZodiacList[ZodiacIndex])       
        
    except ValueError:
        print("You did not provide a year in the form of an integer", '\n')
        
    return birthYear         
    
    
# Repeat 
ZodiacList = ZodiacSetup()

birthYear = 0
while type(birthYear) is int:
    birthyear = ZodiacCalculation()
       


