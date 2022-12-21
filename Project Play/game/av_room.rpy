label av_room:
    scene bg av
    play music "music/class (1).mp3" fadein 1.0 volume 1
    "Welcome to the AV room"
    menu talkToav:
        "Talk to Max":
            jump max
        #"Talk to Paulinm":
            #jump pauline
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
            if "marcushi" not in player["max"]:
                m "If you see him tell him Marcus said {i}hi kiddo{/i}"
            $ characters["max"]["hearts"] += 1
            $ player["max"].append("games")
        "Favorite food?":
            show max happy
            m "Anything Italian really."
            if favorite_food == "italian":
                u "Wait, so pasta and such?"
                show max happy
                m "Yes! I love it!"
                u "Same!"
                $ characters["max"]["hearts"] += 1
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