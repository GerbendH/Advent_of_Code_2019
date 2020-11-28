def split_number(number):
    number_split = []
    split_string = str(number)

    for letter in split_string:
        number_split.append(int(letter))

    return number_split


def six_digit_check(number):
    if len(number) == 6:
        return True
    else:
        return False


def double_digit_check(number):
    retval = False

    for digit in range(1, 6):
        if number[digit - 1] == number[digit]:
            retval = True

    return retval

def increase_check(number):
    retval = True

    for digit in range(1, 6):
        if number[digit] < number[digit - 1]:
            retval = False

    return retval

def password_check(number):
    password_flag = False
    six_digit_flag = False
    double_digit_flag = False
    increase_flag = False

    six_digit_flag = six_digit_check(number)
    double_digit_flag = double_digit_check(number)
    increase_flag = increase_check(number)

    if six_digit_flag and double_digit_flag and increase_flag:
        password_flag = True

    return password_flag

def calculate_passwords(min,max):
    # loop trough min to max
    passwords = []

    for number in range(min,max):
        number_split = split_number(number)

        if password_check(number_split):
            passwords.append(number)

    return passwords


def main():
    min_range = 171309
    max_range = 643603

    passwords = calculate_passwords(min_range, max_range)

    print(len(passwords))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
