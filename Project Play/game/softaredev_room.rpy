#Defining characters

define js = Character("Jorrit Slaats")
define u = Character("You")
#define g = Character("Game devs")

$js.hearts = 0

# The game starts here.

#label start:

label jorrit:

    scene Placeholder
    show js neutral at right
    with dissolve

    js "Hey, welcome!"
    js "I assume you're the future student Pauline told me about"
    js "Let me introduce myself…"
    js "I'm Jorrit, nice to meet you."
    u "Hi Jorrit! Nice to meet you too!"

    menu questionswork_js: 
    "What would you like to ask Jorrit?"

        "What do you teach the students?":
        js "I teach Software development and the elective subject Gameplay."

        "Favorite part of your job?":
        js "I've always enjoyed programming..."
        js "however, I tend to get tired of it when I do it for long periods at a time."
        js "The best part about working as a software development teacher is that I can combine my love for development with a ton of different working activities and tons of social interactions"

        "Is it actually that hard to keep up with grading?"
        show jorrit happy 
        js "Depends on what you are grading and how you are grading!"
        js "Just writing V, G, O, V, V, in Magister is a lot less effort than giving useful feedback."
        js "Also, downloading big Unity projects or Blender files and waiting for the slow programs to open and close can eat up a bunch of time. Work smart!"

pass

js "So, any other questions?"

    menu talk_js:

        "What are your hobbies?":
            js "I play Dungeons&Dragons once or twice a week! {i}As long as scheduling doesn't ruin everything...{/i}"
            js "Recently I've also discovered a new hobby in using AI's to generate art."
            show jorrit blush
            js "Of course I also like to play games which was one of the reasons that got me into development in the first place."
            $askedhobbiesjs = true
            js "I listen to a bunch of music, but like, who doesn't?"
            js "Lastly, I like making cocktails. However I don't do it that often since I only do so at parties."

        "Do you play games?":
            js "As I said before..." if askedhobbiesjs
            js "Quite frequently still!" 

        "Any special interests?":
            js "AI image generation, Dungeons and dragons..." 
            js "Oh, and cats are pretty awesome!" 
        
        "Favorite food?"
            js "I love a proper hamburger! Not some McDonald's hamburger, but a good one." 
pass

    menu flirt_js if adult:
    "Should I try to flirt with him..?"

        "Are you single?":
            #TODO: add variables to determine if Jorrit likes the player or not
            js "As a pringle!" 
            $js.hearts = js.hearts + 1

            js "Maybe you should ask again when I'm in a better mood." 
            $js.hearts = js.hearts - 1

            
        "Any plans for after your'e done working??":
        
            show jorrit angry
            js "I'll probably visit some friends during the weekend!" 
            $js.hearts = js.hearts + 1

            show jorrit angry
            js "You mean for when I retire!? Do you really think I look that old???" 
            $js.hearts = js.hearts - 1

        "If you were my teacher I would be a teachers pet!":
            show jorrit blush
            js "If you are thinking of bringing me an apple, make sure to bring a green one!" 
            $js.hearts = js.hearts + 1

            show jorrit angry
            js "If I was your teacher, I would kick you out of my class..." 
            $js.hearts = js.hearts - 1 
    
return