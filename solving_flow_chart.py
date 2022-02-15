

#solving flow chart for "Lamp" or "bulb" faulted Game either bulb or lamp 
# should be replaced or repaired  
lamp_condition=input("Is lamp pluged in or not ?")
bulb_condition=input("Enter the bulb state. is it burning or not ?")

while lamp_condition:
    if lamp_condition==True:
        if bulb_condition==True:
            print("Repair Lamp")
        else:
            print("Repair Bulb")
    else:
        print("plug in Lamp")
    break    