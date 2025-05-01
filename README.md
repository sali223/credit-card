# py.credit-card-validato
A simple Python program that validates credit card numbers using the Luhn algorithm. Includes user input handling, digit processing, and checksum verification to determine card number validity.
Overview:
This Python program validates credit card numbers based on the Luhn algorithm, a simple checksum formula used to validate various types of identification numbers, including credit card numbers. The program checks whether a card number is valid by performing a series of arithmetic operations on the individual digits.

Features:
Prompts the user to input a credit card number.

Validates the card number using the Luhn algorithm.

Provides an output stating whether the entered card number is valid or invalid.

Allows the user to check multiple card numbers until they decide to exit the program.

Requirements:
Python 3.x

No additional libraries or dependencies are required.

How to Use:
Run the program in your terminal or IDE.

The program will prompt you to enter a credit card number.

Enter a card number (only digits).

The program will check if the number is valid according to the Luhn algorithm.

If the number is valid, it will print: <card_number> is valid!

If the number is invalid, it will print: <card_number> is not valid!

You can enter another card number or type exit to quit the program.

Luhn Algorithm (How it Works):
The Luhn algorithm is a simple checksum formula used to validate a variety of identification numbers. Here's how it works:

Reverse the digits of the card number.

Starting from the rightmost digit, double every second digit.

If doubling any digit results in a number greater than 9, sum the digits of that result.

Add up all the digits (both doubled and undoubled).

If the total sum is divisible by 10, the card number is valid.

Example:
For the card number 4539 1488 0343 6467:

After processing with the Luhn algorithm, the sum is divisible by 10, so the card is valid.

For the card number 1234 5678 9876 5432:

The sum is not divisible by 10, so the card is invalid.

Code Breakdown:
get_digit(number):

A helper function to calculate the sum of digits for a given number. It is used to sum the digits when a number is doubled and the result is greater than 9.

sum_odd_digits(card_number):

Calculates the sum of digits at odd positions (0-indexed) from right to left.

sum_even_digits(card_number):

Calculates the sum of digits at even positions from right to left, but first multiplies each of them by 2 and applies the get_digit function if necessary.

validate_card(card_number):

Uses the sum of odd and even digits to perform the Luhn checksum and determines if the card number is valid.
