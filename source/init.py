def get_digit(number):
    return number % 10 + (number // 10 % 10)

def sum_odd_digits(card_number):
    sum_odd = 0
    for i in range(len(card_number) - 1, -1, -2):
        sum_odd += int(card_number[i])
    return sum_odd

def sum_even_digits(card_number):
    sum_even = 0
    for i in range(len(card_number) - 2, -1, -2):
        sum_even += get_digit(int(card_number[i]) * 2)
    return sum_even

def validate_card(card_number):
    result = sum_even_digits(card_number) + sum_odd_digits(card_number)
    return result % 10 == 0

if __name__ == "__main__":
    print("********** Credit Card Validator **********")
    print("This program validates credit card numbers using the Luhn algorithm.\n")
    
    while True:
        card_number = input("Enter a credit card number (or type 'exit' to quit): ")

        if card_number.lower() == 'exit':
            print("Exiting the program.")
            break

        if not card_number.isdigit():
            print("Invalid input! Please enter only numbers.")
            continue

        if validate_card(card_number):
            print(f"{card_number} is valid!")
        else:
            print(f"{card_number} is not valid!")
