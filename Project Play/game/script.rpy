define p = Character("Pauline")
define u = Character("You")
define g = Character("Game devs")

"""
totalhearts
jorrit     : 4
"""
# The game starts here.
label start:
    $ characters = {"jorrit":{"hearts":0, "askedHobbies": False}, "thijs":{"hearts":0}}
    jump tutorial

label house1_pressed:
    "welcome to \{classroom\}!"
    "ga daten ofzo"
    jump main
label end:
    jump main
return
