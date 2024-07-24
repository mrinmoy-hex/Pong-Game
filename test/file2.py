import pygame

# reassigning vs modifying

"""
Reassigning
Reassigning refers to changing the reference of a variable to a new value or object. This effectively points the variable to a different object or value.

"""
x = 10        # Initial assignment
x = 20        # Reassigning to a new value

# Reassigning Objects:

player = pygame.Rect(0, 0, 50, 50)  # Initial assignment
player = pygame.Rect(100, 100, 50, 50)  # Reassigning to a new Rect object
# Here, player initially points to one pygame.Rect object. After reassignment, it points to a new pygame.Rect object with different properties.

# Modifying

'''Modifying refers to changing the state or attributes of the object that a variable references, without changing the reference itself.'''

x = 10
x += 5   # Modifying the value of x

'''
Here, x is modified to 15 without reassigning it to a different variable. It still refers to the same variable, but its value has changed.
'''

# Modifying Object Attributes:

player = pygame.Rect(0, 0, 50, 50)
player.x = 100   # Modifying the x attribute of the player object
player.y = 200   # Modifying the y attribute of the player object

'''
Here, the player object’s x and y attributes are modified. The player variable still refers to the same pygame.Rect object, but its internal state has changed.
'''