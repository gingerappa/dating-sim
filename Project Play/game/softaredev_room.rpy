#Defining characters

define js = Character("Jorrit Slaats")
define u = Character("You")
#define g = Character("Game devs")

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


        
    
return
