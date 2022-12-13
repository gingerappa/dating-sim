label sd_room:
    scene bg sd
    "welcome to SD room"
    menu talkToSd:
        "who would you like to talk to?"
        "Jorrit":
            jump jorrit
        "Thijs":
            jump thijs
        


label jorrit:
    show jorrit neutral at center
    with dissolve
    if "intro" not in player["jorrit"]:
        js "Hey, welcome!"
        js "I assume you're the future student Pauline told me about"
        js "Let me introduce myself…"
        js "I'm Jorrit, nice to meet you."
        u "Hi Jorrit! Nice to meet you too!"
        $ player["jorrit"].append("intro")
        $ characters["thijs"]["hearts"] += 1
    else:
        js "Hello again!"
    menu questionsWork_js:
        "What would you like to ask Jorrit about his job?"
        "What do you teach the students?":
            js "I teach Software development and the elective subject Gameplay."
            if "questionsWork_js" not in player["jorrit"]:
                $ player["jorrit"].append("questionsWork_js")
            jump questionsWork_js
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
            if "questionsWork_js" not in player["jorrit"]:
                $ player["jorrit"].append("questionsWork_js")
            jump questionsWork_js
        "Nothing..." if "questionsWork_js" in player["jorrit"]:
            pass
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
            #he tells all the games he plays (darksouls(very1), binding of isaac, dead by daylight)
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
                show jorrit suprised
                js "o thats awsome"
                if adult and "foodFlirt" not in player["jorrit"]:
                    u "Maby we can go get one some time..."
                    if characters["jorrit"]["hearts"] > 1:
                        show jorrit blush
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
                    if characters["jorrit"]["hearts"] > 2:
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
                    if characters["jorrit"]["hearts"] >= 0:
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
                    elif characters["jorrit"]["hearts"] >= 0:
                        show jorrit neutral
                        js "Till next time"
                    else:
                        show jorrit irritated
                        js "Oh god..."
                "bye":
                    if characters["jorrit"]["hearts"] >= 0:
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

label thijs:
    show thijs neutral at left
    with dissolve
    u "hey"
    if characters["thijs"]["hearts"] > 1:
        ts "ola mi amo thijs como estas?"
        menu spanish_ts:
            "muy bien, y tu?":
                show ts happy
                ts "muy bien"
            "amo a los chicos pelirrojos":
                show ts suprised
                ts "uuuh..."
                ts "si..."
                show ts happy
                ts "I dont acually know spanish haha"
            "donde esta la biblioteca?":
                show ts suprised
                ts "eyy i acually know that sentence"
                ts "lets gooo"
    elif characters["thijs"]["hearts"] < 0:
        ts "..."
    else:
        ts "ola"
        ts "..."
    "{i}programming noices... {/i}"
    show thijs neutral
    menu questionsStudent_ts:
        "What would you like to ask Thijs?"
        "What are you studying right now?":
            ts "I study software development here"
            if "questionsStudying_ts" not in player["thijs"]:
                menu questionsStudying_ts:
                    "What does that mean?":
                        show thijs happy
                        $ characters["thijs"]["hearts"] += 1
                    "Isn't that just typing on a computer?":
                        show thijs irritated
                        ts "no!"
                        $ characters["thijs"]["hearts"] -= 1
                $ player["thijs"].append("questionsStudying_ts")
            ts "It's like writing instructions for a computer"
            ts "Iike this game, in the code i wrote the options you just got to pick"
            ts "And depending on what options you picked my hearts went up or down"
            ts "Determaning if i like you or well, if my character likes you haha..."
            jump questionsStudent_ts
        "What’s your elective subject?":
            show thijs happy
            ts "Gameplay which is basically just game design but a cooler name"
            ts "It has notting to do with programming more with how to create a game"
            ts "And what makes a game good alwell as how to disign a game in the real world"
            jump questionsStudent_ts
        "Do you have a favorite teacher?":
            ts "I think Jorid is kind of down to earth and chill about school"
            ts "but he can be strict when push comes to shove"
            ts "and he is overall very helpfull"
            if "intro" in player["jorrit"] and "knowJorrit_ts" not in player["thijs"]:
                show thijs happy
                ts "But i see here in the game files that you already know that."
                show thijs neutral
                ts "what did you think of jorrit"
                menu knowJorrit_ts:
                    "I did not talk to Jorrit":
                        show thijs angry
                        ts "DONT LIE TO ME!"
                        $ characters["thijs"]["hearts"] -= 1
                    "i hate Jorrit!":
                        show thijs angry
                        show jorrit angry at right
                        with dissolve
                        $ characters["thijs"]["hearts"] -= 1
                        $ characters["jorrit"]["hearts"] -= 1
                        pause
                        hide jorrit
                        ts "Why would you say that"
                    "i would like to have Jorrit as a teacher":
                        show thijs happy
                        ts "me too, he is a great teacher"
                        $ characters["thijs"]["hearts"] += 1
                $ player["thijs"].append("knowJorrit_ts")
            jump questionsStudent_ts
        "What are they teaching you right now?":
            ts "How to make a unity game, even though this game is not made in unity haha"
            jump questionsStudent_ts
        "nothing..":
            pass
    show thijs neutral
    ts "So, any other questions?"
    menu talk_ts:
        "So, any other questions?"
        "What are your hobbies?":
            ts "I like playing games and coding of course and I have started climbing with some friends recently."
            show thijs happy
            ts "I realy like doing it. And its a great workout for my mind as well as my body."
        "Do you play games?":
            ts "yes."
            u "well.. what games?"
            ts "what I play verys from time to time but I always seem to come back to league and brawlhalla somehow"
        "Have any special interests?" if "specialInterstGood_ts" not in player["thijs"]:
            ts "Something not a lot of people know is that I do acting again for about a year."
            ts "I did it in high school for 2 years and youth drama but I picked it back up again last year with a local acting club."
            ts "I realy enjoy it, esesialy the role i have now because its very close to how i am when not acting."
            if "specialInterst_ts" not in player["thijs"]:
                menu specialInterst_ts:
                    "Iew, a theater kid":
                        show thijs angry
                        $ characters["thijs"]["hearts"] -= 1
                        pause
                        $ player["thijs"].append("specialInterst_ts")
                        show thijs neutral
                        jump talk_ts
                    "o that sounds great":
                        show thijs blush
                        ts "Yea"
                        ts "..."
                        ts "If you want you could come to my next show..."
                        $ player["thijs"].append("specialInterstGood_ts")
                        $ characters["thijs"]["hearts"] += 1
        "how about that show?" if "specialInterstGood_ts" in player["thijs"]:
            show thijs suprised
            ts "o.."
            ts "soo, you want to come to my next show?"
            menu goToShow:
                "yes":
                    show thijs blush
                    $ characters["thijs"]["hearts"] += 1
                    ts "Awsome..."
                "no":
                    show thijs angry
                    $ characters["thijs"]["hearts"] -= 1
                    ts "your loss..."
            $ player["thijs"].remove("specialInterstGood_ts") 
        "Favorite food?":
            ts "Chicken wings for sureeee"
            if favorite_food == "Chicken wings":
                u "me too"
                ts "no way"
                if "favoriteFood_ts" not in player["thijs"]:
                    ts "what place do you get your wings?"
                    menu favoriteFood_ts:
                        "McDonalds":
                            show thijs suprised
                            ts "do they even have wings there?"
                            u "no, the mcnugget"
                            show thijs angry
                            ts "thats not THE SAME THING!!!"
                            $ characters["thijs"]["hearts"] -= 1
                        "KFC":
                            show thijs happy
                            ts "lets goo"
                            ts "ez W"
                            $ characters["thijs"]["hearts"] += 1
                        "Home made":
                            show thijs happy
                            ts "o can i come get some wings next time?"
                            menu whatThijs4wings:
                                "yes":
                                    show thijs blush
                                    $ characters["thijs"]["hearts"] += 1
                                    pause
                                "no":
                                    show thijs angry
                                    $ characters["thijs"]["hearts"] -= 1
                                    ts "o, ok..."
                    $ player["thijs"].append("favoriteFood_ts")
        "Flirt!" if adult:
            menu flirt_ts:
                "You single?":
                    if characters["thijs"]["hearts"] > 3:
                        ts "do you want me to be?"
                "Choice 2":
                    pass

    show thijs neutral
    jump talk_ts
            
                    
        
                