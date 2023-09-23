'''
A big part of programming is asking if certain conditions
are True or False. It's making a decision based on the data. 

Flow Control can be used to make our programming more robust, we
can modify how we send data based on the answers. It's just like 
choosing your path when you have a fork in the road.

A common use for flow control are within our loops, and for
input validation. We know that certain data types don't mix -- 
so if we check it we can change how our computer responds to the 
user when they enter a word when we want a number.

Incorrect password prompts are an easily recognizable use of flow control.

We can break up flow control into three statements.
- If (If true, do this)
- Elif (Or, if this makes it true do this)
- Else (If none of it works, do this as a final step)

These are often paired with Python Logical Operators
- AND (both need to be true)
- OR (either can be true)
- NOT (reverses the logic -- typically checking it's false)

They allow us additional checks on our data as we use them in statements.
There are more ways to add additional checks which you'll use as you progress as a programmer.



Resources:
- https://www.w3schools.com/python/gloss_python_else.asp
- https://www.geeksforgeeks.org/python-if-else/
- https://www.w3schools.com/python/python_operators.asp
'''

def main():
    '''
    Change the variables below to get the right prompt to print out.
    You should follow the if/elif/else statements to see where the variable is following.
    '''
    correct_number = 
    
    if (correct_number ** 2) == 10:
        print("That's not right!")
    elif ((correct_number // 2) < 5) and ((correct_number // 2) > 3):
        print("That's it!")
    else:
        print("You should keep trying")

if __name__ == '__main__':
    main()