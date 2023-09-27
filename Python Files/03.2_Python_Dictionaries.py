'''
Another common data structure are Dictionaries. 

These structures store data in a mutable/changeable format using key/value pairing. 
Other data structures can only hold a single value (think of a list, only one value can
be in the [1] spot) but dictionaries can hold multiple values under the same key.

Keys can not be duplicated, but we can have duplicate values.
Think of stocking items in a store. We only want one of each category but could
have multiple copies of the same item.

The key:value notation shows what piece of data is stored under each key.

my_dictionary = {key_1: 'car', key_2: 'boat', key_3: 'plane'}

If we access the whole dictionary -- print(my_dictionary), we'll see the 
entire listing of key:value pairings printed. Being able to access specific values
based on a key means we can move through large amounts of data.

Resources:
- https://www.w3schools.com/python/python_dictionaries.asp
- https://www.geeksforgeeks.org/python-dictionary/
'''

def main():
    '''
    This short introduction to the dictionary data structure will walk you through
    some of the basics you'll need to start working with them. 

    We'll go over:
    - creating a dictionary
    - accessing the values in a dictionary using its key
    - adding a key:value pair
    - removing a key:value pair
    - adding a value to a specific key
    - removing a value to a specific key
    '''

if __name__ == '__main__':
    main()