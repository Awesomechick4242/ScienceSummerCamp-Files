import random


rolldice = "yes"

while rolldice == "yes" or rolldice == "y":
    print("Rolling the dice...")
    print("The number is ...")
    print(random.randint(1,6))
    

    rolldice = input("Want to play again?")

    
    

