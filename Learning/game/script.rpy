# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("Master")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene island


    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show dog 1
    with dissolve

    "On cracker island it was born"

    scene dawn

    show dog hero at right
    with move

    "to the collective of the dawn"

    scene farm

    show dog watermellon at center
    with move

    "they were planting seeds at night"

    scene paradise

    show dog 3 at center
    with move

    "to grow a made up paradise"

    scene music

    show dog sing

    "Where the truth was auto-tuned"

    show dog 6
    with dissolve

    "For - e - ver - cult"

    show dog egg at center
    with move

    "And it's sadness I consumed"

    show dog 6
    with dissolve

    "For - e - ver - cult"

    show dog smart at right
    with move

    "Into my formats every day"

    show dog cult at center
    with dissolve

    "FOR EEEE VER CULT"

    show dog pay at center
    with dissolve

    "In the end, I had to pay"

    show dog 8 at center
    with dissolve

    "What world is this?"

    show dog 4 at center
    with dissolve

    "In the end, I had to pay"

    show dog 2 at center
    with dissolve

    "I purged my soul"

    show dog pay 2 at center
    with dissolve

    "In the end, I had to pay"

    show dog drink at center
    with dissolve

    "I drank to riot"

    show dog busy at center
    with dissolve

    "Nothing more to say"

    show dog 4 at center
    with dissolve

    "I drank to riot"

    show dog cow at center
    with dissolve

    "They taught themselves to be occult"

    return
