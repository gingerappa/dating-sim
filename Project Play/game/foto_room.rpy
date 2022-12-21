label foto_room:
    scene bg foto
    play music "music/class (4).mp3" fadein 1.0 volume 1
    show grayson neutral at f11, left
    #show other npc neutral at f11, right
    "Welcome to the Fotografie room!"
    menu talkToFoto:
        #todo: show all npcs options, dissolve them after choosing
        "Who would you like to talk to?"
        "Grayson":
            #hide other npc
            jump grayson
        "Leave the room":
            jump main
        
label grayson:
    show grayson neutral at f11
    with dissolve
    if "intro" not in player["grayson"]:
        gm "What? Need something from me?"
        u "Hi?"
        gm "Hya. Can I help you?"
        u "Yess I'm lost..."
        show grayson angry
        gm "Go to the Lost&Found then."
        $ player["grayson"].append("intro")
    else:
        show grayson angry
        gm "Don't tell me you couldn't find Lost&Found... For fuck's sake"
    menu questionsWork_g:
        "What would you like to ask Grayson about his study?"
        "What are you studying right now?":
            show grayson neutral
            gm "Right now I'm studying DDM aka Digital Design and Motion"
            gm "But I used to study Spatial Design in Boxtel."
            if "questionsWork_g" not in player["grayson"]:
                menu jobQuestions_g:
                    "Wait, what are you doing in the Fotografie room then?":
                        show grayson angry
                        gm "Oh, I was bored, so now I'm visiting this loser Lex"
                        show lex angry
                        l "Hey! I'm listening!"
                        pause
                        hide lex
                    "What are you doing in the Fotografie room then? Got lost? Haha":
                        show grayson happy
                        gm "So you're not all bark no bite then"
                        gm "Hmpf."
                        $ characters["grayson"]["hearts"] += 1
                $ player["grayson"].append("jobQuestions_g")
            show grayson neutral
                $ player["grayson"].append("questionsWork_g")
            jump questionsWork_g
        "Do you have a favorite teacher?":
            gm " have many teachers that I vibe with, but I'd say Kevin Driessen, Enzo Witteveen and Robin Hilt are the teachers I get along with most."
            if "questionsWork_g" not in player["grayson"]:
                $ player["grayson"].append("questionsWork_g")
            jump questionsWork_g
        "I want to ask something else" if "questionsWork_g" in player["grayson"]:
            pass
    show grayson neutral
    gm "Get on with it then."
    menu talk_g:
        "Ask Enzo something"
        "What are your hobbies?":
            e"I love going to the gym, playing games, watching anime, hanging out with friends and going to techno parties."
            show enzo happy
            if "gym_e" not in player["enzo"]:
                e"Do you also hit the gym sometimes?"
                menu gym_e:
                    "Yes!":
                        show enzo blush
                        e"That's really cool!"
                        $ characters["enzo"]["hearts"] += 1
                    "Not really.":
                        e"That's fine, the gym is not for everyone."
                    "No, ew...":
                        show enzo angry
                        pause
                        $ characters["enzo"]["hearts"] -= 1
                $ player["enzo"].append("gym_e")
        "Do you play games?":
                e"Yes, for a while I've been playing a lot of CoD MW2, Rocket League, Noita and the binding of Isaac." 
        "Any special interests?":
            show enzo happy
            e"I have a special interest in computer hardware and anything that has to do with loud fast cars."
            e"And, of course, the gym."
            $ characters["enzo"]["hearts"] -= 1
        "Favorite food?":
            show enzo happy
            e "My moms Nasi Goreng will forever be the most delicious meal I have ever had!"
            e "But I'm also a big fan of sushi or anything else rice related. "
            if favorite_food == "sushi":
                u "OMG same I love sushi"
                show enzo surprised
                e"Haha nice!"
                $ characters["enzo"]["hearts"] += 1
        "Flirt!" if adult:
            menu flirt_e:
                "Are you single?" if "single" not in player["enzo"]:
                    if characters["enzo"]["hearts"] > 1 and pronouns == ["she", "her"]:
                        show enzo blush
                        e"Yes, I have a severe addiction to gaming and working out, so the touch of a female is something I do not come across very often." 
                        $ characters["enzo"]["hearts"] += 1
                        $ player["enzo"].append("single")
                    if characters["enzo"]["hearts"] < 0:
                        show enzo angry
                        e"I'm taken!"
                    if pronouns != ["she", "her"]:
                        show enzo neutral
                        e"Better stop trying, I'm straight" 
                    
                "Any plans for after your'e done working??" if "plans" not in player["enzo"]:
                    if characters["enzo"]["hearts"] > 2:
                        show enzo happy
                        e"No, I'm totally free" 
                        $ characters["enzo"]["hearts"] += 1
                    else:
                        show enzo angry
                        e" Gonna hit the gym, its time for a juicy chest pump." 
                        $ characters["enzo"]["hearts"] -= 1
                    $ player["enzo"].append("plans")

                "If you were my teacher I would be a teachers pet!" if "teachersPet" not in player["enzo"]:
                    if characters["enzo"]["hearts"] > 2:
                        show enzo blush
                        e"I've always wanted a pet that's obedient and listens to me." 
                        $ characters["enzo"]["hearts"] += 1
                    else:
                        show enzo angry
                        "Enzo cringes so hard that everyone around notices... That's not a good thing." 
                        $ characters["enzo"]["hearts"] -= 1
                    $ player["enzo"].append("teachersPet")
                "No more questions, nevermind!":
                    show enzo neutral
                    jump talk_e
            jump flirt_e
        "Time to say goodbye":
            menu goodbye_e:
                "Thanks for talking to me!":
                    if "niceGoodbye" not in player["enzo"]:
                        $ characters["enzo"]["hearts"] += 1
                    if characters["enzo"]["hearts"] >= 0:
                        show enzo neutral
                        e"No problem!"
                    else:
                        show enzo angry
                        e"Bye, kid."
                    $ player["enzo"].append("niceGoodbye")
                "Talk to you later!":
                    if characters["enzo"]["hearts"] > 3:
                        show enzo blush
                        e"Hope to see you at the gym!"
                    else:
                        show enzo neutral
                        e"Alright."
                "Bye":
                    if characters["enzo"]["hearts"] >= 0:
                        show enzo happy
                        e"See you!"
                    else:
                        show enzo angry
                        e"Goodbye."
            show enzo neutral
            window hide
            pause
            hide enzo
            jump ddm_room
    show enzo neutral
    jump talk_e