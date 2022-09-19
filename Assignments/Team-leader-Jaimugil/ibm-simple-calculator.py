def add():
    a = int(input("Enter num 1 :"))
    b = int(input("Enter num 2 :"))
    return a + b

def sub():
    a = int(input("Enter num 1 :"))
    b = int(input("Enter num 2 :"))
    return a - b

def mul():
    a = int(input("Enter num 1 :"))
    b = int(input("Enter num 2 :"))
    return a * b

def div():
    a = int(input("Enter num 1 :"))
    b = int(input("Enter num 2 :"))
    if(b == 0):
        return ("Divisor cannot be zero")
    return a / b


if __name__ == "__main__":
    while(True):
        print("Enter your Choice:")
        print("1) Addition\n2) Subtraction\n3)Multiplication\n4) Division")
        choice = int(input())
        if(choice == 1):
            print(add())
        elif(choice == 2):
            print(sub())
        elif(choice == 3):
            print(mul())
        elif(choice == 4):
            print(div())
        else:
            print("Enter a valid choice")
