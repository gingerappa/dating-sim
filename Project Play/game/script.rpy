# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define u = Character("You")


# The game starts here.

label start:

    scene bg room

    show girl sillhouete
    with dissolve

    e "Hi! This is a prototype, welcome to SintLucas simulator."

    e "It's amazing to meet you, can I know your age?"


label age:

    # Silver background
    scene expression Solid("c0c0c0")

    show girl sillhouete

    menu:
    
        "How old are you?"

        "I'm <18":
            jump friendly_start
            
        "I'm 18+":
            jump dating_sim

        "Why is that important?":
            call explanation

jump end  
        
label explanation:
e "It's important that I know your age so that I can optimise the game to best fill your expectations and provide you a nice experience!"
return

label dating_sim:

    e "Thanks! The game is now addapted to your age."
    e "Welcome..."

    show girl sus at center
    with move
    e "to the Sintlucas DATING simulator"
    

label friendly_start:
    show girl sillhouete
    u "Oh well, let's test it out"

    # Silver background
    scene expression Solid("c0c0c0")

    # Show Eileen
    show eileen:
        xalign 0.5
    
    u "What should we say?"

    menu:
        "There she is! I should say something!"

        "Hey, how are you doing?":

            e "Hey! I'm really good!"
            e "Come, let's do something cool"
            

        "Hey hottie, wanna make out?":

            e "Always, babe"
            e "You look amazing today."
            u "Wow. Can't believe that worked."

label end:

    u "I love this game!"
return
