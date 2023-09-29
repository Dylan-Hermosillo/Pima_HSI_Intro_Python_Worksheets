'''
In our final exploraton of Python we'll be talking about Object-Oriented Programming (OOP) and how to
navigate defining and using classes in Python. 

OOP is a programming paradigm (a specific way to code) that organizes code into objects.
These are reusable elements that can represent anything we want. It makes it easy to program real-world entities/concepts.
These objects have data (attributes) and behaviors (methods), allowing for a more structured and
modular approach to software development.
In short, it's another way to easily re-use code and provide a sense of structure.

In this first file we'll go over what it means to define a class -- which you'll see is a lot like defining a function.
In fact, functions that are within a class are called methods. Variables that are stored as data are called attributes.

Resources: 
- https://www.w3schools.com/python/python_classes.asp
- https://www.geeksforgeeks.org/python-classes-and-objects/
'''

# Let's define a class modeling a snake as an example below;

class Snake: 
    ''' 
    The __init__ or initalize method is what we use to
    "construct" our object. In many languages it's simply called the constructor.

    We make a method and inside it we always first pass 'self' to say we're referencing
    this object we're making, followed by any other attributes we want.
    '''
    def __init__(self, name, species):
        self.name = name #on the left-side we say we're changing the self's name to the name we pass in the parameters
        self.species = species # same for the species
        # Later we can access the object's data/attributes that we saved here.

    '''
    Once we have our init method we can continue to make any other methods we would need.
    Considering we use OOP to build models of real world examples we can create
    these abstract representation of things a snake would do.
    '''
    def make_sound(self):
        return "sssssssss"

    def crawl(self):
        print(f"{self.name} is crawling.")

    def snake_facts(self):
        print(f"My {self.species}'s name is {self.name}.")

# Let's make a snake object and test some of the methods!
my_snake = Snake('Mochi', 'Corn Snake') # Creating the new snake object

# This will print the statement we have in the method using the data/attributes we 
# gave it when we first made the snake object!
my_snake.snake_facts() 

# What if I gave it the wrong species?
# We can update it using the object and accessing it's data.
my_snake.species = 'Ball Python'

# Now our snake facts are correct!
my_snake.snake_facts()

# All our methods we defined will work.
my_snake.crawl()
my_snake.make_sound()

# Just like functions, the method can be called in various places.
print("My snake always hisses at me!", my_snake.make_sound())