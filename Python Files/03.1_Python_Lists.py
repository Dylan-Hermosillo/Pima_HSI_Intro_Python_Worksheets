'''
Data Structures are one of the big concepts you need to grasp to
be a good programmer. They allow us to store, reuse and manipulate
large amounts of data.

One of the easiest to grasp are lists/tuples.
Often called arrays in other language, they are ways to store data sequentially; in order.
We access them through their index; the number that represents where they are in the list.
Starting with the number 0, we can pick which item we want by choosing a number.

The key differences between lists and tuples are whether they can be modified after creation.
Lists can be changed after creation -- you can add/remove values.
Tuples can not be change -- they are what's known as "immutable"

Lists/Tuples really are just containers, but knowing where data is makes it
easier to develop algorithms -- steps applied to a set of data.

We can make lists with brackets
my_list = []

Tuples with paranthesis
my_tuple = ()

Good Resources:
- https://www.w3schools.com/python/python_lists.asp
- https://www.w3schools.com/python/python_tuples.asp
- https://automatetheboringstuff.com/2e/chapter4/
'''

def main():
    '''
    Let's go over a few useful things to know when working with lists.
    We're going to:
    - Make a List
    - Access a specific element
    - Traverse/Iterate Over it
    - Append an Item
    - Remove an Item
    '''
    # We'll make the list for you to work with.
    plants = ['tree', 'flower', 'shrub', 'bush', 'crop', 'grass']

    # Let's access a specific element
    correct_element = # We need the shrub element -- how can we access it using an index?

    if correct_element == 'shrub':
        print('That\'s it!')
    else:
        print('We accessed', correct_element, 'try again!')

    # How can we print the entire list?
    # Try using a for loop since we're looping through an iterable

    for ___ in ___:
        print()
    
    # The append function is an easy way to add an element 
    # it's done through: my_list.append('New Item')
    # https://www.w3schools.com/python/ref_list_append.asp
    
    # Can you append the list and change the correct_element variable?
    plants.
    correct_element = # Now change the correct element to the last index
    
    if correct_element == 'cactus':
        print('That\'s it!')
    else:
        print('We accessed', correct_element, 'try appending!')

    # The pop function will remove the last item in a list.
    # We can remove the cactus we added by following:
    # my_list.pop()
    # if you add an index inside pop it will eliminate that value
    # my_list.pop(0) removes the first item
    
    plants.

    if plants[-1] == 'crop':
        print('You got it!')
    else:
        print('That\'s not quite it, what did you remove?')

if __name__ == '__main__':
    main()