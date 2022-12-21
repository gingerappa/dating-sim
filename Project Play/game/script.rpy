define e = Character("Enzo Witteveen")
define g = Character("Game devs")
define gm = Character("Grayson Middelink")
define jl = Character("Julia Wiebbelling")
define js = Character("Jorrit Slaats")
define kd = Character("Kevin Driessen")
define l = Character("Lex van den Bergh")
define ls = Character("Lusi Ryborz")
define m = Character("Max Marzano")
define p = Character("Pauline")
define rh = Character("Robin Hilt")
define sk = Character("Sam Kaufman")
define ts = Character("Thijs Swinkels")
define u = Character("You")

"""
totalhearts (if food +1)
jorrit     : 5 | 8
thijs      : 6 | 9
"""
transform f11:
    zoom 1.5

transform midleft:
    zoom 1.5
    xpos 300

transform midright:
    zoom 1.5
    xpos 900

init python:
    config.keymap['rollback'] = []
    config.keymap['screenshot'] = []
    config.keymap['toggle_fullscreen'] = []
    config.keymap['game_menu'] = ["K_ESCAPE"]
    config.keymap['hide_windows'] = []
    config.keymap['launch_editor'] = []
    config.keymap['inspector'] = []
    config.keymap['hide_windows'] = []
    #TODO make wasd work on select
    for x in ["K_r", "K_LSHIFT", "K_f", "K_SPACE", "K_LCTRL", "K_e",  "K_KP4", "K_KP5", "K_KP6", "K_KP7", "K_KP8", "K_KP9"]:
        config.keymap['dismiss'].append(x)
    
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
    $ pronouns = ["the player, the player"]
    $ adult = True
    $ characters = {"jorrit":{"hearts":0}, "thijs":{"hearts":0}, "lusi":{"hearts":0}, "julia":{"hearts":0}, "enzo":{"hearts":0}, "pauline":{"hearts":0},"max":{"hearts":0},"grayson":{"hearts":0}, "kevin":{"hearts":0}, "lex":{"hearts":0},"robin":{"hearts":0},"sam":{"hearts":0}}
    $ player = {"jorrit":[], "thijs":[], "lusi":[], "julia":[], "enzo":[], "pauline":[], "max":[], "grayson":[], "kevin":[], "lex":[], "robin":[], "sam":[]}
    $ favorite_food = "Candy"
    jump tutorial

label house1_pressed:
    scene bg classroom
    "Welcome to a classroom!"
    "This will be updated soon, for now please explore the other classrooms!"
    jump main
label end:
    jump main
return
