label main:
    play music "music/main.mp3" fadein 1.0 volume 0.1
    call screen MapUI
screen MapUI:
    add "map.png"
    imagebutton:
        xpos 0
        ypos 0
        idle "house1_idle.png"
        hover "house1_hover.png"
        action Jump("house1_pressed")

