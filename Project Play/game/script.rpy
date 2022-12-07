define p = Character("Pauline")
define u = Character("You")
define g = Character("Game devs")

# The game starts here.

label start:

    scene Placeholder

    show eileen happy at left
    with move

    p "Hi! Welcome to SintLucas!"
    p "I'm Pauline and I'll be your guide today"
    # TODO: put Pauline's function (the correct way)
    p "Oficially, I'm a softskills teacher"
    p "First of all, what are your pronouns?"

    menu:

        "What are your pronouns?"

        "He/him":
            $ pronouns = "he"
            
        "She/her":
            $ pronouns = "she"
            
        "They/them":
            $ pronouns = "neutral"
        "None":            
            $ pronouns = "none"
 
        
    p "Alright! I'll remember that!"
    p "It's amazing to meet you, can I know your age?"

label age:

    menu:
    
        "How old are you?"

        "I'm a minor":
            $ age = 1
            jump minor
            
        "I'm 18+":
            $ age = 18
            jump dating_sim

        "Why is that important?":
            call explanation

jump end  
        
label explanation:
p "It's important that I know your age so that I can optimise the game to best fill your expectations and provide you a nice experience!"
jump age


label dating_sim:

    g "Disclaimer: we hope you've been honest, because now there is no coming back."
    #TODO change logo and name, unlock 18+ features
    p "Thanks! The game is now addapted to your age."
    p "Welcome..."
    p "to the Sintlucas DATING simulator"
jump map_info

label minor:

    show eileen vhappy    
    p "Thanks for your honesty!"

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
            jump understand_map_no

        "Yes!":
            p "Alright! Thanks for listening."
            p "Feel free to explore all the classrooms. I'd specially recommend visiting the DDM place, there are some cool people in there."
            u "Okay, thanks!."
            jump end

label understand_map_no:
    p "Just press the third button on the arcade machine, just like this one! That should open the map."
    p "With the map open, just hover around a place and click to go there. The paths aren't that long, so you should be able to arrive in a few seconds."            
jump understand_map

label end:

    u "I love this game!"
return
