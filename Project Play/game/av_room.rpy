label av_room:
    scene bg av
    play music "music/class (1).mp3" fadein 1.0 volume 1
    "Welcome to the AV room"
    menu talkToav:
        "Talk to Max":
            jump max
        "Talk to Pauline":
            jump pauline
        "Go away":
            jump main

#Add options  
#if "shivaDialogum" in player["grayson"]:
    #u "Oh, and Shiva told me to say {i}hiya old hag{/i}"
    #$ characters["grayson"]["hearts"] += 1

label max:
    show max neutral at f11

    if "intro" not in player["max"]:
        m "Well, hi!"
        m "I'm Max, nice to meet you."
        u "Hi Max!"
        $ player["max"].append("intro")
        $ characters["max"]["hearts"] += 1
    else:
        e "Hi again! Need anything?"
    menu questionsStudy_max:
        "What would you like to ask Max about his study?"
        "What are you studying right now?":
            m "I'm studying AV!"
            menu studyQuestions_max:
                "What's that?":
                        show max happy
                        m "It's an abbreviation for “Audio Visual”, basically film production. We learn how to make videos from start to end!"
                        $ characters["max"]["hearts"] += 1
                "Zzz":
                        show max angry
                        m "Hey, are you even listening?"
                        $ characters["max"]["hearts"] -= 1
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
                #if "marcusHi" not in player["max"]
                #m "If you see him tell him Marcus said {i}hi kiddo{/i}"
            $ characters["max"]["hearts"] += 1
            $ player["max"].append("games")
        "Favorite food?":
            show max happy
            m "Anything Italian really."
            if favorite_food == "pasta":
                u "Wait, so pasta and such?"
                show max happy
                m "Yes! I love it!"
                u "Same!"
                $ characters["max"]["hearts"] += 1
        "Flirt!" if adult:
            menu flirt_m:
                "Are you single?" if "singlm" not in player["max"]:
                    if characters["max"]["hearts"] > 1:
                        show max blush
                        m "Uhmm, yes why?"
                        $ characters["max"]["hearts"] += 1
                        #Needed? $ player["max"].append("singlm")
                    else:
                        show max angry
                        m "Uhmm, not really." 
                    
                "You are really good looking, did you know that?" if "mwa" not in player["max"]:
                    if characters["max"]["hearts"] > 1:
                        show max blush
                        m "Oh... you think so? Thank you!" 
                        $ characters["max"]["hearts"] += 1
                    else:
                        show max surprised
                        m "I mean.. thanks, I think? This is weird... " 
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
    show pauline neutral at f11
    with dissolve
    p "hey, its you again!"
    if characters["pauline"]["hearts"] > 0:
        p "its nice to see you again"
    else:
        p "..."
    if "intro" not in player["pauline"]:
        $ player["max"].append("intro")
    menu questionsWork_p:
        "What would you like to ask pauline about her job?"
        "What do you teach the Students?":
            p "I teach them softskills and helping students with creating overview."
            menu helpfull_p:
                "o so you basicly do nothing?":
                    show pauline angry
                    p "thats just plain rude!"
                    $ characters["pauline"]["hearts"] -= 1
                "o thats really helpfull!":
                    show pauline happy
                    p "o thank you!"
                    $ characters["pauline"]["hearts"] += 1
            if "questionsWork_p" not in player["pauline"]:
                $ player["pauline"].append("questionsWork_p")
            show pauline neutral
            jump questionsWork_p
        "Favourite part of your job?":
            p "The best thing is to inspire the student to find their inner motivation!"
            u "thats very noble of you"
            show pauline happy
            p "thanks its the reson i got into teaching in the first place!"
            if "questionsWork_p" not in player["pauline"]:
                $ player["pauline"].append("questionsWork_p")
            show pauline neutral
            jump questionsWork_p
        "Is it actually that hard to keep up with grading?":
            p "no"
            #TODO: ask to awnser this question
            if "questionsWork_p" not in player["pauline"]:
                $ player["pauline"].append("questionsWork_p")
            show pauline neutral
            jump questionsWork_p
        "nothing...":
            pass
    show pauline neutral
    p "So, any other questions?"
    menu talk_p:
        "What are your hobbies?":
            p "I really like to go out for dinner and talk with my friends."
            p "I also love walking in nature."
            if "walkingForrest" not in player["pauline"]:
                menu walkingForrest:
                    "o lusi likes that too!" if "collectingBugs" in player["lusi"]:
                        show pauline surprised
                        p "o, thats great!"
                        u "maby we can all go on a walk together?"
                        show pauline happy
                        p "sure!"
                        $ characters["pauline"]["hearts"] += 1
                    "i dont like walking":
                        show pauline angry
                        p "well that too bad, i was going to ask you to join me..."
                        u "o..."
                        $ characters["pauline"]["hearts"] -= 1
                    "maby we can go on a walk together!":
                        show pauline blush
                        p "yes, i would love that..."
                        $ characters["pauline"]["hearts"] += 1
                $ player["pauline"].append("walkingForrest")
        "Do you play games?":
            p "Yes I love games. Board games for sure!"
            #TODO: ask fav board medium and least and add it to a menu
        "Have any special interests?":
            p "no"
            #TODO: ask to awnser this question
        "Favorite food?":
            p "Mmm I love Indonesian food."


            


    

