define p = Character("Pauline")
define u = Character("You")
define g = Character("Game devs")
define js = Character("Jorrit Slaats")
define ts = Character("Thijs Swinkels")
define e = Character("Enzo Witteveen")
define m = Character("Max Marzano")

transform f11:
    zoom 1.5

"""
totalhearts (if food +1)
jorrit     : 5 | 8
thijs      : 6 | 9
"""
init python:
    def getDic(*args):
        if not args:
            dir = characters
            tabs = 0
        else:
            dir = args[0]
            if len(args) >= 2:
                tabs = args[1]
            else:
                tabs = 0
        for key, value in dir.items():
            if type(value) == type({}):
                print(f"{'  ' * tabs}{key}:")
                getDic(dir[key], tabs+1)
            else:
                print(f"{'  ' * tabs}{key}: {value}")

label start:
    $ pronouns = ["the player, the player"]
    $ adult = True
    $ characters = {"jorrit":{"hearts":0}, "thijs":{"hearts":0}, "enzo":{"hearts":0}, "pauline":{"hearts":0},"max":{"hearts":0},"grayson":{"hearts":0}}
    $ player = {"jorrit":[], "thijs":[], "enzo":[], "pauline":[], "max":[], "grayson":[]}
    $ favorite_food = "hamburger"
    jump tutorial

label house1_pressed:
    scene bg classroom
    "Welcome to a classroom!"
    "Hint, go to the SD room for the prototype ;)"
    jump main
label end:
    jump main
return
