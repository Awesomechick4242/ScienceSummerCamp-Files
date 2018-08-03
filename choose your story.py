def main ():
    gender = input("female or male? (f/m)")
    if (gender == "m" or gender == "f"):
        print("")
        if gender == "m":
            male()
        elif gender == "f":
            female()
        else:
            print("Invalid Selection")
            
def male():
    #code for male
    print("You are a male.")
def female():
    #code for female
    print("You are female.")
    

def seccond ():
    name = input("For your name choose either Tannis or Zaneeura. (t/z)")
    if (name == "t" or name == "z"):
        print("")
        if name == "t":
            tannis()
        elif name == "z":
            zaneeura()
        else:
            print("Invalid Selecton")
            
def tannis():
    #code for tannis
    print("Hello, Tannis.")
def zaneeura():
    #code for zaneeura
    print("Hello, Zaneeura.")
    


main()
seccond()
