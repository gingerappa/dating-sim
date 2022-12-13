label ddm_room:
    scene ddm placeholder
    "welcome to the DDM room"
    menu talkToDdm:
        #todo: show all npcs options, dissolve them after choosing
        "Who would you like to talk to?"
        "Enzo":
            jump enzo
        "Someone else":
            jump main
        
label enzo:
    show enzo neutral at left
    with dissolve
    if "intro" not in player["enzo"]:
        e "Hello, student!"
        e "Excited to learn about Sint Lucas?"
        e "By the way, I'm Enzo."
        u "Hey Enzo! Pauline told me to come to the DDM class."
        $ player["enzo"].append("intro")
        $ characters["pauline"]["hearts"] += 1
    else:
        e "Hi again! Need anything?"
    menu questionsWork_e:
        "What would you like to ask Enzo about his job?"
        "What do you teach the students?":
            e "Technically I don't teach the students anything since I'm not a teacher, but I can definitely help them out with 3D and general concepting."
            if "questionsWork_e" not in player["enzo"]:
                $ player["enzo"].append("questionsWork_e")
            jump questionsWork_e
        "Favorite part of your job?":
            e "Interacting with the students, talking with them or helping them out."
            if "jobQuestions_e" not in player["enzo"]:
                menu jobQuestions_e:
                    "That sounds so boring...":
                        show enzo angry
                        pause
                        $ characters["enzo"]["hearts"] -= 1
                    "That's so sweet!":
                        show enzo happy
                        e"Thank you!"
                        $ characters["enzo"]["hearts"] += 1
                $ player["enzo"].append("jobQuestions_e")
            show enzo neutral
            if "questionsWork_e" not in player["enzo"]:
                $ player["enzo"].append("questionsWork_e")
            jump questionsWork_e
        "I want to ask something else" if "questionsWork_e" in player["enzo"]:
            pass
    show enzo neutral
    e"Sure, ask me."
    menu talk_e:
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
                        show enzo irritated
                        pause
                        $ characters["enzo"]["hearts"] -= 1
                $ player["enzo"].append("gym_e")
        "Do you play games?":
                e"Yes, for a while I'vve been playing a lot of CoD MW2, Rocket League, Noita and the binding of Isaac." 
        "Any special interests?":
            show enzo special_interest
            e"I have a special interest in computer hardware and anything that has to do with loud fast cars."
            e"And, of course, the gym."
            $ characters["enzo"]["hearts"] -= 1
        "Favorite food?":
            show enzo happy
            e "My moms Nasi Goreng will forever be the most delicious meal I have ever had!"
            e "But I'm also a big fan of sushi or anything else rice related. "
            if favorite_food == "sushi":
                u "OMG same I love sushi"
                show enzo suprised
                e"Haha nice!"
                $ characters["enzo"]["hearts"] += 1
        "Flirt!" if adult:
            menu flirt_e:
                "Are you single?" if "single" not in player["enzo"]:
                    if characters["enzo"]["hearts"] > 1:
                        show enzo blush
                        e"Yes, I have a severe addiction to gaming and working out, so the touch of a female is something I do not come across very often." 
                        $ characters["enzo"]["hearts"] += 1
                        $ player["enzo"].append("single")
                    else:
                        show enzo angry
                        e"I'm taken!" 
                    
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
                        show enzo irritated
                        e"Goodbye."
            show enzo waving
            window hide
            pause
            hide enzo
            jump ddm_room
    show enzo neutral
    jump talk_e