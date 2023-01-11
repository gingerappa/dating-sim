label av_room:
    scene bg av
    play music "music/class (4).mp3" fadein 1.0 volume 1
    show max neutral at f11, left
    show pauline neutral at f11, right
    "Welcome to the AV room"
    menu talkToav:
        "Talk to Max":
            hide pauline
            jump max
        "Talk to Pauline":
            hide max
            jump pauline
        "Go away":
            jump main

label max:
    show max neutral at f11

    if "intro" not in player["max"]:
        m "Well, hi!"
        m "I'm Max, nice to meet you."
        u "Hi Max!"
        $ player["max"].append("intro")
        $ characters["max"]["hearts"] += 1
    else:
        m "Hi again! Need anything?"
    menu questionsStudy_max:
        "What would you like to ask Max about his study?"
        "What are you studying right now?":
            m "I'm studying AV!"
            if "studyQuestions" not in player["max"]:
                menu studyQuestions_max:
                    "What's that?":
                            show max happy
                            m "It's an abbreviation for “Audio Visual”, basically film production. We learn how to make videos from start to end!"
                            $ characters["max"]["hearts"] += 1
                    "Zzz":
                            show max angry
                            m "Hey, are you even listening?"
                            $ characters["max"]["hearts"] -= 1
                player["max"].append("studyQuestions")
            if "studyQuestions_max" not in player["max"]:
                $ player["max"].append("studyQuestions_max")
            jump questionsStudy_max
        "Do you have a favorite teacher?":
            show max surprised
            m "..."
            m "I won't say that unless you sign this NDA agreement right here."
            show max happy
            m "Okaaay fine, it's Mieke Janssen."
            u "Oh! Are they also here today?"
            show max surprised
            m "Sadly not..."
            if "questionsStudy_max" not in player["max"]:
                $ player["max"].append("questionsStudy_max")
            jump questionsStudy_max
        "What are they teaching you right now?":
            show max happy
            m "I'm learning {i}vormgeving&Beeldgebruik{/i} which is all about the storytelling aspect of AV."
            if "questionsStudy_max" not in player["max"]:
                $ player["max"].append("questionsStudy_max")
            jump questionsStudy_max
        "I want to ask something else" if "questionsStudy_max" in player["max"]:
            pass
    show max neutral
    m"Sure, ask me."
    menu talk_m:
        "Ask Max something!"
        "What are your hobbies?":
            show max happy
            m "Well, I'm big into anything related to roleplaying!"
            m "So: Dungeons&Dragons, Vampire: The Masquerade, Warhammer 40k, Live Action Role Play {i}or, LARP, for short{/i}."
            if "games" not in player["max"]:
                u "Do you also play games sometimes?"
                m "Yeah, mostly single player story games."
                $ player["max"].append("games")
        "Any special interests?":
            show max special interest
            m "Vampire: the Masquerade is my biggest special interest at the moment!"
            m "It's a roleplaying game about political intrigue and character drama, once a month I go to a club in Haarlem where we LARP this game."
            m "I play an Italian gangster. It's very fun. I do this with Grayson from DDM actually! He kinda plays my son."
            if "marcushi" not in player["max"]:
                m "If you see him tell him Marcus said {i}hi kiddo{/i}"
            if "games" not in player["max"]:
                $ characters["max"]["hearts"] += 1
                $ player["max"].append("games")
        "Favorite food?":
            show max happy
            m "Anything Italian really."
            if favorite_food == "italian" and food not in player["max"]:
                u "Wait, so pasta and such?"
                show max happy
                m "Yes! I love it!"
                u "Same!"
                $ characters["max"]["hearts"] += 1
                $ player["max"].append("food")
        "I spoke to Grayson!" if "shiva" in player["grayson"]:
            show max surprised
            m "Oh, you did?"
            u "Yes! Oh, and he told me to tell you that Shiva said {i}hiya old hag{/i}"
            show max special interest
            m "Ahaha, that's my boy."
            if "marcushi" not in player["max"]:
                m "If you see him again, tell him Marcus said {i}hi kiddo{/i}"
                show max neutral
                $ player["max"].append("marcushi")
        "How many hearts do I have with you?":
            show max neutral
            $ hmax = characters["max"]["hearts"]
            if characters["max"]["hearts"] > 1:
                m "Right now, you have... [hmax] hearts."
            elif characters["max"]["hearts"] <= 1:
                m "Right now, you have... [hmax] heart."
        "Flirt!" if adult:
            menu flirt_m:
                "Are you single?" if "singlm" not in player["max"]:
                    if characters["max"]["hearts"] > 1:
                        show max blush
                        m "Uhmm, yes why?"
                        $ characters["max"]["hearts"] += 1
                        $ player["max"].append("singlm")
                    else:
                        show max angry
                        m "Uhmm, not really." 
                    
                "You are really good looking, did you know that?" if "mwa" not in player["max"]:
                    if characters["max"]["hearts"] > 1:
                        show max blush
                        m "Oh… you think so? Thank you!" 
                        $ characters["max"]["hearts"] += 1
                    else:
                        show max surprised
                        m "I mean.. thanks, I think? This is weird… " 
                        $ characters["max"]["hearts"] -= 1
                    $ player["max"].append("mwa")

                "Are you a 90 degree angle? Because you look so right!" if "angle" not in player["max"]:
                    if characters["max"]["hearts"] > 2:
                        show max blush
                        m"Are you wifi? Because I'm feeling a connection here." 
                        $ characters["max"]["hearts"] += 1
                    else:
                        show max angry
                        m "Dude, cut it out." 
                        $ characters["max"]["hearts"] -= 1
                    $ player["max"].append("angle")
                "No more questions, nevermind!":
                    show max neutral
                    jump talk_m
            jump flirt_m
        "Time to say goodbye":
            menu goodbye_m:
                "Talk to you later!":
                    if "niceGoodbye" not in player["max"]:
                        $ characters["max"]["hearts"] += 1
                    if characters["max"]["hearts"] >= 0:
                        show max happy
                        m"Yeah, alright! See ya!"
                    else:
                        show max angry
                        m" No need for that."
                    $ player["max"].append("niceGoodbye")

                "Bye":
                    if characters["max"]["hearts"] >= 0:
                        show max happy
                        m"Ciao ciao!"
                    else:
                        show max irritated
                        m"Finally."
            window hide
            pause
            hide max
            jump av_room
    jump talk_m

label pauline:
    show pauline neutral at f11, left
    with dissolve
    p "Hey, its you again!"
    if characters["pauline"]["hearts"] > 0:
        p "It's nice to see you again."
    else:
        p "..."
    if "intro" not in player["pauline"]:
        $ player["pauline"].append("intro")
    menu questionsWork_p:
        "What would you like to ask Pauline about her job?"
        "What do you teach the students?":
            p "I teach them softskills and help students with creating overview."
            menu helpfull_p:
                "Oh, so you basicly do nothing?":
                    show pauline angry
                    p "That's just plain rude!"
                    $ characters["pauline"]["hearts"] -= 1
                "Oh, thats really helpful!":
                    show pauline happy
                    p "Thank you!"
                    $ characters["pauline"]["hearts"] += 1
            if "questionsWork_p" not in player["pauline"]:
                $ player["pauline"].append("questionsWork_p")
            show pauline neutral
            jump questionsWork_p
        "Favourite part of your job?":
            p "The best thing is to inspire the student to find their inner motivation!"
            u "Thats very noble of you"
            show pauline happy
            p "Thanks, it's the reason I got into teaching in the first place!"
            if "questionsWork_p" not in player["pauline"]:
                $ player["pauline"].append("questionsWork_p")
            show pauline neutral
            jump questionsWork_p
        "Nothing.":
            pass
    show pauline neutral
    p "So, any other questions?"
    menu talk_p:
        "What are your hobbies?":
            p "I really like to go out for dinner and chat with my friends."
            p "I also love walking in nature."
            if "walkingForrest" not in player["pauline"]:
                menu walkingForrest:
                    "Lusi likes that too!" if "collectingBugs" in player["lusi"]:
                        show pauline surprised
                        p "Haha, thats great!"
                        u "Maybe we can all go on a walk together?"
                        show pauline happy
                        p "Sure!"
                        $ characters["pauline"]["hearts"] += 1
                    "I dont like walking":
                        show pauline angry
                        p "Well,t too bad... I was going to ask you to join me..."
                        u "Ah..."
                        $ characters["pauline"]["hearts"] -= 1
                    "Maybe we can go on a walk together!":
                        show pauline blush
                        p "Yes, I would love that!"
                        $ characters["pauline"]["hearts"] += 1
                $ player["pauline"].append("walkingForrest")
        "Do you play games?":
            p "Yes I love games. Board games for sure!"
            $ characters["pauline"]["hearts"] += 1
        "Favorite food?":
            p "Mmm I love Indonesian food."
            if "foodnice" not in player["pauline"]:
                menu food_p:
                    "Oh, I think it's too spicy":
                        show pauline surprised
                        p "Just get some milk!"
                        $ player["pauline"].append("foodnice")
                    "It's alright...":
                        show pauline happy
                        p "Yea right!"
                        $ characters["pauline"]["hearts"] += 1
                        $ player["pauline"].append("foodnice")
                    "I LOVE IT" if favorite_food == "Indonesian":
                        show pauline blush
                        p "Me too!"
                        $ characters["pauline"]["hearts"] += 1
                        $ player["pauline"].append("foodnice")
        "How many hearts do I have with you?":
            show pauline neutral
            $ hp = characters["pauline"]["hearts"]
            if characters["pauline"]["hearts"] > 1:
                p "You [hp] hearts, love"
            elif characters["pauline"]["hearts"] <= 1:
                p "Your score is [hp]."
        "Flirt!" if adult:
            menu flirt_p:
                "Are you single?" if "single" not in player["pauline"]:
                    if characters["pauline"]["hearts"] > 1:
                        show pauline blushing
                        p "Yes, my love." 
                        $ characters["pauline"]["hearts"] += 1
                        $ player["pauline"].append("single")
                    if characters["pauline"]["hearts"] < 1:
                        show pauline angry
                        p "Uh… Nope."     
                        $ player["pauline"].append("single")               
                "Any plans for after your'e done working??" if "plans" not in player["pauline"]:
                    if characters["pauline"]["hearts"] > 2:
                        show pauline blushing
                        p "I have no plans, my love" 
                        $ characters["pauline"]["hearts"] += 1
                    else:
                        show pauline angry
                        p "Sleeping! Alone!!" 
                        $ characters["pauline"]["hearts"] -= 1
                    $ player["pauline"].append("plans")

                "If you were my teacher I would be a teachers pet!" if "teachersPet" not in player["pauline"]:
                    if characters["pauline"]["hearts"] > 2:
                        show pauline blushing
                        p "Tell me more!" 
                        u "Oh!"
                        $ characters["pauline"]["hearts"] += 1
                    else:
                        show pauline angry
                        p "I don't like pets." 
                        $ characters["pauline"]["hearts"] -= 1
                    $ player["pauline"].append("teachersPet")
                "Are you a loan, because you are gaining my interest." if "loan" not in player["pauline"]:
                    if characters["pauline"]["hearts"] > 2:
                        show pauline blushing
                        p "You read my mind. I'm also into you!" 
                        $ characters["pauline"]["hearts"] += 1
                    else:
                        show pauline angry
                        p "Ugh. Try harder." 
                        $ characters["pauline"]["hearts"] -= 1
                    $ player["pauline"].append("teachersPet")
                "No more questions, nevermind!":
                    show pauline neutral
                    jump talk_p
            jump flirt_p
        "Goodbye!":
            show pauline neutral
            p "Bye!"
            window hide
            hide pauline
            jump av_room
    show pauline neutral
    jump talk_p