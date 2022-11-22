define l = Character("Lezalith",
    who_color = "E34D0C")

define e = Character("Eileen",
    who_color = "E6E600")

label start():

    show eileen
    l "Oh well, let's test it out"

    # Silver background
    scene expression Solid("c0c0c0")

    # Show Eileen
    show eileen happy:
        xalign 0.5
    
    l "What should we say?"

    menu:
        l "There she is! I should say something!"

        "Hey, how are you doing?":

            e "Hey! I'm really good!"
            e "Come, let's do something cool"

        "Hey hottie, wanna make out?":

            e "Always, babe"
            e "You look amazing today."
            l "Wow. Can't believe that worked."

        # I told you I'd include it!
        #"{image=gui/window_icon.png}":

            # I was too lazy to come up with something that
            # would connect with the last dialogue line, so I
            # just gave it the pass statement so that this choice does nothing.
            #pass

    l "Ah yes, it works!"

    return
