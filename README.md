Credit Card Validator
Overview
This Python program validates credit card numbers using the Luhn algorithm, a checksum formula designed to check the validity of various identification numbers, including credit cards. It performs arithmetic operations on the digits of the card number to determine if it’s valid.

Features
Prompts the user to input a credit card number.

Validates the number using the Luhn algorithm.

Prints whether the card number is valid or invalid.

Allows multiple validations until the user decides to exit.

Requirements
Python 3.x

No additional libraries required.

How to Use
Run the program in your terminal or IDE.

Enter a credit card number (digits only).

The program will validate the card and display if it's valid or not.

You can enter another card number or type exit to quit.

Luhn Algorithm
Reverse the digits of the card number.

Starting from the right, double every second digit.

If doubling a digit results in a number > 9, sum those digits.

Sum all digits (doubled and undoubled).

If the total is divisible by 10, the card is valid.

Example:
Valid: 4539 1488 0343 6467

Invalid: 1234 5678 9876 5432

Code Breakdown
get_digit(number): Sums the digits of a number (used when doubling results in >9).

sum_odd_digits(card_number): Sums digits in odd positions (from right to left).

sum_even_digits(card_number): Sums digits in even positions, doubling them first.

validate_card(card_number): Calculates the Luhn checksum to determine validity.
