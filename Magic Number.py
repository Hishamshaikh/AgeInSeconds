def magic_num():
    user_input = int(input("Enter a magic number between 0 and 10: "))
    magic = 5
    if user_input == magic:
        print("You've won")
    elif user_input != magic:
        print("Wrong number, please try again")

magic_num()