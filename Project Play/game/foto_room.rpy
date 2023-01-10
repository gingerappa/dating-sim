label foto_room:
    scene bg foto
    play music "music/class (3).mp3" fadein 1.0 volume 1
    show grayson neutral at f11, left
    show lex neutral at f11, right
    "Welcome to the Fotografie room!"
    menu talkToFoto:
        "Who would you like to talk to?"
        "Grayson":
            hide lex
            jump grayson
        "Lex":
            hide grayson
            jump lex
        "Leave the room":
            jump main
        
label grayson:
    show grayson neutral at f11, left
    with move
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
                        show lex angry at midright
                        l "Hey! I'm listening!"
                        hide lex
                        show grayson neutral
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
            gm "I have many teachers that I vibe with, but I'd say Kevin Driessen, Enzo Witteveen and Robin Hilt are the teachers I get along with most."
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
            gm "I do a loooot"
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
            gm"Max from AV dragged me along and now I love it! I play this character Shiva Lentile. The “adoptive” son of Marcus."
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
        "How many hearts do I have with you?":
            show grayson neutral
            $ hgrayson = characters["grayson"]["hearts"]
            if characters["grayson"]["hearts"] > 1:
                gm "You have [hgrayson] hearts, but don't get too excited about it."
            elif characters["grayson"]["hearts"] <= 1:
                gm "[hgrayson]. You suck."
        "Flirt!" if adult:
            menu flirt_g:
                "Are you single?" if "single" not in player["grayson"]:
                    if characters["grayson"]["hearts"] > 1:
                        show grayson blushing
                        gm "I am. Why, asking for a friend?" 
                        $ characters["grayson"]["hearts"] += 1
                        $ player["grayson"].append("single")
                    if characters["grayson"]["hearts"] < 1:
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
            jump foto_room
    show grayson neutral
    jump talk_g

label lex:
    show lex happy at f11, left
    with move
    if "intro" not in player["lex"]:
        l "Hiiii"
        l "I'm Lex, nice to meet you!"
        u "Hey Lex!"
        $ player["lex"].append("intro")
    else:
        l "Hello hello!"
    menu questionsWork_l:
        "What would you like to ask Lex as a student?"
        "What are you studying right now?":
            l "I'm studying Photography right now and I am a second year student."
            if "questionsWork_l" not in player["lex"]:
                $ player["lex"].append("questionsWork_l")
                menu elective:
                    "Cool! What's your elective subject?":
                        l "At photography they don't really do elective subjects unlike the other studies here. But we do have Photography focused subjects!"
                        l "Right now, we're focusing on {i}Software Verdieping{/i}"
                    "Nice!":
                        l "Yeah, right?"
            show lex neutral
            jump questionsWork_l
        "Do you have a favorite teacher?":
            l "Well, I have two main teachers in photography so I would say they're both my favorite."
            show lex happy
            if "jobQuestions_l" not in player["lex"]:
                menu jobQuestions_l:
                    "What are they teaching you right now?":
                        show lex happy
                        $ characters["lex"]["hearts"] += 1
                        l "Oh, my favorite teachers? They're my mentors but they also just teach me photography stuff."
                    "...":
                        show lex neutral
                        l "..."
                $ player["lex"].append("jobQuestions_l")
            if "questionsWork_l" not in player["lex"]:
                $ player["lex"].append("questionsWork_l")
            show lex neutral
            jump questionsWork_l
        "Something else" if "questionsWork_l" in player["lex"]:
            pass
    show lex neutral
    l "So, any other questions?"
    menu talk_l:
        "So, any other questions?"
        "What are your hobbies?":
            l "I like gaming a lot, but when I'm not gaming I like to read."
            l "Of course, I also like taking pictures of friends and fumbling with my analog cameras."
            $ player["lex"].append("hobbies")
        "Do you play games?":
            if "hobbies" in player["lex"]:
                l "As I said before..." 
            l "Yes, absolutely!"
            l "I mostly play Sea of Thieves, Fortnite… yeah, I know its cringe. Valorant and hades are also up there."
            l "But once every now and then I fuck around in Overwatch with Grayson from DDM"
            if "intro" in player["grayson"]:
                u "Oh, Grayson..."
                show lex surprised
                l "Wait, I saw you talking to him before!"
                l "Dont mind him being rude, thats just.. {i}his thing.{/i}"
        "Any special interests?":
            show lex happy
            l "My analog cameras! I really love them, it's fun to just fuck around and find out what the next picture is gonna look like. It's a gamble but the vibe makes up for it."
            l "My favorite camera right now Is my rolleicord, it makes absolutely stunning pictures every single time."
            show lex blushing
            l "But hot buff fantasy woman also pique my interest. Like, have you seen Lexa from the hundred??? {b}MY GOD.{/b}"
        "Favorite food?":
            l "I really like sushi, but just any dish from Asia is also very good."
            if favorite_food == "sushi":
                u "Yeah, me too."
                show lex surprised
                l "Meow! That's amazing"
        "How many hearts do I have with you?":
            show lex neutral
            $ hlex = characters["lex"]["hearts"]
            if characters["lex"]["hearts"] > 1:
                l "You have [hlex] hearts."
            elif characters["lex"]["hearts"] <= 1:
                l "I think you have [hlex], actually."
        "Flirt!" if adult:
            l "Try your best!"
            menu flirt_l:
                "Are you single?" if "single" not in player["lex"]:
                    if characters["lex"]["hearts"] > 1 and pronouns == ["she", "her"]:
                        show lex blushing
                        l "Yes, I am!" 
                        $ characters["lex"]["hearts"] += 1
                    elif characters["lex"]["hearts"] < 1 and pronouns == ["she", "her"]:
                        show lex neutral
                        l "I'm talking to someone right now, why are you asking exactly?"
                    if pronouns != ["she", "her"]:
                        l "I only do women, don't get your hopes up."
                    $ player["lex"].append("single")
                "You are really good looking, did you know that?" if "plans" not in player["lex"] and pronouns == ["she", "her"]:
                    if characters["lex"]["hearts"] > 1:
                        show lex blushing
                        l "Ah thank you, you don't look too bad yourself you know?" 
                        $ characters["lex"]["hearts"] += 1
                    else:
                        show lex angry
                        l "Uhm.. right sure, thanks?" 
                        $ characters["lex"]["hearts"] -= 1
                    $ player["lex"].append("plans")
                "If I could rearrange the alphabet? I'd put ‘u’ and ‘I’ together." if "alphabet" not in player["lex"] and pronouns == ["she", "her"]:
                    if characters["lex"]["hearts"] > 1:
                        show lex blushing
                        "Lex blushes really hard. That was very effective!" 
                        $ characters["lex"]["hearts"] += 2
                    else:
                        show lex angry
                        l "I like the alphabet the way it is" 
                        $ characters["lex"]["hearts"] -= 1
                    $ player["lex"].append("alphabet")
                "Why can't I flirt with you..?" if pronouns != ["she", "her"]:
                    show lex neutral
                    l "I'm not attracted to you, don't take it personally."
                "Return":
                    show lex neutral
                    jump talk_l
            jump flirt_l
        "Say goodbye":
            menu goodbye_l:
                "See you around!":
                    if "niceGoodbye" not in player["lex"]:
                        $ characters["lex"]["hearts"] += 1
                        $ player["lex"].append("niceGoodbye")
                    if characters["lex"]["hearts"] >= 0:
                        show lex goodbye
                        l "MEOW! See you later alligator!"
                    else:
                        show lex goodbye
                        l "Mmhm sure yeah whatever"
                "Talk to you later!":
                    if characters["lex"]["hearts"] > 1:
                        show lex goodbye
                        l "MEOW! You know where to find me!"
                    else:
                        show lex goodbye
                        l "Please don't"
                "Bye":
                    if characters["lex"]["hearts"] >= 0:
                        show lex goodbye
                        l "MEOW!"
                    else:
                        show lex goodbye
                        l "Goodbye forever, {i}weirdo.{/i}"
            jump foto_room
    show lex neutral
    jump talk_l
