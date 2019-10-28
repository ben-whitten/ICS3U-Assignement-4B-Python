#!/usr/bin/env python3

# Created by: Ben Whitten
# Created on: October 2019
# This is a program which tells you which of three numbers are the greatest.


# This allows me to do things with the text.
class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def main():
    # This is what tells you the greatest number.
    print("")
    print("WELCOME TO GREATEST NUMBER!")
    print("")

    while True:
        # Input
        number_1_as_string = input(color.BOLD + color.YELLOW +
                                   'Input your first number: ' + color.END)
        number_2_as_string = input(color.BOLD + color.YELLOW +
                                   'Input your second number: ' + color.END)
        number_3_as_string = input(color.BOLD + color.YELLOW +
                                   'Input your third number: ' + color.END)

        # Process
        try:
            number_1 = int(number_1_as_string)
            number_2 = int(number_2_as_string)
            number_3 = int(number_3_as_string)

            if number_1 > number_2 and number_1 > number_3:
                # Output
                print('')
                print(color.BOLD + color.GREEN + 'Number 1 is the greatest.' +
                      ' ({0})'.format(number_1) + color.END)
                break
            # Process
            elif number_2 > number_1 and number_2 > number_3:
                # Output
                print('')
                print(color.BOLD + color.GREEN + 'Number 2 is the greatest.' +
                      ' ({0})'.format(number_2) + color.END)
                break
            # Process
            elif number_3 > number_1 and number_3 > number_2:
                # Output
                print('')
                print(color.BOLD + color.GREEN + 'Number 3 is the greatest.' +
                      ' ({0})'.format(number_3) + color.END)
                break
            # Process
            elif number_1 == number_2 and number_1 > number_3:
                # Output
                print('')
                print(color.BOLD + color.GREEN + 'Number 1 and number 2 are' +
                      ' the greatest. ({0})'.format(number_1) + color.END)
                break
            # Process
            elif number_1 == number_3 and number_1 > number_2:
                # Output
                print('')
                print(color.BOLD + color.GREEN + 'Number 1 and number 3 are' +
                      ' the greatest. ({0})'.format(number_1) + color.END)
                break
            # Process
            elif number_2 == number_3 and number_2 > number_1:
                # Output
                print('')
                print(color.BOLD + color.GREEN + 'Number 2 and number 3 are' +
                      ' the greatest. ({0})'.format(number_2) + color.END)
                break
            # Process
            elif number_1 == number_2 and number_1 == number_3:
                # Output
                print('')
                print(color.BOLD + color.GREEN + 'All numbers are equal' +
                      ' ({0})'.format(number_1) + color.END)
                break
            else:
                print("ERROR")

        # This stops them from putting in something let bob and gets them to
        # re-input their age.
        except Exception:
            print('')
            print(color.RED + 'One or more of those were not numbers'
                  + color.END)
            print("")
            print("")


if __name__ == "__main__":
    main()
