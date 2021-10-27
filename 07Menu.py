import sys

def print_menu():
    print("""
 ------------------------------------------------
|                                                |
|    07Menu                                      |
|    Name : Menaal Hassan                        |
|    Version : 01                                |
|                                                |
 ------------------------------------------------

1. Hello World
2. Goodbye World
3. Goodbye Person
4. Good Teacher
5. forLoop
6. whileLoop
7. string Loop
8. Convert to ascii
9. Encode a string
x. To Exit
    """)

while True:
    print_menu()
    menu_option = input("Enter an option ")
    #options = ['1','2','3','4','5','6','7','8','9','x']
    options = ['1','2','3','4','5','6','x']
    
    print("----Start of Output ---------------------------\n")

    if menu_option in options:
        if menu_option.lower() == 'x': 
            sys.exit()
        elif menu_option == '1':
            print("Hello World")
        elif menu_option == '2':
            print("Hello World")
            input("------> Program paused - press enter to continue")
            print("Goodbye World")
        elif menu_option == '3':
            print("Hello World\n")
            name = input("What is your name ? ")
            print("Goodbye " + name)
        elif menu_option == '4':
            teacher_name = input("Teacher's name (try Mr Horan) ")
            print(teacher_name + " is an ok teacher")
        elif menu_option == '5':
            for i in range(500):
                print(i)
        elif menu_option == '6':
            subject = "IST"
            my_input = ""
            while my_input != subject:
                my_input = input("What is the name of this subject ")
                if my_input == subject:
                    print("\nCongratulations!!")
                else:
                    print("Not Correct - try again")
    else:
        print("invalid option")

    print("\n----End of Output -----------------------------\n\n")

    input("Press Enter to continue ")
