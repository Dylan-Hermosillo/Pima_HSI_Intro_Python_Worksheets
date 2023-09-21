'''
As you begin your programming journey one of the key skills you'll learn is how to find quick info.
Every question you have has been asked hundreds of times, and there are quite a few well-known resources for
everything programming.

1) Here are few -- with a special focus on variables.
   https://www.geeksforgeeks.org/python-variables/
   https://www.w3schools.com/python/python_variables.asp
   https://automatetheboringstuff.com/2e/chapter1/

2) Another website you'll get used to using is StackOverflow. It's a forum for technical questions.
   Often when you Google something like an error code or "how do I use [x] in Python" your first few hits will
   probably be a stack overflow answer.

3) Finally, everyone knows chatGPT is starting to become a great resource for boiler-plate code. 
   While you should absolutely start developing your own skills to be a better programmer, this tool can be
   a great resource for debugging. getting some extra help, and when you start programming often; writing
   chunks of monotonous code. The best part about knowing how to program is that you can fix the mistakes
   chatGPT gives you.

   We reviewed variables a bit in the intro, let's do a quick review and see how we can specify the 
   data type we want stored in a variable
'''
def main():
    '''
    Taking in data from the user.

    Often we want to use variables to collect info from the user. To do this we can use the input() function.
    Ex: animal_name = input('Enter the name of your animal: ')
   
    We have the variable name -- animal_name -- and it's being assigned by the input() function. 
    If you include a string inside the input, it'll write that as a message in the terminal.

    We already know variables can be used as containers, and we learned about how Python
    has different data types. One thing to keep in mind is that certain data types don't always mix.

    Type errors can occur when we use different data types in a way that's not supported.
    Such as trying to divide a string by a number. 
    
    There are cases where you can use mixed data types, multiplying a string by a number
    repeats the string. 

    Type casting is a way to ensure your data types are the format you want them to be.

    When we use the input command, it mainly takes in that information as a str.
    If we want to use it as a number, we'll need to cast it either when we collect it or after.
    '''
    # To show this we can test taking in user-input through the terminal
    test_variable = input("Enter a num: ")
    print(type(test_variable)) #notice that this says the variable is a str type not an int like we entered.

    print('-' * 20)
    # We can use type casting either during input:
    test_variable = int(input("Enter a num: "))
    print(type(test_variable))

    print('-' * 20)
    # We can also type cast after we gather input:
    print(float(test_variable))
    print(type(float(test_variable))) #Notice this will show a decimal of our previous values
    
    print('-' * 20)


  
if __name__ == '__main__':
    main()