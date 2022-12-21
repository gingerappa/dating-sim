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
        "Ask Grayson something"
        "What are your hobbies?":
            gm "I do a loooot."
            show grayson happy
            gm "I play DnD, gaming, drawing but I also enjoy creative writing! These are just the main things I like to do with the little free time I get."
            if "dnd" not in player["grayson"]:
                menu dnd:
                    "What a nerd!":
                        show grayson neutral
                        gm "Takes one to notice one."
                    "DnD is super cool!":
                        show grayson happy
                        gm "Damn right it is baby."
                        $ characters["grayson"]["hearts"] += 1
                    "Ew...":
                        show grayson angry
                        gm "That's the same response I gave when I smelled your breath."
                        $ characters["grayson"]["hearts"] -= 1
                $ player["grayson"].append("dnd")
        "Do you play games?":
                gm "Of course I do!"
                gm "Matter of fact, I used to play Overwatch professionally. For 2 years in a row I managed to generally stay in top 200 Europe support role! I played with a team for 2,5 years."
                gm "Don't tell anyone btw, I used to suck absolute ass at the game. I was an adopt a bronze. Ah, the good ol' days."
                gm "Nowadays I carry Lex from photography. This man plays rein on shift cooldown…"
        "Any special interests?":
            show grayson happy
            gm"Larping! Once I month I do Vampire Larp."
            show grayson special interest
            e"Max from AV dragged me along and now I love it! I play this character Shiva Lentile. The “adoptive” son of Marcus."
            $ characters["grayson"]["hearts"] += 1
            if "shiva" not in player["grayson"]:
                gm "If you see Max? Tell him that Shiva said {i}hiya old hag{/i}" 
                u "Okay! Will do!"
                show grayson blushing
                gm "So obedient, I like that."
                $ player["grayson"].append("shiva")
        "Favorite food?":
            show grayson surprised
            gm "Fuuuuck, I wouldn't say I have a favourite food."
            gm "Mainly because eating just about anything while being high? Everything fucking slaps."
            gm "But if you really must know? Sushi has a special place in my heart."
            if favorite_food == "sushi":
                u "Oh wow! I love sushi"
                show grayson happy
                gm "Let's be real. If you don't, you're crazy."
                $ characters["grayson"]["hearts"] += 1
        "I spoke to Max!" if "marcushi" in player["max"]:
            show grayson surprised
            gm "What did the cumwipe have to say for himself"
            u "You're so mean!"
            show grayson happy
            gm "Hahah, I knew he was going to say that. But in all seriousness? Being mean is my love language, take it as a compliment kay?" 
            u "No, wait... Nevermind"
            u "Marcus told me to say {i}hi kiddo{/i}"
            show grayson special interest
            if "shiva" not in player["grayson"]:
                gm "Well, tell Max that Shiva said {i}hiya old hag{/i}"
                u "Okay! Will do!"
                show grayson blushing
                gm "So obedient, I like that."
                $ player["grayson"].append("shiva")
            if "shiva" in player["grayson"] and "marcushi" in player["max"] :
                show grayson blushing
                gm "What a nice errand runner you are, you could be a fit for the Sciarpa Rossa, consider it."
            if "marcushi" not in player["max"]:
                m "If you see him again, tell him Marcus said {i}hi kiddo{/i}"
                show max neutral
                $ player["max"].append("marcushi")
        "Flirt!" if adult:
            menu flirt_g:
                "Are you single?" if "single" not in player["grayson"]:
                    if characters["grayson"]["hearts"] > 1:
                        show grayson blushing
                        gm "I am. Why, asking for a friend?" 
                        $ characters["grayson"]["hearts"] += 1
                        $ player["grayson"].append("single")
                    if characters["grayson"]["hearts"] < 0:
                        show grayson angry
                        gm "Not for you, try again."
                "You are really good looking, did you know that?" if "plans" not in player["grayson"]:
                    if characters["grayson"]["hearts"] > 2:
                        show grayson blushing
                        gm "Why thank you, big compliment coming from a shining star like you. " 
                        $ characters["grayson"]["hearts"] += 1
                    else:
                        show grayson angry
                        gm "Thanks? Anyways… *visible cringe* " 
                        $ characters["grayson"]["hearts"] -= 1
                    $ player["grayson"].append("plans")

                "Are you a 90 degree angle because you look so right!" if "teachersPet" not in player["grayson"]:
                    if characters["grayson"]["hearts"] > 2:
                        show grayson blushing
                        gm "I might be! Does that mean I'm also very hot?" 
                        $ characters["grayson"]["hearts"] += 1
                    else:
                        show grayson angry
                        gm "Do I look like I'm the type to enjoy science jokes? {i}*scoff*{/i}" 
                        $ characters["grayson"]["hearts"] -= 1
                    $ player["grayson"].append("teachersPet")
                "No more questions, nevermind!":
                    show grayson neutral
                    jump talk_g
            jump flirt_g
        "Time to say goodbye":
            menu goodbye_g:
                "Talk to you later!":
                    if characters["grayson"]["hearts"] > 3:
                        show grayson blushing
                        gm"I'll be around!"
                    else:
                        show grayson angry
                        gm"For the love of god? Fuck off."
                "Bye":
                    if characters["grayson"]["hearts"] >= 0:
                        show grayson happy
                        gm"Seeya!"
                    else:
                        show grayson angry
                        gm"Bye."
            show grayson neutral
            window hide
            pause
            hide grayson
            jump foto_room
    show grayson neutral
    jump talk_g