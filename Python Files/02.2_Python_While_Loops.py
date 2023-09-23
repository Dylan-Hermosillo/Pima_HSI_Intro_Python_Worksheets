'''
While loops are used to do something until we meet a certain condition.

A common mistake with While Loops are entering infinite loops
that never exit. They'll keep repeating until our computers run out
of memory and crash.

A good way to check your loops are to remember that you need:
- A way in
- A way out

We set that by entering our condition when starting the loop,
and we make sure something in the body of the loop modifies it.

number_to_reach = 5

while(number_to_reach < 10):
    print('Our number is too small...')

Take a look and see how we enter the loop: We're checking
if our number is less than 10 -- which we know is True.
It'll then print the statement but since we never change that number,
we never exit the loop. 

while(number_to_reach < 10):
    print('Our number is too small...')
    print('Adding one....')
    number_to_reach = number_to_reach + 1 

Now we see that our number will keep increasing and eventually be 
equal to ten, escaping out of the while loop.

Some good resources:
- https://www.w3schools.com/python/python_while_loops.asp
'''

def main():
    '''
    Let's practice finding ways outside of while loops. 
    We'll set up a few below and you find ways to fix the code
    so we can meet our exit condition.
    '''
    number_to_match = 24
    string_to_match = 'saguaro'

    while number_to_match < 24:
        print("We haven't left yet!")
        # What should we add here to fix it?
    
    while string_to_match != 'roadrunner':
        print("That's not the right word")
        # What should we add here to fix it? 
        # Hint: we can do a few things; change the variable or take in a user's input...

if __name__ == '__main__':
    main()