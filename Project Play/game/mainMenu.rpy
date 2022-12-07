label main:
    play music "music/main.mp3" fadein 1.0 volume 0.1
    call screen MapUI
screen MapUI:
    add "map/map.png"
    imagebutton:
        xpos 681
        ypos 296
        idle "map/av.png"
        hover "map/av_hover.png"
        action Jump("house1_pressed")
    imagebutton:
        xpos 1065
        ypos 923
        idle "map/ddm.png"
        hover "map/ddm_hover.png"
        action Jump("house1_pressed")
    imagebutton:
        xpos 1315
        ypos 974
        idle "map/sd.png"
        hover "map/sd_hover.png"
        action Jump("house1_pressed")
    imagebutton:
        xpos 821
        ypos 579
        idle "map/fg.png"
        hover "map/fg_hover.png"
        action Jump("house1_pressed")

