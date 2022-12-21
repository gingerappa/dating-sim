label ddm_room:
    scene bg ddm
    play music "music/class (2).mp3" fadein 1.0 volume 1
    "Welcome to the DDM room!"
    menu talkToDdm:
        #todo: show all npcs options, dissolve them after choosing
        "Who would you like to talk to?"
        "Enzo":
            jump enzo
        "Kevin":
            jump kevin
        "Leave the room":
            jump main
        
        #todo: enzo says he's straight, tells you to stop trying 

label enzo:
    show enzo neutral at f11
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
                e"Yes, for a while I've been playing a lot of CoD MW2, Rocket League, Noita and the binding of Isaac." 
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
    
label kevin:
    show kevin neutral at f11
    with dissolve
    if "intro" not in player["kevin"]:
        kd "Hi!"
        kd "I'm Kevin, you probably heard about me already."
        u "Hey Kevin! OMG I was so excited to see you here!"
        kd "Everyone is playing this just to talk to me, tsc tsc"
        $ player["kevin"].append("intro")
        $ characters["kevin"]["hearts"] += 1
    else:
        kd "Hello! Anything new?"
    menu questionsWork_k:
        "What would you like to ask Kevin about his job?"
        "What do you teach the students?":
            kd "I teach my students 3D modelling and Texturing."
            if "questionsWork_e" not in player["kevin"]:
                $ player["kevin"].append("questionsWork_k")
            jump questionsWork_k
        "Favorite part of your job?":
            kd "My favorite part is joking around with students and colleagues."
            if "jobQuestions_k" not in player["kevin"]:
                menu jobQuestions_k:
                    "Really? You seem so serious tho":
                        show kevin angry
                        kd "Is that a bad thing?"
                        $ characters["kevin"]["hearts"] -= 1
                    "So that's why everyone loves you!":
                        show kevin happy
                        kd"I guess so? Haha"
                        $ characters["kevin"]["hearts"] += 1
                $ player["kevin"].append("jobQuestions_k")
            show kevin neutral
            if "questionsWork_k" not in player["kevin"]:
                $ player["kevin"].append("questionsWork_k")
            jump questionsWork_k
        "I want to ask something else" if "questionsWork_k" in player["kevin"]:
            pass
    show kevin neutral
    kd "Go on then."
    menu talk_k:
        "Ask Kevin something"
        "What are your hobbies?":
            kd "My hobbies are playing guitar and bass as well as playing baseball."
            show kevin happy
            if "dream_k" not in player["kevin"]:
                show kevin neutral
                kd "What do you think of that, huh?"
                menu dream_k:
                    "It's just like a dream":
                        show kevin blush
                        kd "Staawp!"
                        $ characters["kevin"]["hearts"] += 1
                    "It's nice":
                        kd"Thanks, thanks"
                    "Veeery boring":
                        show kevin angry
                        pause
                        $ characters["kevin"]["hearts"] -= 1
                $ player["kevin"].append("dream_k")
        "Do you play games?":
                kd "I have very little spare time, but when I do I usually play Gears of War competitive." 
        "Any special interests?":
            show kevin happy
            kd "I am in love with the work made by ILM and movie scores by Hans Zimmer."
            $ characters["kevin"]["hearts"] += 1
        "Favorite food?":
            show kevin happy
            kd "My favorite food is a good warm bowl of udon noodles with teriyaki sauce and vegetables!"
            if favorite_food == "noodles":
                u "Slay! Same!"
                show enzo suprised
                kd "Haha nice!"
                $ characters["kevin"]["hearts"] += 1
        "Flirt!" if adult:
            menu flirt_k:
                "Are you single?" if "single" not in player["kevin"]:
                    if characters["kevin"]["hearts"] > 1:
                        show kevin blush
                        kd "For you I am!" 
                        $ characters["kevin"]["hearts"] += 1
                        $ player["kevin"].append("single")
                    if characters["kevin"]["hearts"] < 0:
                        show kevin angry
                        e"You're too short for me."                   
                "Any plans for after your'e done working??" if "plans" not in player["kevin"]:
                    if characters["kevin"]["hearts"] > 1:
                        show kevin happy
                        kd"Well… I'm planning on taking you home with me." 
                        $ characters["kevin"]["hearts"] += 2
                    else:
                        show kevin neutral
                        kd"Ohhh sorry I'm not looking for a relationship right now." 
                    $ player["kevin"].append("plans")

                "If you were my teacher I would be a teachers pet!" if "teachersPet" not in player["kevin"]:
                    if characters["kevin"]["hearts"] > 1:
                        show kevin happy
                        kd "Would you be willing to wear a leash and sit by my side all day?"
                        u "Woof woof!" 
                        show kevin blush
                        kd "Good."
                        show kevin happy
                        $ characters["kevin"]["hearts"] += 2
                    else:
                        show kevin angry
                        "Go kiss some other ass. You are not getting a better grade." 
                        $ characters["kevin"]["hearts"] -= 1
                    $ player["kevin"].append("teachersPet")
                "Nevermind!":
                    show kevin neutral
                    jump talk_k
            jump flirt_k
        "Time to say goodbye":
            menu goodbye_k:
                "Thanks for talking to me!":
                    if "niceGoodbye" not in player["kevin"]:
                        $ characters["kevin"]["hearts"] += 1
                    if characters["kevin"]["hearts"] >= 0:
                        show kevin happy
                        kd"My pleasure!"
                    else:
                        show kevin angry
                        kd"Just go, bye."
                    $ player["kevin"].append("niceGoodbye")
                "Bye":
                    show kevin neutral
                    e "Bye!"
            show kevin neutral
            window hide
            pause
            hide kevin
            jump ddm_room
    show kevin neutral
    jump talk_k