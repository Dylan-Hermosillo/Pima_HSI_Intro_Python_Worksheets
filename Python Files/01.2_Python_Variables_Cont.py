'''
Let's enter a few variable commands to fix this program
'''

def main():
    # Fix the program below by creating the variables being called in the print statement

    # We'll need three variables to fix the first one. Here's the start
    dog_name = ''

    print("The dog's name is", dog_name, "\nTheir breed is", dog_breed, "\nand their age is", dog_age)

    #-----------------------
    print('-' * 20) # This is decorative to separate stuff in the terminal
    #-----------------------

    # We'll need to use some type casting to fix this next one. 
    # It looks like we used strings when collecting the data but we're trying to use numbers.
    number1 = '3'
    number2 = 4
    print('Number 1 raised to the power of Number 2 is:', (number1 ** number2)) # add some type casting on this line


if __name__ == '__main__':
    main()