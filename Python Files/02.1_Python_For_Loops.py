'''
Loops can seem complicated but once we break them
down and think about how and why we use them it'll 
hopefully clear up the fog.

Loops are used when we need to repeat a task until we meet a condition.

All loops require different things For loops need one:
- Something to iterate over (a data structure, string, or range of numbers)

For loops are used for "iterating" over something that has a sequence.
We'll learn later that most data structures (lists, arrays and dictionaries)
are ways to store information that we can iterate through a loop. 
Many things are iterable, including strings or even just ranges of numbers.

Here's a quick reminder of the composition of a for loop:

for x in ____:
    do this

The 'x' is a variable that stands for each iteration.
Meaning if we're iteraing through a string, the x will represent
each letter as it goes through the loop.

We can name that 'x' anything we want;

our_word = 'Dog'
for letter in our_word:
    print(letter)

If we don't have an iterable object but a certain number of steps we can use a number:

for i in range(3)
    print(i)
    
Some good resources:
- https://www.w3schools.com/python/python_for_loops.asp
- https://www.geeksforgeeks.org/loops-in-python/
- https://automatetheboringstuff.com/2e/chapter2/
'''

def main():
    '''
    Let's practice iterating through a few loops.
    We'll create the variables and you finish the for loops.
    '''
    my_list = ['dog', 'cat', 'hedgehog', 'snake']
    my_string = 'Wicket'
    number_for_range = 10

    # Let's print all the animals in a list
    for animal in :# what variable goes here?
        print()

    # Now try writing your own to print each letter in our string.
    for 

    # Finally, print each number from 0 - 10 using our number_for_range variable
    for 

if __name__ == '__main__':
    main()