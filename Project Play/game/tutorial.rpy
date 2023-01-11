label tutorial:
    scene sintlucas bg
    play music "music/map_music.mp3" fadein 1.0 volume 1
    show pauline happy at f11

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

label favFood:
    p "Also, what is your favorite food?"
    menu Favorite_food:
        "What is your favorite food?"
        "Hamburger":
            $ favorite_food = "hamburger"
        "Chicken wings":
            $ favorite_food = "Chicken wings"
        "Candy":
            $ favorite_food = "Candy"
            p "Here you go, have some candy!"
        "Sushi":
            $ favorite_food = "sushi"
        "Italian food":
            $ favorite_food = "italian"
        "Strogannof":
            $ favorite_food = "strogannof"
        "I have no favorites":
            $ favorite_food = "none"
    p "Great choice!"
    jump map_info

label age:
    menu:
        "How old are you?"

        "I'm a minor":
            $ adult = False
            show pauline happy    
            p "Thanks for your honesty!"
            jump Favorite_food
            
        "I'm 18+":
            $ adult = True
            g "Disclaimer: we hope you've been honest, because now there is no coming back."
            #TODO change logo and name, unlock 18+ features
            p "Thanks! The game is now addapted to your age."
            p "Welcome..."
            p "to the Sintlucas DATING simulator"
            jump Favorite_food

        "Why is that important?":
            p "It's important that I know your age so that I can optimise the game to best fill your expectations and provide you a nice experience!"
            jump age      

label map_info:
    p "Now that we have every important information about you, let's head to the real fun."
    show bg map
    p "This is a map, an useful gadget that you will use a lot around here."
    window hide
    p "Using it is quite simple, I'll teach you!"
    p "With the map open, just hover around a place and click to go there."
    hide bg map
    p "The paths aren't that long, so you should be able to arrive in a few seconds."

    menu understand_map:
        "Did you understand everything?"

        "Not really, can you repeat?":
            p "Just use the mouse the click where you'd like to go!"
            jump understand_map

        "Yes!":
            p "Alright! Thanks for listening."
            p "Feel free to explore all the classrooms. I'd specially recommend visiting the DDM place, there are some cool people in there."
            u "Okay, thanks!"
            jump end