"""
    Integration Project

    This is a basic calculator to demonstrate my understanding of the Python
    language.

    Sources https://www.w3schools.com/python/
"""

__author__ = "Victor Morales Blanco"

import math


def main_equation_string_builder(list_of_numbers, total, sign):
    """
        This function builds the addition, subtraction, and multiplication
        equations strings for visual purposes.

    :param list_of_numbers: This contains all the numbers the user inputted.
    :param total: This holds the calculated total as a decimal.
    :param sign: This holds either the "+" or "*" operators for string
        concatenation.
    :return equation_string:  This holds the equation string to display to the
            user.
    """
    equation_string = ""
    i = 0
    while i < len(list_of_numbers):
        if i == len(list_of_numbers) - 1:
            equation_string += str(list_of_numbers[i]) + " = " + str(total)
        else:
            equation_string += str(list_of_numbers[i]) + sign
        i += 1
    return equation_string


def division_equation_string_builder(list_of_numbers, total, remainder,
                                     denominator,
                                     type_of_answer):
    """
        This function builds the division equation string for visual purposes.

    :param list_of_numbers: This contains all the numbers the user inputted.
    :param total: This holds the calculated total as a decimal.
    :param remainder: This holds the remainder of the division.
    :param denominator: This holds the value of the second item in the list of
        numbers to the last value multiplied.
    :param type_of_answer: This holds the decision the user made: whether they
        want a fraction or decimal answer.
    :return equation_string:  This holds the equation string to display to the
            user.
    """
    equation_string = ""
    i = 0
    while i < len(list_of_numbers):
        if i == len(list_of_numbers) - 1:
            if type_of_answer == "fraction":
                mixed_fraction = str(total).split(".")[0] + "  " + str(
                    int(remainder)) + "/" + str(int(denominator))
                equation_string += str(
                    list_of_numbers[i]) + " = " + mixed_fraction
            else:
                equation_string += str(list_of_numbers[i]) + " = " + str(total)
        else:
            equation_string += str(list_of_numbers[i]) + " / "
        i += 1
    return equation_string


def equation_prompt(operation_as_word):
    """
        This function prompts the user for critical information to perform the
        calculations.

    :param operation_as_word: Holds the operation the user inputted previously
        as a string for prompt.
    :return list_of_numbers: This is the list of numbers that is sent back to
        one of the equation functions for calculation.

    :iteration_counter: Controls the loop.
    """
    number_of_items = 0
    while number_of_items < 2:
        try:
            print(
                "I'm going to need at least two numbers to be able to do any "
                "calculation.")
            number_of_items = int(float(input(
                "How many numbers do you wish to " + operation_as_word + "? "
            ).replace(' ', '')))
        except ValueError:
            print("Invalid input. Please type a number")
    iteration_counter = 0
    list_of_numbers = []
    while iteration_counter < number_of_items:
        try:
            number = float(input(
                "Enter number" + " " + str(
                    iteration_counter + 1) + " of " + str(
                    number_of_items) + " : ").replace(' ', ''))
            list_of_numbers.append(number)
            iteration_counter += 1
        except ValueError:
            print("Numbers and decimals only, please.")

    return list_of_numbers


def subtraction_function():
    """
         This function calculates a subtraction equation based on user inputs.

     :list_of_numbers: This list holds the numbers the user input for
         multiplication.
     :total: This is the result of the calculation.
     :iteration_counter: Controls the loop.
     :answer: This holds the equation string to display to the user.
     """
    list_of_numbers = equation_prompt("subtract")
    total = list_of_numbers[0]
    iteration_counter = 1
    while iteration_counter < len(list_of_numbers):
        total -= list_of_numbers[iteration_counter]
        iteration_counter += 1
    answer = main_equation_string_builder(list_of_numbers, total, " - ")
    print(answer)
    operation_decision()


def addition_function():
    """
        This function calculates an addition equation based on user inputs.

    :list_of_numbers: This list holds the numbers the user input for
        multiplication.
    :total: This is the result of the calculation.
    :answer:  This holds the equation string to display to the user.
    """
    list_of_numbers = equation_prompt("add")
    total = 0.0
    for item in list_of_numbers:
        total += item
    answer = main_equation_string_builder(list_of_numbers, total, " - ")
    print(answer)
    operation_decision()


def multipy_function():
    """
        This function calculates a division equation based on user inputs.

    :list_of_numbers: This list holds the numbers the user input for
        multiplication.
    :total: This is the result of the calculation.
    :answer:  This holds the equation string to display to the user.
    """

    list_of_numbers = equation_prompt("multiply")
    total = 1
    for item in list_of_numbers:
        total *= item
    answer = main_equation_string_builder(list_of_numbers, total, " * ")
    print(answer)
    operation_decision()


def divide_function(type_of_answer):
    """
        This function calculates a division equation based on user inputs.

    :param type_of_answer: This variable is used to hold the secondary user
        choice.

    :list_of_numbers: This is a list of the user inputs.
    :total: This is the result of the calculation.
    :denominator: This stores the denominator calculated by multiplying all the
        numbers the user input except the first.
    :remainder: This stores the remainder using the modulus operator.
    :answer:  This holds the equation string to display to the user.

    """
    list_of_numbers = equation_prompt("divide")
    total = 1
    for item in range(len(list_of_numbers)):
        total *= list_of_numbers[item]
    denominator = total / list_of_numbers[0]
    total = list_of_numbers[0] / denominator
    remainder = list_of_numbers[0] % denominator
    answer = division_equation_string_builder(list_of_numbers, total,
                                              remainder, denominator,
                                              type_of_answer)
    print(answer)
    operation_decision()


def exponent_function():
    """
        This function calculates an exponential equation based on user input.

    :base_number: This is the base number the user inputs.
    :exponent: This is the exponent the user inputs.
    :total: This stores the total after the equation has been calculated.
    """
    continue_loop = True
    continue_loop_2 = True
    base_number = 0
    exponent = 0
    while continue_loop:
        try:
            print("Please enter the base number:")
            base_number = float(input().replace(' ', ''))
            continue_loop = False
        except ValueError:
            print("Please enter a number.")
    while continue_loop_2:
        try:
            print("Please enter the exponent:")
            exponent = float(input().replace(' ', ''))
            continue_loop_2 = False
        except ValueError:
            print("Please enter a number.")
    total = math.pow(base_number, exponent)
    print(str(base_number) + "^" + str(exponent) + " = " + str(total))
    operation_decision()


def operation_decision():
    """
        This function serves determines which functions get called depending on
        user input.

    :operations_list: This is a list of acceptable inputs.
    :mathematical_operation: This is the user's initial input.
    :division_choice: This is a secondary input when the user selects
        division.
    """
    operations_list = ["1", "2", "3", "4", "5"]
    print(
        "Please enter the kind of calculation you wish to do." +
        "\n1. Addition \n2. Subtraction \n3. Multiplication \n4. Division " +
        "\n5. Exponential \n",
        end="(No other input will be accepted)\n")
    mathematical_operation = input().replace(' ', '')
    if mathematical_operation not in operations_list:
        print("Sorry, I cannot do this operation. Please try again.")
        operation_decision()
    else:
        if mathematical_operation == "1":
            addition_function()
        elif mathematical_operation == "2":
            subtraction_function()
        elif mathematical_operation == "3":
            multipy_function()
        elif mathematical_operation == "4":
            division_choice = ""
            while division_choice != "1" and division_choice != "2":
                continue_loop = True
                while continue_loop:
                    print("Do you wish to have a decimal answer? Type 1.")
                    print(
                        "Do you wish to have a precise fraction answer? Type "
                        "2.")
                    division_choice = input().replace(' ', '')
                    if division_choice == "2":
                        divide_function("fraction")
                        continue_loop = False
                    elif division_choice == "1":
                        divide_function("decimal")
                        continue_loop = False
        elif mathematical_operation == "5":
            exponent_function()


def main():
    """
        This is the main function that controls the program.
    """
    print("Hello! " * 2, "Welcome to my calculator program!", sep="\n")
    print(
        "I can add, subtract, multiply, divide, and I can even do exponents!")
    operation_decision()


if __name__ == "__main__":
    main()
