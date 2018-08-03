def main():
    gender = input("Male or Female (m/f)")
    if (gender == "m" or gender == "f"):
        print("")
        if gender == "m":
            malestory()
        elif gender == "f":
            femalestory()
        else:
            print("Invalid Selection")
            
def malestory():
    #code for malestory
    print("the guy walked to the candy store")
def femalestory():
    #code for femalestory
    print("The girl walked to the candy store")
    

def seccondary():
    age = input("How old are you? 18 and younger or 18 and older.")
    if (age == "18 and younger" or age == "18 and older"):
        print("")
        if age == "18 and younger":
            Youth()
        elif age == "18 and older":
            Adult()
        else:
            print("Try again")
        
def Youth():
    #code for Youth
    print("Once he got there he saw...")
def Adult():
    #code for Adult
    print("Once she got there she saw...")  
    

def third():
    hunger = input("Are you hungry? Yes or No")
    if (hunger == "No" or hunger == "Yes"):
        print("")
        if hunger == "No":
            No()
        elif hunger == "Yes":
            Yes()
        else:
            print("Nice try")
            
def No():
    #code for No
    print("Superman!")
def Yes():
    #code for Yes
    print("The Joker!")
    
    
def fourth():
    ending = input("What would you like? cheese or bacon?")
    if (ending== "cheese" or ending == "bacon"):
        print("")
        if ending == "cheese":
            cheese()
        elif ending == "bacon":
            bacon()
        else:
            print("No Way!")
            
def cheese():
    #code for cheese
    print("The guy and superman become best friends and save the world together. The End.")
def bacon():
    #code for bacon
    print("The Joker takes everyone the girl loves hostage, only letting them free when she swears to be his thrall. Once she agrees Joker kills all of her loved ones and keeps the girl as his thrall for eternity. The End.") 
    
            


main()            
seccondary()
third()
fourth()