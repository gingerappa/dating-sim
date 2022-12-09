#Defining characters


# The game starts here.

label sd_room:
    scene bg sd
    "welcome to SD room"
    jump jorrit


label jorrit:
    show jorrit neutral at right
    with dissolve
    if "intro" not in player["jorrit"]:
        js "Hey, welcome!"
        js "I assume you're the future student Pauline told me about"
        js "Let me introduce myself…"
        js "I'm Jorrit, nice to meet you."
        u "Hi Jorrit! Nice to meet you too!"
        $ player["jorrit"].append("intro")
    else:
        js "Hello again!"
    menu questionsWork_js:
        "What would you like to ask Jorrit?"
        "What do you teach the students?":
            js "I teach Software development and the elective subject Gameplay."
        "Favorite part of your job?":
            js "I've always enjoyed programming..."
            js "however, I tend to get tired of it when I do it for long periods at a time."
            js "The best part about working as a software development teacher is that I can combine my love for development with a ton of different working activities and tons of social interactions"
            u "Is it actually that hard to keep up with grading?"
            js "Depends on what you are grading and how you are grading!"
            js "Just writing V, G, O, V, V, in Magister is a lot less effort than giving useful feedback."
            js "Also, downloading big Unity projects or Blender files and waiting for the slow programs to open and close can eat up a bunch of time. Work smart!"
            if "jobQuestions_js" not in player["jorrit"]:
                menu jobQuestions_js:
                    "wow that sounds really easy":
                        show jorrit angry
                        pause
                        $ characters["jorrit"]["hearts"] -= 1
                    "u seem like a great teacher":
                        show jorrit happy
                        js "thank you"
                        $ characters["jorrit"]["hearts"] += 1
                $ player["jorrit"].append("jobQuestions_js")
    show jorrit neutral
    js "So, any other questions?"
    menu talk_js:
        "So, any other questions?"
        "What are your hobbies?":
            js "I play Dungeons&Dragons once or twice a week! {i}As long as scheduling doesn't ruin everything...{/i}"
            js "Recently I've also discovered a new hobby in using AI's to generate art."
            show jorrit blush
            js "Of course I also like to play games which was one of the reasons that got me into development in the first place."
            js "I listen to a bunch of music, but like, who doesn't?"
            js "Lastly, I like making cocktails. However I don't do it that often since I only do so at parties."
            show jorrit neutral
            if adult and "wantDrink_js" not in player["jorrit"]:
                js "Would you like a cocktail?"
                menu wantDrink_js:
                    "Yes":
                        show jorrit blush
                        js "Here you go!"
                        "Jorrit hands you a drink"
                        $ characters["jorrit"]["hearts"] += 1
                    "No":
                        js "Thats alright."
                    "iew..":
                        show jorrit irritated
                        pause
                        $ characters["jorrit"]["hearts"] -= 1
                $ player["jorrit"].append("wantDrink_js")
            $ player["jorrit"].append("hobbies")
        "Do you play games?":
            if "hobbies" in player["jorrit"]:
                js "As I said before..." 
            js "Quite frequently still!"
            #he tells all the games he plays
        "Any special interests?":
            show jorrit special_interest
            js "AI image generation, Dungeons and dragons..."
            if "animalMenu_js" not in player["jorrit"]:
                js "and i also love animals!"
                menu animalMenu_js:
                    "Me too i love cats!":
                        show jorrit happy
                        js "Oh yea cats are pretty awesome!"
                        $ characters["jorrit"]["hearts"] += 1
                        $ player["jorrit"].append("cats")
                    "Me too i love dogs!":
                        show jorrit angry
                        js "O yea i guese they exist too..."
                        $ characters["jorrit"]["hearts"] -= 1
                    "i dont realy like animals...":
                        js "o, thats alright"
                $ player["jorrit"].append("animalMenu_js")
            elif "cats" in player["jorrit"]:
                js "Oh, yea cats are pretty awesome!"
        "Favorite food?":
            js "I love a proper hamburger! Not some McDonald's hamburger, but a good one."
            if favorite_food == "hamburger":
                u "Yea me too."
                js "o thats awsome"
                if adult and "foodFlirt" not in player["jorrit"]::
                    u "Maby we can go get one some time..."
                    if characters["jorrit"]["hearts"] > 1:
                        show jorrit happy
                        js "i would love that!"
                        $ characters["jorrit"]["hearts"] +=  1
                    $ player["jorrit"].append("foodFlirt")
                
        "flirt!" if adult:
            menu flirt_js:
                "Are you single?" if "single" not in player["jorrit"]:
                    if characters["jorrit"]["hearts"] > 3:
                        show jorrit blush
                        js "As a pringle!" 
                        $ characters["jorrit"]["hearts"] += 1
                        $ player["jorrit"].append("single")
                    else:
                        show jorrit angry
                        js "Maybe you should ask again when I'm in a better mood." 
                    
                "Any plans for after your'e done working??" if "plans" not in player["jorrit"]:
                    if characters["jorrit"]["hearts"] > 2:
                        show jorrit happy
                        js "I'll probably visit some friends during the weekend!" 
                        $ characters["jorrit"]["hearts"] += 1
                    else:
                        show jorrit angry
                        js "You mean for when I retire!? Do you really think I look that old???" 
                        $ characters["jorrit"]["hearts"] -= 1
                    $ player["jorrit"].append("plans")

                "If you were my teacher I would be a teachers pet!" if "teachersPet" not in player["jorrit"]:
                    if characters["jorrit"]["hearts"] > 4:
                        show jorrit blush
                        js "If you are thinking of bringing me an apple, make sure to bring a green one!" 
                        $ characters["jorrit"]["hearts"] += 1
                    else:
                        show jorrit angry
                        js "If I was your teacher, I would kick you out of my class..." 
                        $ characters["jorrit"]["hearts"] -= 1
                    $ player["jorrit"].append("teachersPet")
                "nevermind...":
                    show jorrit neutral
                    jump talk_js
            jump flirt_js
        "say goodbye...":
            menu goodbye_js:
                "Thanks for talking to me!":
                    if "niceGoodbye" not in player["jorrit"]:
                        $ characters["jorrit"]["hearts"] += 1
                    if characters["jorrit"]["hearts"] > 0:
                        show jorrit neutral
                        js "Anytime!"
                    else:
                        show jorrit angry
                        js "Wish I could say the same!"
                    $ player["jorrit"].append("niceGoodbye")
                "Talk to you later!":
                    if characters["jorrit"]["hearts"] > 3:
                        show jorrit blush
                        js "Till next time"
                    elif characters["jorrit"]["hearts"] > 0:
                        show jorrit neutral
                        js "Till next time"
                    else:
                        show jorrit irritated
                        js "Oh god..."
                "bye":
                    if characters["jorrit"]["hearts"] > 0:
                        show jorrit neutral
                        js "See you later."
                    else:
                        show jorrit irritated
                        js "{i}finally...{/i}"
            show jorrit waving
            window hide
            pause
            hide jorrit
            jump sd_room
    show jorrit neutral
    jump talk_js
    
return