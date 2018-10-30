# print a messsage to the terimal window
print("Rules that govern the state of water")

# set up a variable to hold the tempature we imput 
current_temp = False 

while current_temp is False:
    current_temp = input("Enter a tempature:\n")
    # see what current temp is
    print(current_temp)

    # if the current temp is at freezing or below, water is a solid
    if (int(current_temp) < 0 or (int(current_temp)==0)):
    	print("water is a solid! cuz it's at or below freezing")
    	current_temp = False
    # else check another condition. if its not freezing, is below boiling?
    elif (int(current_temp) < 100):
    	print("water is a liquid, because it's above freezing and below boiling")
    	current_temp = False

    elif (int(current_temp) > 100 or (int(current_temp) == 100)):
    	print("water is a gas. Cuz it's, like, really hot")
    	current_temp = False