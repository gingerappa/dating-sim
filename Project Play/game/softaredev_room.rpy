#Defining characters

define js = Character("Jorrit Slaats")
define u = Character("You")
#define g = Character("Game devs")

# The game starts here.

label sd_room:
    scene Placeholder
    "welcome to SD room"
    jump jorrit


label jorrit:
    show js neutral at right
    with dissolve

    js "Hey, welcome!"
    js "I assume you're the future student Pauline told me about"
    js "Let me introduce myself…"
    js "I'm Jorrit, nice to meet you."
    u "Hi Jorrit! Nice to meet you too!"

    menu questionsWork_js:
        "What would you like to ask Jorrit?"

        "What do you teach the students?":
            js "I teach Software development and the elective subject Gameplay."
        "Favorite part of your job?":
            js "I've always enjoyed programming..."
            js "however, I tend to get tired of it when I do it for long periods at a time."
            js "The best part about working as a software development teacher is that I can combine my love for development with a ton of different working activities and tons of social interactions"

            "Is it actually that hard to keep up with grading?"
            show js happy 
            js "Depends on what you are grading and how you are grading!"
            js "Just writing V, G, O, V, V, in Magister is a lot less effort than giving useful feedback."
            js "Also, downloading big Unity projects or Blender files and waiting for the slow programs to open and close can eat up a bunch of time. Work smart!"
            menu jobQuestions_js:
                "wow that sounds realy easy":
                    show js angry
                    $ characters["jorrit"]["hearts"] -= 1
                "u seem like a great teacher":
                    show js happy
                    $ characters["jorrit"]["hearts"] += 1
    js "So, any other questions?"
    menu talk_js:
        "What are your hobbies?":
            js "I play Dungeons&Dragons once or twice a week! {i}As long as scheduling doesn't ruin everything...{/i}"
            js "Recently I've also discovered a new hobby in using AI's to generate art."
            show js blush
            js "Of course I also like to play games which was one of the reasons that got me into development in the first place."
            $ characters["jorrit"]["askedHobbies"] = True
            js "I listen to a bunch of music, but like, who doesn't?"
            js "Lastly, I like making cocktails. However I don't do it that often since I only do so at parties."
            if adult:
                js "Would you like a cocktail?"
                menu wantDrink_js:
                    "Yes":
                        js "Here you go!"
                        "Jorrit hands you a drink"
                        $ character["jorrit"]["hearts"] += 1
                    "No":
                        js "Thats alright."
        "Do you play games?":
            if characters["jorrit"]["askedHobbies"]:
                js "As I said before..." 
            js "Quite frequently still!"
            #he tells all the games he plays

        "Any special interests?":
            js "AI image generation, Dungeons and dragons..." 
            js "i also love animals!"
            menu animalMenu_js:
                "Me too i love cats!":
                    show js happy
                    js "Oh yea cats are pretty awesome!"
                    $ characters["jorrit"]["hearts"] += 1
                "Me too i love dogs!":
                    show js angry
                    js "O yea i guese they exist too..."
                    $ characters["jorrit"]["hearts"] -= 1
                "i dont realy like animals...":
                    show js neutral
                    js "o, thats alright"

        
        "Favorite food?":
            js "I love a proper hamburger! Not some McDonald's hamburger, but a good one."
        "flirt!" if adult:
            menu flirt_js:
                "Are you single?":
                    if characters["jorrit"]["hearts"] > 3:
                        show js blush
                        js "As a pringle!" 
                        $ characters["jorrit"]["hearts"] += 1
                    else:
                        show js angry
                        js "Maybe you should ask again when I'm in a better mood." 
                        $ characters["jorrit"]["hearts"] -= 1

                    
                "Any plans for after your'e done working??":
                    if characters["jorrit"]["hearts"] > 2:
                        show js happy
                        js "I'll probably visit some friends during the weekend!" 
                        $ characters["jorrit"]["hearts"] += 1
                    else:
                        show js angry
                        js "You mean for when I retire!? Do you really think I look that old???" 
                        $ characters["jorrit"]["hearts"] -= 1

                "If you were my teacher I would be a teachers pet!":
                    if if characters["jorrit"]["hearts"] > 4:
                        show js blush
                        js "If you are thinking of bringing me an apple, make sure to bring a green one!" 
                        $ characters["jorrit"]["hearts"] += 1
                    else:
                        show js angry
                        js "If I was your teacher, I would kick you out of my class..." 
                        $ characters["jorrit"]["hearts"] -= 1 
                "nevermind...":
                    jump talk_js
    
return