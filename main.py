# Integration Project
__author__ = "Victor Morales Blanco"
# This is a basic calculator to demonstrate my understanding of the Python language.
# Sources https://www.w3schools.com/python/


import math


def answer_associated_property_equations_prompt(list_of_numbers, total, sign):
    """

    :param list_of_numbers:
    :param total:
    :param sign:
    :return:
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


# This function builds the subtraction equation for visual purposes
def answer_subtraction_prompt(list_of_numbers, total):
    equation_string = ""
    i = 0
    while i < len(list_of_numbers):
        if i == len(list_of_numbers) - 1:
            equation_string += str(list_of_numbers[i]) + " = " + str(total)
        else:
            equation_string += str(list_of_numbers[i]) + " - "
        i += 1
    return equation_string


# This function builds the division equation for visual purposes
def answer_division_prompt(list_of_numbers, total, remainder, denominator,
                           type_of_answer):
    """

    :param list_of_numbers:
    :param total:
    :param remainder:
    :param denominator:
    :param type_of_answer:
    :return:
    """
    equation_string = ""
    i = 0
    while i < len(list_of_numbers):
        if i == len(list_of_numbers) - 1:
            if type_of_answer == "fraction":
                total_as_string = str(total).split(".")[0] + "  " + str(
                    int(remainder)) + "/" + str(int(denominator))
                equation_string += str(
                    list_of_numbers[i]) + " = " + total_as_string
            else:
                equation_string += str(list_of_numbers[i]) + " = " + str(total)
        else:
            equation_string += str(list_of_numbers[i]) + " / "
        i += 1
    return equation_string


# This function gets vital information for the computation
def equation_prompt(operation_as_word):
    """

    :param operation_as_word:
    :return:
    """
    number_of_items = 0
    # This loop serves as validation to make sure the user inputs a number greater than 1
    while number_of_items < 2:
        print(
            "I'm going to need at least two numbers to be able to do any calculation.")
        number_of_items = int(float(input(
            "How many numbers do you wish to " + operation_as_word + "? ")))
    iteration_counter = 0
    list_of_numbers = []
    # This loop allows the user to input the numbers and sends it into a list
    while iteration_counter < number_of_items:
        number = float(input(
            "Enter number" + " " + str(iteration_counter + 1) + " of " + str(
                number_of_items) + " : "))
        list_of_numbers.append(number)
        iteration_counter += 1
    return list_of_numbers


# This function subtracts the numbers from each other in the order they were
# put into the list
def subtraction_function():
    """

    """
    # This line sends a parameter for the purpose of user interaction and
    # returns a list of numbers.
    list_of_numbers = equation_prompt("subtract")
    # This line saves the first number in the list
    total = list_of_numbers[0]
    iteration_counter = 1
    # This loop subtracts the number stored in the list in the proper order
    while iteration_counter < len(list_of_numbers):
        total -= list_of_numbers[iteration_counter]
        iteration_counter += 1
    # This line sends the list of numbers and the total to a function in order
    # to create a string displaying
    # the equation for the user. That function returns the equation as a string
    # that is stored in answer.
    answer = answer_subtraction_prompt(list_of_numbers, total)
    print(answer)
    # This line sends the user back to the beginning, so they can do another calculation.
    operation_decision()


# This function adds all the numbers in the list
def addition_function():
    """


    :return:
    """
    # This line sends a parameter for the purpose of user interaction and returns a list of numbers.
    list_of_numbers = equation_prompt("add")
    # This line initializes the variable total.
    total = 0.0
    # This loop adds all the numbers in the list.
    for item in list_of_numbers:
        # This line is the same as saying: total = total + list_of_numbers[iteration_counter]
        total += item
    # This line sends the list of numbers and the total to a function in order to create a string displaying
    # the equation for the user. That function returns the equation as a string that is stored in answer.
    answer = answer_associated_property_equations_prompt(list_of_numbers,
                                                         total, " - ")
    print(answer)
    # This line sends the user back to the beginning, so they can do another calculation.
    operation_decision()


# This function multiplies all the numbers in the list
def multipy_function():
    """

    :return:
    """
    # This line sends a parameter for the purpose of user interaction and returns a list of numbers.
    list_of_numbers = equation_prompt("multiply")
    # This line initializes total so that it can be referenced outside the loop.
    # Set = to 1 so as not to affect the total.
    total = 1
    # This loop multiplies all the numbers in the list.
    for item in list_of_numbers:
        total = total * item
    # This line sends the list of numbers and the total to a function in order to create a string displaying
    # the equation for the user. That function returns the equation as a string that is stored in answer.
    answer = answer_associated_property_equations_prompt(list_of_numbers,
                                                         total, " * ")
    print(answer)
    # This line sends the user back to the beginning, so they can do another calculation.
    operation_decision()


def divide_function(type_of_answer):
    """
        This function calculates a division equation based on user inputs.

    :param type_of_answer: This variable is used to hold

    :list_of_numbers: This is a list of the user inputs.
    :total: This is the result of the calculation.
    :denominator: This stores the denominator calculated by multiplying all the
        numbers the user input except the first.
    :remainder: This stores the remainder using the modulus operator.
    :answer: This is a string that has the entire equation so that it can be
        displaced.
    """
    list_of_numbers = equation_prompt("divide")
    total = 1
    # This line initializes answer so that it may be referenced outside the if
    #  statement.
    for item in range(len(list_of_numbers)):
        total = total * list_of_numbers[item]
    denominator = total / list_of_numbers[0]
    total = list_of_numbers[0] / denominator
    remainder = list_of_numbers[0] % denominator
    # This line sends the list of numbers and the total to a function in order
    # to create a string displaying the equation for the user. That function
    # returns the equation as a string that is stored in answer.
    answer = answer_division_prompt(list_of_numbers, total, remainder,
                                    denominator, type_of_answer)
    print(answer)
    operation_decision()


def exponent_function():
    """
        This function calculates an exponential equation

    :base_number: This is the base number the user inputs.
    :exponent: This is the exponent the user inputs.
    :total: This stores the total after the equation has been calculated.
    """
    print("Please enter the base number:")
    base_number = float(input())
    print("Please enter the exponent:")
    exponent = float(input())
    total = math.pow(base_number, exponent)
    print(str(base_number) + "^" + str(exponent) + " = " + str(total))


def operation_decision():
    """
        This function serves determines which functions get called depending on
        user input.

    :operations_list: This is a list of acceptable inputs.
    :mathematical_operation: This is the user's initial input.
    :division_choice: This is a secondary input when the user selects
        division.
    """
    operations_list = ["add", "subtract", "multiply", "divide", "exponent"]
    print(
        "Please enter the kind of calculation you wish to do." +
        " Type add, subtract, multiply, divide, or exponent",
        end=". (No other input will be accepted)\n")
    mathematical_operation = input()
    # This if statement checks for the presence of user input in the list of
    # acceptable values
    if mathematical_operation not in operations_list:
        print("Sorry, I cannot do this operation. Please try again.")
        operation_decision()
    else:
        if mathematical_operation == "add":
            addition_function()
        elif mathematical_operation == "subtract":
            subtraction_function()
        elif mathematical_operation == "multiply":
            multipy_function()
        elif mathematical_operation == "divide":
            division_choice = ""
            while division_choice != "decimal" and division_choice != "fraction":
                print("Do you wish to have a decimal answer? Type decimal.")
                print(
                    "Do you wish to have a precise fraction answer? Type "
                    "fraction.")
                division_choice = input()
            if division_choice == "fraction":
                divide_function("fraction")
            else:
                divide_function("decimal")
        elif mathematical_operation == "exponent":
            exponent_function()


def main():
    """

    """
    print("Hello! " * 2, "Welcome to my calculator program!", sep="\n")
    print(
        "I can add, subtract, multiply, divide, and I can even do exponents!")
    # Redirects to function operation_decision()
    operation_decision()


# This line calls the startup() function
main()
