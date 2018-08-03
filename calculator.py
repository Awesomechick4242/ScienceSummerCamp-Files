def main():
    number1 = input("Enter a number  ")
    number2 = input("Enter another number  ")
    if number2 == 'x':
        number2 = number1
    func = input("What operation  ")
    if func == "1":
        print("the awnser is "+ str(int(number1)+int(number2)))
    elif func == "2":
        print("the awnser is "+ str(int(number1)-int(number2)))
    elif func == "3":
        print("the awnser is "+ str(int(number1)*int(number2)))
    elif func == "4":
        print("the awnser is "+ str(int(number1)/int(number2)))
    else:
        print("'1' for addition '2' for subtraction '3' for multiplication '4' for division")
    main()    
    return 0

if __name__ == "__main__":
    main()