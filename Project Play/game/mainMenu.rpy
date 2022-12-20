label main:
    scene bg map
    call screen MapUI
screen MapUI:
    #add "map/bg map.png"
    imagebutton:
        xpos 681
        ypos 296
        idle "map/av.png"
        hover "map/av_hover.png"
        action Jump("house1_pressed")
    imagebutton:
        xpos 821
        ypos 579
        idle "map/fg.png"
        hover "map/fg_hover.png"
        action Jump("house1_pressed")
    imagebutton:
        xpos 1065
        ypos 973
        idle "map/ddm.png"
        hover "map/ddm_hover.png"
        action Jump("house1_pressed")
    imagebutton:
        xpos 1215
        ypos 974
        idle "map/sd.png"
        hover "map/sd_hover.png"
        action Jump("sd_room")
    

