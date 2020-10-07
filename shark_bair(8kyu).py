def shark(pontoonDistance, sharkDistance, youSpeed, sharkSpeed, dolphin):
    # Don't get eaten!
    if dolphin :
        pontoonDistance = pontoonDistance / 2
    
    youT = pontoonDistance/youSpeed 
    sharkT = pontoonDistance/ sharkSpeed
    
    if youT < sharkT and youT != sharkT:
        return "Alive!"
    else:
        return "Shark Bait!"
