# practice 6
# create a list of all the even number in a range given by the user

def program():

    while True:
        print("")
        num1 = input("1/ please provide a number here: ")
        num2 = input("2/ please provide a number here: ")
        even = []

        if num1.isdigit() and num2.isdigit():
            number1, number2 = int(num1), int(num2)
            if number1 < number2:
                for i in range(number1, number2 + 1):
                    if i % 2 == 0:
                        even.append(i)
                break
            else:
                print("")
                print("** the first number is greater or equal to the second number.\n"
                      "please try again.")
        else:
            print("")
            print("** the values provided are not full digits.\n"
                  "please try again.")
    print("")
    return f"these are the even numbers in the range you provided: {even}"

print("hello dear user! we are very excited to have you here.\n"
      "for our program to operate, we only need two numbers.\n"
      "please input any numbers you desire and we will take care of the rest :)")

value = program()
print(value)