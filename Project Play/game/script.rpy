﻿define p = Character("Pauline")
define u = Character("You")
define g = Character("Game devs")

"""
totalhearts (if food +1)
jorrit     : 4 | 7
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


# The game starts here.
label start:
    show a neutral
    show a happy
    show a sad
    ""
    $ characters = {"jorrit":{"hearts":0, "askedHobbies": False}, "thijs":{"hearts":0}}
    jump tutorial

label house1_pressed:
    "welcome to \{classroom\}!"
    "ga daten ofzo"
    jump main
label end:
    jump main
return
