'''
Functions are another way to make easily reusable code.
They are blocks of code you can call later to perform their function.

We start by defining a function, along with any parameters.

def my_function(parameter_1, parameter_2):
    print(parameter_1)
    print(parameter_2)

Later, we call the function and use arguments where the parameters are.
These arguments take the place of the parameters when the code is ran.

my_function('I am argument 1', 'I am argument 2')

Above we've called our function and passed two strings. These strings
will take the place of our parameter_1 and parameter_2 spots.

Functions offer a way to do the same steps repeatedly. With the benefit of only
having to change the function definition to edit every function we use.

Imagine having a function to work a certain math equation. Later we find out
we got the formula wrong -- instead of fixing it everywhere in our program, we 
only have to change the function definition.

We've seen the main function in all our programs.
It works like any other function, but we use that one as a starting point for our code.

In general, we'll define all our functions separately and use them within out main program.

For example;

def function_1():
    code goes here

def function_2():
    code goes here

def main():
    function1() calling function's in main
    function2() 
'''
# Let's work on defining a few functions
# Let's start with the sum_two_numbers that takes two integers and adds them together
def sum_two_numbers(number_1, number_2):
    print('The sum is:', (number_1 + number_2))

# Now follow the same format to finish the remaining two!
# product_two_numbers

# dividing_two_numbers

def main():
    sum_two_numbers(8, 12)
    product_two_numbers(12, 10)
    dividing_two_numbers(9, 171)


if __name__ == '__main__':
    main()