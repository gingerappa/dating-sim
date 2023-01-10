label sd_room:
    scene bg sd
    play music "music/class (3).mp3" fadein 1.0 volume 1
    call screen sd_screen

screen sd_screen:
    imagebutton:
        xpos 0
        ypos 360
        idle "characters/jorrit/jorrit neutral.png"
        hover "characters/jorrit/jorrit happy.png"
        action Jump("jorrit")
    imagebutton:
        xpos 473
        ypos 360
        idle "characters/thijs/thijs neutral.png"
        hover "characters/thijs/thijs happy.png"
        action Jump("thijs")
    imagebutton:
        xpos 946
        ypos 360
        idle "characters/lusi/lusi neutral.png"
        hover "characters/lusi/lusi happy.png"
        action Jump("lusi")
    imagebutton:
        xpos 1419
        ypos 360
        idle "characters/julia/julia neutral.png"
        hover "characters/julia/julia happy.png"
        action Jump("julia")
    imagebutton:
        xpos 0
        ypos 0
        idle "icons/map logo.png"
        hover "icons/map logo_hover.png"
        action Jump("main")

label jorrit:
    show jorrit neutral at f11
    with dissolve
    if "intro" not in player["jorrit"]:
        js "Hey, welcome!"
        js "I assume you're the future student Pauline told me about"
        js "Let me introduce myself..."
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
            show jorrit neutral
            jump questionsWork_js
        "Favorite part of your job?":
            js "I've always enjoyed programming..."
            js "However, I tend to get tired of it when I do it for long periods at a time."
            js "The best part about working as a software development teacher is that I can combine my love for development with a ton of different working activities and tons of social interactions"
            u "Is it actually that hard to keep up with grading?"
            show jorrit surprised
            js "Depends on what you are grading and how you are grading!"
            show jorrit happy
            js "Just writing V, G and O in Magister is a lot less effort than giving useful feedback."
            js "Also, downloading big Unity projects or Blender files and waiting for the slow programs to open and close can eat up a bunch of time. Work smart!"
            if "jobQuestions_js" not in player["jorrit"]:
                menu jobQuestions_js:
                    "Wow, that sounds really easy":
                        show jorrit angry
                        pause
                        $ characters["jorrit"]["hearts"] -= 1
                    "U seem like a great teacher":
                        show jorrit happy
                        js "Thank you! I always try my best."
                        $ characters["jorrit"]["hearts"] += 1
                $ player["jorrit"].append("jobQuestions_js")
            if "questionsWork_js" not in player["jorrit"]:
                $ player["jorrit"].append("questionsWork_js")
            show jorrit neutral
            jump questionsWork_js
        "Why did you pick teaching?":
            js "I kind of rolled into it."
            show jorrit happy
            js "I couldn't get myself to full-time program from 9 to 5 and saw a vacancy to work here."
            js "I decided to give it a try and haven't thought of going back ever since."
            u "Wow, thats interesting."
            if "questionsWork_js" not in player["jorrit"]:
                $ player["jorrit"].append("questionsWork_js")
            show jorrit neutral
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
            show jorrit blushing
            js "Of course I also like to play games which was one of the reasons that got me into development in the first place."
            js "I listen to a bunch of music, but like, who doesn't?"
            js "Lastly, I like making cocktails. However I don't do it that often since I only do so at parties."
            show jorrit neutral
            if adult and "wantDrink_js" not in player["jorrit"]:
                js "Would you like a cocktail?"
                menu wantDrink_js:
                    "Yes":
                        show jorrit blushing
                        js "Here you go!"
                        "Jorrit hands you a drink"
                        $ characters["jorrit"]["hearts"] += 1
                    "No":
                        js "That's alright."
                    "Ew...":
                        show jorrit angry
                        pause
                        $ characters["jorrit"]["hearts"] -= 1
                $ player["jorrit"].append("wantDrink_js")
            $ player["jorrit"].append("hobbies")
        "Do you play games?":
            if "hobbies" in player["jorrit"]:
                js "As I said before..." 
            js "Quite frequently still!"
            js "Right now I'm very into Dark Souls, Binding of Isaac and Dead by Daylight."
        "Any special interests?":
            show jorrit special_interest
            js "AI image generation, Dungeons&Dragons..."
            if "animalMenu_js" not in player["jorrit"]:
                js "And i also love animals!"
                menu animalMenu_js:
                    "Me too, I love cats!":
                        show jorrit happy
                        js "Oh yeah! Cats are pretty awesome!"
                        $ characters["jorrit"]["hearts"] += 1
                        $ player["jorrit"].append("cats")
                    "Me too, I love dogs!":
                        show jorrit neutral
                        js "I guess they exist too..."
                        $ characters["jorrit"]["hearts"] -= 1
                    "I dont realy like animals...":
                        js "Ah, that's alright."
                $ player["jorrit"].append("animalMenu_js")
            elif "cats" in player["jorrit"]:
                js "Cats are pretty awesome!"
        "Favorite food?":
            js "I love a proper hamburger! Not some McDonald's hamburger, but a good one."
            if favorite_food == "hamburger":
                u "Yeah, me too."
                show jorrit surprised
                js "Oh, thats awesome!"
                if adult and "foodFlirt" not in player["jorrit"]:
                    u "Maybe we can go get one some time..."
                    if characters["jorrit"]["hearts"] > 1:
                        show jorrit blushing
                        js "I would love that!"
                        $ characters["jorrit"]["hearts"] +=  1
                    $ player["jorrit"].append("foodFlirt")
                
        "Flirt!" if adult:
            menu flirt_js:
                "Are you single?" if "single" not in player["jorrit"]:
                    if characters["jorrit"]["hearts"] > 3:
                        show jorrit blushing
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
                        show jorrit blushing
                        js "If you are thinking of bringing me an apple, make sure to bring a green one!" 
                        $ characters["jorrit"]["hearts"] += 1
                    else:
                        show jorrit angry
                        js "If I was your teacher, I would kick you out of my class..." 
                        $ characters["jorrit"]["hearts"] -= 1
                    $ player["jorrit"].append("teachersPet")
                "Nevermind...":
                    show jorrit neutral
                    jump talk_js
            jump flirt_js
        "Say goodbye":
            menu goodbye_js:
                "Thanks for talking to me!":
                    if "niceGoodbye" not in player["jorrit"]:
                        $ characters["jorrit"]["hearts"] += 1
                        $ player["jorrit"].append("niceGoodbye")
                    if characters["jorrit"]["hearts"] >= 0:
                        show jorrit neutral
                        js "Anytime!"
                    else:
                        show jorrit angry
                        js "Wish I could say the same!"
                "Talk to you later!":
                    if characters["jorrit"]["hearts"] > 3:
                        show jorrit blushing
                        js "Till next time"
                    elif characters["jorrit"]["hearts"] >= 0:
                        show jorrit neutral
                        js "Till next time"
                    else:
                        show jorrit angry
                        js "Oh god..."
                "bye":
                    if characters["jorrit"]["hearts"] >= 0:
                        show jorrit neutral
                        js "See you later."
                    else:
                        show jorrit angry
                        js "{i}Finally...{/i}"
            hide jorrit
            jump sd_room
    show jorrit neutral
    jump talk_js

label thijs:
    show thijs neutral at f11
    with dissolve
    u "Hey!"
    if characters["thijs"]["hearts"] > 1:
        ts "Ola, mi llamo thijs como estas?"
        menu spanish_ts:
            "Muy bien, y tu?":
                show thijs happy
                ts "Muy bien!"
            "Amo a los chicos pelirrojos":
                show thijs surprised
                ts "Uuuh..."
                ts "Si..."
                show thijs happy
                ts "I dont acually know Spanish haha"
            "Donde esta la biblioteca?":
                show thijs surprised
                ts "Eyy i acually know that sentence"
                ts "Let's gooo"
    elif characters["thijs"]["hearts"] < 0:
        ts "..."
    else:
        ts "Ola"
        ts "..."
    "{i}Programming noises... {/i}"
    show thijs neutral
    menu questionsStudent_ts:
        "What would you like to ask Thijs as a student?"
        "What are you studying right now?":
            ts "I study software development here"
            if "questionsStudying_ts" not in player["thijs"]:
                menu questionsStudying_ts:
                    "What does that mean?":
                        show thijs happy
                        $ characters["thijs"]["hearts"] += 1
                    "Isn't that just typing on a computer?":
                        show thijs angry
                        ts "No!"
                        $ characters["thijs"]["hearts"] -= 1
                $ player["thijs"].append("questionsStudying_ts")
            ts "It's like writing instructions for a computer"
            ts "Like this game, in the code I wrote the options you just got to pick"
            ts "And depending on what options you picked my hearts went up or down"
            ts "Determining if I like you or {i}well{/i}, if my character likes you haha..."
            if "questionsStudent_ts" not in player["thijs"]:
                $ player["thijs"].append("questionsStudent_ts")
            jump questionsStudent_ts
        "What's your elective subject?":
            show thijs happy
            ts "Gameplay, which is basically just game design but with a cooler name"
            ts "It has notting to do with programming. More with how to create a game"
            ts "And what makes a game good, as well as how to design a game in the real world"
            if "questionsStudent_ts" not in player["thijs"]:
                $ player["thijs"].append("questionsStudent_ts")
            jump questionsStudent_ts
        "Do you have a favorite teacher?":
            ts "I think Jorrit is kind of down to earth and chill about school"
            ts "But he can be strict when push comes to shove"
            ts "And he is overall very helpful!"
            if "intro" in player["jorrit"] and "knowJorrit_ts" not in player["thijs"]:
                show thijs happy
                ts "But i see here in the game files that you already know that."
                show thijs neutral
                ts "What did you think of Jorrit?"
                menu knowJorrit_ts:
                    "I did not talk to Jorrit":
                        show thijs angry
                        ts "DON'T LIE TO ME!"
                        $ characters["thijs"]["hearts"] -= 1
                    "I hate Jorrit!":
                        show thijs angry
                        show jorrit angry at f11, right
                        with dissolve
                        $ characters["thijs"]["hearts"] -= 1
                        $ characters["jorrit"]["hearts"] -= 1
                        pause
                        hide jorrit
                        ts "Why would you say that?!"
                    "I would like to have Jorrit as a teacher":
                        show thijs happy
                        ts "Me too, he is a great teacher."
                        $ characters["thijs"]["hearts"] += 1
                $ player["thijs"].append("knowJorrit_ts")
            if "questionsStudent_ts" not in player["thijs"]:
                $ player["thijs"].append("questionsStudent_ts")
            jump questionsStudent_ts
        "What are they teaching you right now?":
            ts "How to make a unity game, even though this game is not made in Unity haha"
            if "questionsStudent_ts" not in player["thijs"]:
                $ player["thijs"].append("questionsStudent_ts")
            show thijs neutral
            jump questionsStudent_ts
        "Nothing..." if "questionsStudent_ts" in player["thijs"]:
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
            ts "Yes."
            u "Well... what games?"
            ts "What I play varies from time to time but I always seem to come back to League of Legends and Brawlhalla somehow"
        "Have any special interests?" if "specialInterstGood_ts" not in player["thijs"]:
            ts "Something not a lot of people know is that I do acting again for about a year."
            ts "I did it in high school for 2 years and youth drama but I picked it back up again last year with a local acting club."
            ts "I realy enjoy it, specially the role I have now because it's very close to how I am when not acting."
            if "specialInterst_ts" not in player["thijs"]:
                menu specialInterst_ts:
                    "Iew, a theater kid":
                        show thijs angry
                        $ characters["thijs"]["hearts"] -= 1
                        pause
                        $ player["thijs"].append("specialInterst_ts")
                        show thijs neutral
                        jump talk_ts
                    "That sounds great":
                        show thijs blushing
                        ts "Yeah"
                        ts "..."
                        ts "If you want you could come to my next show..."
                        $ player["thijs"].append("specialInterstGood_ts")
                        $ characters["thijs"]["hearts"] += 1
        "How about that show?" if "specialInterstGood_ts" in player["thijs"]:
            show thijs surprised
            ts "Oh..."
            ts "Soo, you want to come to my next show?"
            menu goToShow:
                "Yes!":
                    show thijs blushing
                    $ characters["thijs"]["hearts"] += 1
                    ts "Awesome..."
                "Nope":
                    show thijs angry
                    $ characters["thijs"]["hearts"] -= 1
                    ts "Your loss..."
            $ player["thijs"].remove("specialInterstGood_ts") 
        "Favorite food?":
            ts "Chicken wings for sureeee"
            if favorite_food == "Chicken wings":
                u "Me too!"
                ts "No way!"
                if "favoriteFood_ts" not in player["thijs"]:
                    ts "What place do you get your wings from?"
                    menu favoriteFood_ts:
                        "McDonalds":
                            show thijs surprised
                            ts "Do they even have wings there?"
                            u "No, the McNugget."
                            show thijs angry
                            ts "That's not THE SAME THING!!!"
                            $ characters["thijs"]["hearts"] -= 1
                        "KFC":
                            show thijs happy
                            ts "Lets goo"
                            ts "Easy W"
                            $ characters["thijs"]["hearts"] += 1
                        "Home made":
                            show thijs happy
                            ts "Can i come get some wings next time?"
                            menu whatThijs4wings:
                                "Yes":
                                    show thijs blushing
                                    $ characters["thijs"]["hearts"] += 1
                                    pause
                                "No":
                                    show thijs angry
                                    $ characters["thijs"]["hearts"] -= 1
                                    ts "Oh, ok..."
                    $ player["thijs"].append("favoriteFood_ts")
        "Flirt!" if adult:
            menu flirt_ts:
                "You single?":
                    if characters["thijs"]["hearts"] > 3:
                        show thijs blushing
                        ts "Do you want me to be?"
                    else:
                        show thijs angry
                        ts "Not for you..."
                "You are really good looking, did you know that?" if "GoodLooking_ts" not in player["thijs"]:
                    if characters["thijs"]["hearts"] > 3:
                        show thijs surprised
                        ts "Agree to disagree"
                        $ characters["thijs"]["hearts"] += 1
                    else:
                        show thijs angry
                        ts "Disagree"
                        $ characters["thijs"]["hearts"] -= 1
                    $ player["thijs"].append("GoodLooking_ts")
                "Are you a 90 degree angle because you look so right!" if "angle_ts" not in player["thijs"]:
                    if characters["thijs"]["hearts"] > 3:
                        show thijs blush
                        pause
                        ts "Really, with that. Damn, you're good."
                        $ characters["thijs"]["hearts"] += 1
                    else:
                        show thijs angry
                        ts "Iight, Imma just turn a 180 degrees around and walk away"
                        $ characters["thijs"]["hearts"] -= 1
                    $ player["thijs"].append("angle_ts")
                "Does school keep you busy? Or is love also a priority?" if "busy_ts" not in player["thijs"]:
                    if characters["thijs"]["hearts"] > 3:
                        show thijs blush
                        pause
                        ts "For you, it is..."
                        $ characters["thijs"]["hearts"] += 1
                    else:
                        show thijs angry
                        ts "Nah, I'm pretty busy making this game..."
                        $ characters["thijs"]["hearts"] -= 1
                    $ player["thijs"].append("busy_ts")
                "Nevermind...":
                    show thijs neutral
                    jump talk_ts
            jump flirt_ts
        "Say goodbye...":
            menu goodbye_ts:
                "Talk to you later!":
                    if "niceGoodbye" not in player["thijs"]:
                        $ characters["thijs"]["hearts"] += 1
                        $ player["thijs"].append("niceGoodbye")
                    if characters["thijs"]["hearts"] > 2:
                        show thijs happy
                        ts "Adios amigo"
                    elif characters["thijs"]["hearts"] >= 0:
                        show thijs neutral
                        ts "Adios"
                    else:
                        show thijs angry
                        ts "..."
                "See you around!":
                    if characters["thijs"]["hearts"] > 1:
                        show thijs happy
                        ts "Bye bye"
                    else:
                        show thijs angry
                        ts "That != True"
                "Bye.":
                    if characters["thijs"]["hearts"] > 1:
                        show thijs happy
                        ts "Aju paraplu"
                    else:
                        show thijs angry
                        ts "Yep"
            show thijs waving
            pause
            hide thijs
            jump sd_room
    show thijs neutral
    jump talk_ts
            
label lusi:
    show lusi neutral at f11
    with dissolve
    ls "Heya!"
    if "intro" not in player["lusi"]:
        ls "I'm Lusi!"
        $ player["lusi"].append("intro")
    "{i}fast flappy waves{/i}"
    menu questionsStudent_ls:
        "What would you like to ask Lusi as a student?"
        "What are you studying right now?":
            ls "I'm currently studying software development so I can make the dream games I always played!"
            ls "I also do other things on the side, but we don't have to talk about that..."
            if "otherThings" not in player["lusi"]:
                menu otherThings_ls:
                    "Ok.":
                        show lusi happy
                        ls "Ok"
                        $ characters["lusi"]["hearts"] += 1
                    "What things?":
                        show lusi angry
                        ls "Nothing..."
                        "{i}clown noises...{/i}"
                $ player["lusi"].append("otherThings")
            if "questionsStudent" not in player["lusi"]:
                $ player["lusi"].append("questionsStudent")
            show lusi neutral
            jump questionsStudent_ls
        "What's your elective subject?":
            show lusi happy
            ls "My elective subjects are Game design and agile game development."
            ls "I really really really like game design! It's helping me a lot with my own game projects"
            if "questionsStudent" not in player["lusi"]:
                $ player["lusi"].append("questionsStudent")
            show lusi neutral
            jump questionsStudent_ls
        "Do you have a favorite teacher?":
            ls "I do actually! Pieter has always been one of my favorites and he helps me with a lot of my troubles"
            if "teacherPieter_ls" not in player["lusi"]:
                menu teacherPieter_ls:
                    "Pieter? For real?":
                        show lusi angry
                        ls "Yes he is great, what do you want from me?!"
                        $ characters["lusi"]["hearts"] -= 1
                    "Yeah, Pieter is great":
                        show lusi happy
                        ls "Yeah right!"
                        $ characters["lusi"]["hearts"] += 1
                $ player["lusi"].append("teacherPieter_ls")
            ls "and Jorrit is also one of them!"
            if "questionsStudent" not in player["lusi"]:
                $ player["lusi"].append("questionsStudent")
            show lusi neutral
            jump questionsStudent_ls
        "What are they teaching you right now?":
            ls "Well Pieter sadly doesn't give me any lessons right now."
            ls "But Jorrit is my software development and game design teacher."
            ls "I hope he is still my teacher for agile game development!"
            if "jorritAgile" not in player["lusi"]:
                menu jorritAgile_ls:
                    "I hope so too":
                        show lusi happy
                        ls "Thanks!"
                        $ characters["lusi"]["hearts"] += 1
                    "I dont, I hate Jorrit!":
                        show lusi angry
                        show jorrit angry at f11, right
                        with dissolve
                        js "Well, that's just rude!"
                        ls "Yeah, why would you say that?"
                        $ characters["lusi"]["hearts"] -= 1
                        $ characters["jorrit"]["hearts"] -= 1
                        hide jorrit
                $ player["lusi"].append("jorritAgile")
            if "questionsStudent" not in player["lusi"]:
                $ player["lusi"].append("questionsStudent")
            show lusi neutral
            jump questionsStudent_ls
        "Nothing" if "questionsStudent" in player["lusi"]:
            pass
    show lusi neutral
    ls "So, any other questions?"
    menu talk_ls:
        "So, any other questions?"
        "What are your hobbies?":
            ls "I got quite a lot!"
            ls "ready...?"
            ls "Themeparks,"
            ls "gaming"
            ls "game design"
            ls "art"
            ls "Themeparks"
            ls "collecting several things"
            ls "music"
            ls "writing"
            ls "entertainment"
            ls "Themeparks"
            ls "musicals and talking"
            ls "and themeparks..."
            ls "Did I say themeparks already?"
            if "favoriteThemepark" not in player["lusi"]:
                ls "whats your favorite themepark by the way?"
                menu favoriteThemepark:
                    "Whats your favorite themepark?"
                    "EuropaPark":
                        show lusi surprised
                        ls "Seriously! That's the best answer you could give!"
                        u "Do you like it too?"
                        show lusi happy
                        ls "Of course i do! I love it so much! It's one of my biggest comfort places and I love going there! I even have a subscription for it!"
                        $ characters["lusi"]["hearts"] += 1
                    "Walibi":
                        show lusi angry
                        ls "Oh.. cool.."
                        $ characters["lusi"]["hearts"] -= 1
                    "Efteling":
                        show lusi neutral
                        ls "Oh! i actually work there as entertainment!"
                        u "For real?"
                        ls "Yes I do! It's a fun sidejob I have now but I really like puppeteering and entertaining kids! It's still not my favorite tho"
                $ player["lusi"].append("favoriteThemepark")
        "Do you play games?":
            ls "I play quite a few games, my favorite game is any of the Pokemon games but I also really like Hollowknight!"
            show lusi happy
            ls "The design and aesthetic has inspired me a lot to create my own projects!"
            ls "I like playing collecting games and platformers as well."
            u "I like dating simulators"
        "Have any special interests?":
            show lusi happy
            ls "I have loads of special interests! They usually swap around a lot but"
            if "favoriteThemepark" in player["lusi"]:  
                ls "As I told you before... "
            ls "Theme parks have always been my favorite special interest!"
            ls "But along with that I also love musicals and forests!"
            ls "Currently my swapping interests are challenging games and collecting different types of bugs!"
            if "collectingBugs" not in player["lusi"]:
                menu collectingBugs:
                    "Bugs? Ew...":
                        show lusi surprised
                        ls "Dont say that..."
                        $ characters["lusi"]["hearts"] -= 1
                    "Cool!":
                        ls "Yes, I usualy get them from the forest"
                        show lusi happy
                        ls "I like nature."
                        $ characters["lusi"]["hearts"] += 1
                $ player["lusi"].append("collectingBugs")
        "Favorite food?":
            ls "That's a difficult question, it changes all the time! Right now I like anything with chicken meat in it"
            ls "But you can always make me happy with candy!"
            if "candy" not in player["lusi"] and favorite_food == "Candy":
                menu candy_ls:
                    "Do you want to give Lusi some of your candy?"
                    "Yes":
                        show lusi blushing
                        ls "Thank you so much!"
                        $ characters["lusi"]["hearts"] += 1
                    "No":
                        show lusi angry
                        ls "You won't share..."
                        ls "That's very mean"
        "Flirt!" if adult:
            menu flirt_ls:
                "You single?" if "single" not in player["lusi"]:
                    if characters["lusi"]["hearts"] > 2:
                        show lusi blushing
                        ls "Well no, but I am in an open relationship, that was a fun totally random question tho!"
                        $ characters["lusi"]["hearts"] += 1
                        $ player["lusi"].append("single")
                    else:
                        ls "That's odd to randomly ask..."
                "You are really good looking, did you know that?" if "goodLooking" not in player["lusi"]:
                    if characters["lusi"]["hearts"] > 2:
                        show lusi blushing
                        ls "Ahwwww! That's so sweet of you to say! I don't hear compliments like that nowadays!"
                        $ characters["lusi"]["hearts"] += 1
                    else:
                        ls "Oh uhm, thanks? A bit sudden, but still thanks."
                        $ characters["lusi"]["hearts"] -= 1
                    $ player["lusi"].append("goodLooking")
                "Are you a 90 degree angle because you look so right!" if "angle" not in player["lusi"]:
                    if characters["lusi"]["hearts"] > 2:
                        show lusi blushing
                        ls "Nahw that's so sweet! I'll make sure to keep my ion you! Get it? Science jokes!"
                        $ characters["lusi"]["hearts"] += 1
                    else:
                        show lusi angry
                        ls "I guess you tried?..."
                        $ characters["lusi"]["hearts"] -= 1
                    $ player["lusi"].append("angle")
                "Does school keep you busy? Or is love also a priority?" if "busy" not in player["lusi"]:
                    if characters["lusi"]["hearts"] > 2:
                        show lusi blushing
                        ls "Well actually school doesnt keep me that busy, I'm quite fast with doing all my school work!"
                        ls "Its mostly my jobs that keep my busy but I always make sure to have time left over!"
                        $ characters["lusi"]["hearts"] += 1
                    else:
                        show lusi angry
                        ls "Uhm well I have two jobs, I guess those keep me busy."
                        ls "Weird question..."
                        $ characters["lusi"]["hearts"] -= 1
                    $ player["lusi"].append("busy")
                "Nevermind...":
                    show lusi neutral
                    jump talk_ls
            show lusi neutral
            jump flirt_ls
        "Say goodbye":
            menu goodbye_ls:
                "Talk to you later!":
                    if "niceGoodbye" not in player["lusi"]:
                        $ characters["lusi"]["hearts"] += 1
                        $ player["lusi"].append("niceGoodbye")
                    if characters["lusi"]["hearts"] > 1:
                        show lusi happy
                        ls "Hope I'll talk to you again! It was fun talking with you!"
                    else:
                        show lusi angry
                        ls "Oh, I guess we will talk again?"
                "See you around!":
                    if characters["lusi"]["hearts"] > 1:
                        show lusi happy
                        ls "see you later feralgatr! That's a pokemon pun!"
                    else:
                        show lusi angry
                        ls "I'll be around."
                "Bye.":
                    if characters["lusi"]["hearts"] > 1:
                        show lusi happy
                        ls "Bye bye!"
                    else:
                        show lusi angry
                        ls "Goodbye."
            show lusi goodbye
            pause
            hide lusi
            jump sd_room
    show lusi neutral
    jump talk_ls
    
label julia:
    show julia neutral at f11
    with dissolve
    if "intro" not in player["julia"]:
        jl "Hello there! Im Julia, all good?"
        $ player["julia"].append("intro")
    else:
        if characters["julia"]["hearts"] >= 0:
            jl "Hello there! All good?"
        else:
            show julia angry
            jl "Ugh, you again?"
    menu questionsStudent_jl:
        "What would you like to ask Julia as a student?"
        "What are you studying right now?":
            show julia happy
            jl "I'm currently studying Software Development! It's the best subject EVER!"
            if "subject" not in player["julia"]:
                menu subject_jl: 
                    "I think Software Development SUCKS!":
                        show julia angry
                        jl "No, it's THE BEST!"
                        $ characters["julia"]["hearts"] -= 1
                    "I wanna study software development too!":
                        show julia happy
                        jl "OMG, thats awesome!"
                        $ characters["julia"]["hearts"] += 1
                    "I guess it's alright...":
                        show julia neutral
                        jl "I mean, it's pretty cool."
                $ player["julia"].append("subject")
            if "questionsStudent" not in player["julia"]:
                $ player["julia"].append("questionsStudent")
            show julia neutral
            jump questionsStudent_jl
        "What's your elective subject?":
            show julia happy
            jl "I chose Gameplay and Agile"
            jl "Gameplay teaches us how to make good games and how to make the user enjoy them."
            jl "Agile teaches us physical computing, we use Arduinos to make cool gadgets."
            if "questionsStudent" not in player["julia"]:
                $ player["julia"].append("questionsStudent")
            show julia neutral
            jump questionsStudent_jl
        "Do you have a favorite teacher?":
            jl "Don't tell anyone, but Jorrit is my favorite one. He's the greatest!"
            jl "Aaand I heard he's single, you should probably meet him."
            if "intro" in player["jorrit"]:
                u "Oh yeah, I met him!"
                jl "Nice! So I guess his fanclub has one more member? Haha jk"
            if "questionsStudent" not in player["julia"]:
                $ player["julia"].append("questionsStudent")
            show julia neutral
            jump questionsStudent_jl
        "What are they teaching you right now?":
            jl "Right now I'm mainly learning to build games that are enjoyable, just like this one!"
            if "dificultGame" not in player["julia"]:
                menu dificultGame:
                    "Was it difficult to make this game?":
                        jl "Yeah, there is a lot of text we had to make"
                        jl "Aaand Thijs wanted to use Ren'Py to make this"
                        jl "Which is nice! But i now have to use python for this project..."
                        show julia surprised
                        pause
                    "Fame making sounds sooo easy":
                        show julia surprised
                        jl "IT'S NOT! Trust me!"
                        $ characters["julia"]["hearts"] -= 1
                    "I want to make games too":
                        show julia happy
                        jl "Eyy, maybe we can even do a collab one day?"
                        $ characters["julia"]["hearts"] += 1
                $ player["julia"].append("dificultGame")
            if "questionsStudent" not in player["julia"]:
                $ player["julia"].append("questionsStudent")
            show julia neutral
            jump questionsStudent_jl
        "I want to ask something else" if "questionsStudent" in player["julia"]:
            pass
    show julia neutral
    jl "Alright, any other questions?"
    menu talk_jl:
        "Any other questions?"  
        "What are your hobbies?":
            jl "Gaming, drawing, learning new languages... Sometimes even programming!"
            show julia happy
            jl "Building games is really cool, you should give it a try!"
            if "makeAgame" not in player["julia"]:
                menu makeAgame:
                    "I want to!":
                        show julia surprised
                        jl "Nice, I'd recommend using Unity."
                        jl "It's very beginner friendly and there are MANY tutorials online to help you."
                        $ characters["julia"]["hearts"] += 1
                    "I have!":
                        show julia happy
                        jl "Really? Let me play it please!"
                        $ characters["julia"]["hearts"] += 1
                    "Not really my thing":
                        show julia angry
                        jl "Than why are you in the SD room?"
                        $ characters["julia"]["hearts"] -= 1
                $ player["julia"].append("makeAgame")
        "Do you play games?": 
            show julia happy
            jl "I absolutely love playing games! My all-time favorites are Stardew Valley, The Sims, LoL and Forza."
        "Have any special interests?":
            jl "I'm glad you asked! I have many special interests, but my number-one is travelling."
            jl "One of my biggest passions is to explore different countries and learn new languages and cultures!"
            jl "Did you know I'm originally from Brazil?"
            u "No I did not, that's so cool"
            show julia happy
            jl "I came to The Netherlands in 2019 and it was love at first sight. I love it here!"
        "Favorite food?":
            jl "Good question... I think it's actually strogannof"
            if favorite_food == "strogannof" and "strogannofKnow" not in player["julia"]:
                u "No way, I love that!"
                jl "Hmmm, what is it then?"
                menu strogannofKnow:
                    "A famous Russian dish!":
                        show julia surprised
                        jl "Wow. u acualy know it!"
                        jl "I used to eat it a lot as a kid"
                        show julia happy
                        jl "Buuuuut without mushrooms"
                        $ characters["julia"]["hearts"] += 2
                    "A famous Brazilian dish!":
                        show julia happy
                        jl "You're not wrong, we do have that in Brazil!"
                        jl "It's just a bit different, but still absolutely delicious!"
                        $ characters["julia"]["hearts"] += 1
                    "A Dutch dish!":
                        show jullia angry
                        jl "Do you realy think the Dutch have good cuisine?"
                        $ characters["julia"]["hearts"] -= 1
                        u "Yes..."
                        jl "Lmao no"
                        jl "Strogannof is a famous Russian dish that I used to eat a lot as a kid. But without mushrooms!"
                $ player["julia"].append("strogannofKnow")
            else:
                show julia happy
                jl "The Russian dish that I used to eat a lot as a kid. But without mushrooms!"
        "flirt!" if adult:
            menu flirt_jl:
                "You single?":
                    show julia blushing
                    jl "I'm happily married."
                "You are really good looking, did you know that?" if "goodLooking" not in player["julia"]:
                    show julia blushing
                    jl "Yeah, my fiancé tells me that everyday."
                    $ player["julia"].append("goodLooking")
                "Are you a 90 degree angle because you look so right!" if "angle" not in player["julia"]:
                    show julia angry
                    jl "You must be a tree, cause I see you and think leave."
                    $ characters["julia"]["hearts"] -= 1
                    $ player["julia"].append("angle")
                "Does school keep you busy? Or is love also a priority ;)" if "busy" not in player["julia"]:
                    show julia angry
                    jl "What kind of question is that? Go away."
                    $ characters["julia"]["hearts"] -= 1
                    $ player["julia"].append("busy")
                "Nevermind":
                    show julia neutral
                    jump talk_jl
            show julia neutral
            jump flirt_jl
        "Say goodbye":
            menu goodbye_jl:
                "Talk to you later!":
                    if "niceGoodbye" not in player["julia"]:
                        $ characters["julia"]["hearts"] += 1
                        $ player["julia"].append("niceGoodbye")
                    if characters["julia"]["hearts"] > 1:
                        show julia happy
                        jl "Sure, anytime!"
                    else:
                        show julia angry
                        jl "{i}puts headphones on{/i}"
                "See you around!":
                    if characters["julia"]["hearts"] > 1:
                        show julia happy
                        jl "See ya! Make sure to check the DDM place as well!!"
                    else:
                        show julia angry
                        jl "Ugh..."
                "Bye.":
                    if characters["julia"]["hearts"] > 1:
                        show julia happy
                        jl "Bye-bye, have fun!"
                    else:
                        show julia angry
                        jl "Adiós, hasta nunca!"
            show julia waving
            pause
            hide julia
            jump sd_room
    show julia neutral
    jump talk_jl