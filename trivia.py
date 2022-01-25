
number_correct = 0

print("What color is Link's tunic in breath of the wild?")
print("1) Red")
print("2) Blue")
print("3) Pink")
print("4) Black")
color = input("> ")

if color == "2":
    print ("Correct")
    number_correct = number_correct + 1
else:
    print ("You are wrong")

print("who do you get the parglider from?")
print("1) monster")
print("2)vilger")
print("3)old man")
print("4)impa")
answer2 = input("> ")

if answer2 == "3":
    print ("correct")
    number_correct = number_correct + 1
else:
    print ("you are wrong")

print("You got", number_correct, "correct")
    
    