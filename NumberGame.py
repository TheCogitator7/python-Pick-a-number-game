#import random module
import random

#count how many time you try to choose
count=0

#The game level
game_level=str(input("Select the game level : easy(E), normal(N), hard(H), very hard(HH) "))
if game_level == "E":
    level = 10
elif game_level == "N":
    level = 100
elif game_level == "H":
    level = 1000
else:
    level = 10000

#Target number
com_number=random.randint(1, level)

#function the_same()
def the_same(target, number):
    if target == number :
        result = "Win"
    elif target > number :
        result = "Low"
    else:
        result = "High"
    return result

#start the game
print("Start the number game")
print("Pick a number between 1 and", level, ". and then press the enter button : ")
#your pick(number between 1 and 100)
guess=int(input())
count+=1
print("How many times?? : ", count)

#call the_same func
higher_or_lower=the_same(com_number, guess)

#continue game until the user wins
while higher_or_lower != "Win":
    if higher_or_lower == "Low":
        guess=int(input("Your number is less than the target. Choose one more again! : "))
        count+=1
        print("How many times?? : ", count)
        
    else:
        guess=int(input("Your number is greater than the target. Choose again!! : "))
        count+=1
        print("How many times?? : ", count)

    higher_or_lower=the_same(com_number, guess)




#End the game
input("You Win!!! Press the enter button if you finish the number game.")

