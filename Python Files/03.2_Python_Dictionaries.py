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

    # Let's create a dictionary! They use curly braces {}
    # Remember we use Key:Value to add information
    # Notice on the courses we're using a list, if we want multiple
    #   values in the same key we need them in their own container. 
    student_dict = {'student_Number': 123654, 'student_major': 'Programming',
                    'student_gpa': 3.5, 'student_courses': ['CIS129', 'MAT151']} 

    # We'll now access a few elements within the dictionary.
    # First, lets get the student's major
    print("Student's Major:",student_dict['student_major'])
    # What about their courses?
    print("Student's Courses:",student_dict['student_courses'])
    # What if we want to view just the first course?\
    # Notice we just index the list within the dictionary 
    print("Student's First Course:",student_dict['student_courses'][0])

    print('-----'*10)
    # Now let's add another category, their birthday.
    student_dict['student_birthday'] = '01/01/2000' # notice we just index the new key and add a value to it
    print('Updated Dictionary:',student_dict)

    print('-----'*10)
    # We probably shouldn't have personal information on here. Let's remove that K:V pair.
    del(student_dict['student_birthday'])
    print(student_dict)

    print('-----'*10)
    # Let's add a final class to the student's course key.
    # Since we're just using a list within the dictionary we'll use the same append() function.
    student_dict['student_courses'].append('CIS136')
    print('Updated Dictionary:', student_dict)

    print('-----'*10)
    # Our student is no longer in MAT151, so we should remove it.
    student_dict['student_courses'].remove('MAT151')
    print('Updated Dictionary:', student_dict)



if __name__ == '__main__':
    main()