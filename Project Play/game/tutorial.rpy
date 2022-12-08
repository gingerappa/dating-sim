define p = Character("Pauline")
define u = Character("You")
define g = Character("Game devs")

# The game starts here.

label tutorial:

    scene Placeholder

    show eileen happy at left

    p "Hi! Welcome to SintLucas!"
    p "I'm Pauline and I'll be your guide today"
    p "First of all, what are your pronouns?"

    menu:
        "What are your pronouns?"
        "He/him":
            $ pronouns = ["he", "him"]
            
        "She/her":
            $ pronouns = ["she", "her"]
        "They/them":
            $ pronouns = ["they, them"]
        "None":
            $ pronouns = ["the player, the player"]
 
        
    p "Alright! I'll remember that!"
    p "It's amazing to meet you, can I know your age?"
    jump age

label age:
    menu:
        "How old are you?"

        "I'm a minor":
            $adult = False
            show eileen happy    
            p "Thanks for your honesty!"
            jump map_info
            
        "I'm 18+":
            $adult = True
            g "Disclaimer: we hope you've been honest, because now there is no coming back."
            #TODO change logo and name, unlock 18+ features
            p "Thanks! The game is now addapted to your age."
            p "Welcome..."
            p "to the Sintlucas DATING simulator"
            jump map_info

        "Why is that important?":
            p "It's important that I know your age so that I can optimise the game to best fill your expectations and provide you a nice experience!"
            jump age

label map_info:
    p "Now that we have every important information about you, let's head to the real fun."
    #TODO: show map given
    p "This is a map, an useful gadget that you will use a lot around here."
    p "Using it is quite simple, I'll teach you!"
    #TODO: show picture of arcade button
    p "Just press the third button on the arcade machine, just like this one! That should open the map."
    p "With the map open, just hover around a place and click to go there. The paths aren't that long, so you should be able to arrive in a few seconds."

    menu understand_map:
        "Did you understand everything?"

        "Not really, can you repeat?":
            p "Just press the third button on the arcade machine, just like this one! That should open the map."
            p "With the map open, just hover around a place and click to go there. The paths aren't that long, so you should be able to arrive in a few seconds." 
            jump understand_map

        "Yes!":
            p "Alright! Thanks for listening."
            p "Feel free to explore all the classrooms. I'd specially recommend visiting the DDM place, there are some cool people in there."
            u "Okay, thanks!"
            play music "music/main.mp3" fadein 1.0 volume 0.1
            jump end
