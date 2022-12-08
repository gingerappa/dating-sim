define p = Character("Pauline")
define u = Character("You")
define g = Character("Game devs")

"""
totalhearts (if food +1)
jorrit     : 4 | 7 
"""
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
