# Jamie Hilton
# 23/09/14
# Fridge and Lift Calculator v1.1

fridge_height = float(input("Please enter the height of your fridge in m: "))

fridge_width = float(input("Please enter the width of your fridge in m: "))

fridge_depth = float(input("Please enter the depth of your fridge in m: "))

lift_height = float(input("Please enter the height of your lift in m: "))

lift_width = float(input("Please enter the width of your lift in m: "))

lift_depth = float(input("Please enter the depth of your lift in m: "))

fridge_volume = fridge_height*fridge_width*fridge_depth

lift_volume = lift_height*lift_width*lift_depth

total_volume = lift_volume-fridge_volume

print("you have {0} m of space left in the lift".format(total_volume))
