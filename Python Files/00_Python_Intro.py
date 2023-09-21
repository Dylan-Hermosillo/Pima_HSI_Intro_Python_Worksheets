'''
Welcome to this introductory boot-camp for learning the Python programming language!

We'll be going over some of the basics that will carry you into your first few courses here at Pima.

We'll be looking at:
- Pseudocode
- Data Types
- Variables
- Loops
- Functions
- Object Oriented Programming

Each of these python files will be follow-along programming projects written in pseudocode.

Pseudocode is what a lot of your projects will look like in your courses.
They're basic english instructions that provide a direction for your python programming.

A quick example of this would be

Pseudocode:
1) Make a variable called classroom_a to represent the number of students and set the value to 15
2) Make a variable called classroom_b and set the value to 25
3) Using the two classroom variables, add them together and save it as total_students

You then use these instructions to write your python code

Python Code:
classroom_a = 15
classroom_b = 25
total_students = classroom_a + classroom_b

Let's talk about some of the code you'll see below. 

First, we have def main(): -- This is defining our main function, which in basic terms is how we execute/start our code.
We'll be learning more about functions later but I remember seeing it when I was first starting and no one
bothered to explain it. 

In our def main(), we can see everything is indented one tab in. Python is picky about indentation and when writing
our function body they need to be indented. We'll be doing some small editing to the main program below.

Finally, we have what's known as the main guard. 
if __name__ == '__main__'
    main()

The main guard is useful when you start having multiple files that contain main functions. It lets
your computer execute the main function when you run the Python script instead of when you import into 
another file. It might be confusing now but think of it as part of a template to your Python file, you'll 
usually always have it.
'''

def main():
    '''
    Let's review some basic data types, and then create a few variables

    integers (int): are numeric data types representing non-decimal values
    floats (float): are numerical data types representing decimal values
    strings (str): are character data types we use for words; strings of characters
    boolean (bool): are values that represent true or false logic

    Variables are ways to store information, much like how we use in math problems.
    You can set the variable name and have it equal the data type you need it to be.

    I.e:

    integer_variable = 10
    float_variable = 1.2341
    string_variable = 'This is a string of characters'

    Variables are great ways to use the same data repeatedly without making mistakes.
    They also make it easy to update code -- as changing one variable used 500 times is easier than
    changing 500 lines of code.

    Now it's your turn! Use the pseudocode comments below to complete the program.

    '''
    # Let's add some integers together to get the sum of two numbers!
    # Make two variables below called number1 and number2, assign them some integer values and let's get their sum.

    # We'll start the first one for you!
    number1 =  
    # Now make the number2 variable below

    print("*************")
    print("The sum is:", (number1 + number2))
    print("*************")

    
    

if __name__ == '__main__':
    main()
