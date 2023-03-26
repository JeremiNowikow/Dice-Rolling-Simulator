from random import randint


# checks if the string inputted by the player is in XDY + Z format
def validate_input(input_str: str) -> bool:
    input_str = input_str.lower()
    if input_str.count("d") != 1:
        return False
    sub_str = input_str.split("d")

    # checks if the string on the right of "d" has the proper number of "+" or "-" signs, if any
    if (sub_str[1].count("+") > 1) or (sub_str[1].count("-") > 1) or ("+" in sub_str[1] and "-" in sub_str[1]) or (sub_str[1][0] == "+") or (sub_str[1][0] == "-"):
        return False

    # splitting the right string by the "+" or "-" sign for further validation
    if "+" in sub_str[1]:
        sub_str_2 = sub_str[1].split("+")
    elif "-" in sub_str[1]:
        sub_str_2 = sub_str[1].split("-")
    else:
        sub_str_2 = [sub_str[1], 0]

    try:
        # checks if the values in the input are correct by converting them to integers
        if (sub_str[0] != "") and (int(sub_str[0]) < 1):  # checks if the value on the left of "d" is positive or 0
            return False
        int(sub_str_2[0])
        int(sub_str_2[1])
    except ValueError:
        return False

    return True


# requests the user to input the string until it is in the correct format, and then returns it
def get_user_input() -> str:
    while True:
        input_str = input("")
        if validate_input(input_str):
            return input_str
        else:
            print("Incorrect input. Requested input format: xDy, xDy+Z or xDy-Z")


# generates a specified amount of random numbers in specified range, summarizes them, and returns the sum
def generate_roll_result(input_str: str) -> int:
    split_input = input_str.lower().split("d")
    if split_input[0] == "":  # if there was no number on the left of "D", the number of dice is set to 1 by default
        dice_amount = 1
    else:
        dice_amount = int(split_input[0])
    if "+" in split_input[1]:
        split_input_2 = split_input[1].split("+")
    elif "-" in split_input[1]:
        split_input_2 = split_input[1].split("-")
    else:
        split_input_2 = [split_input[1], 0]
    dice_type = int(split_input_2[0])
    optional_modifier = int(split_input_2[1])
    rolls = [randint(1, dice_type) for i in range(dice_amount)]
    print("The rolls:")
    print(rolls)
    return sum(rolls) + optional_modifier


print("Input the dice to roll in xDy format. If you only want to roll 1 die, you can omit the first number \n"
      "Optionally, you can include the number to add/subtract from the final roll as xDy+Z or xDy-Z. \n")

user_input = get_user_input()
result = generate_roll_result(user_input)
print(f"Your result: {result}")

