# 1. Generator for exponentiation
import string
import random
from curses.ascii import isalpha
from operator import contains

import requests


def multiplier_factor(number):
    def multiplier_n(base):
        return base ** number

    return multiplier_n


multi_2 = multiplier_factor(2)
assert multi_2(2)


# 2. Reversing a string
def text_invert(text):
    return text[::-1]


assert text_invert("hello") == "olleh"


# 3. Adding the letter 'A' after each character in a string
def each_step_a(text):
    new_str = ''
    for i in range(len(text)):
        new_str += text[i] + 'A'
    return new_str


assert each_step_a("hello") == "hAeAlAlAoA"


# 4. Generator for numbers from 1 to 10
def one_to_ten_gen():
    for i in range(1, 11):
        yield i


gen = one_to_ten_gen()
first_number = next(gen)
second_number = next(gen)
third_number = next(gen)
assert first_number < second_number < third_number
assert first_number == 1
assert third_number == 3


# 5. Dividing even numbers
def division_of_even_numbers(dividend, divisor):
    if divisor % 2 == 0:
        return dividend / divisor
    else:
        return 'The divisor is an odd number'


assert division_of_even_numbers(2, 3) == 'The divisor is an odd number'
assert division_of_even_numbers(744, 744) == 1


# 6. Dividing odd numbers
def division_of_odd_numbers(dividend, divisor):
    if divisor % 2 != 0:
        return dividend / divisor
    else:
        return 'The divisor is an even number'


assert division_of_odd_numbers(2, 2) == 'The divisor is an even number'
assert division_of_odd_numbers(743, 743) == 1


# 7. Switching letter cases
def letter_case_switch(text):
    return ''.join(letter.upper() if letter.islower()
                   else letter.lower() if letter.isupper() else letter for letter in text)


assert letter_case_switch("PoKEMoN") == "pOkemOn"
assert letter_case_switch("jezus666CHRYSTUS") == "JEZUS666chrystus"


# 8. Odd or even number checker
def odd_even_checker(number):
    if number % 2 == 0:
        return 'even number'
    else:
        return 'odd number'


assert odd_even_checker(2) == 'even number'
assert odd_even_checker(743) == 'odd number'


# 9. Check if a string contains letters
def it_has_letters(string):
    if any(sign.isalpha() for sign in string):
        return 'it contains letters'
    else:
        return 'it does not contain letters'


assert it_has_letters('pokemon') == 'it contains letters'
assert it_has_letters('666') == 'it does not contain letters'


# 10. Check if a string contains numbers
def it_has_number(string):
    if any(sign.isdigit() for sign in string):
        return 'it contains numbers'
    else:
        return 'it does not contain numbers'


assert it_has_number('666') == 'it contains numbers'
assert it_has_number('pokemon') == 'it does not contain numbers'


# 11. Check if a string contains special characters
def it_has_special(string):
    if any(not sign.isalpha() and not sign.isdigit() for sign in string):
        return 'it has special characters'
    else:
        return 'it does not have special characters'


assert it_has_special('pokemon') == 'it does not have special characters'
assert it_has_special('6pok!!!!emon6') == 'it has special characters'


# 12. Replace digit '2' with '4' in a number
def change_two_for_four(number):
    return int(''.join(i if i != '2' else '4' for i in str(number)))


assert change_two_for_four(666) == 666
assert change_two_for_four(6226446) == 6446446


# 13. Replace whitespace with '-'
def whitespace_changer(text):
    return ''.join('-' if i == ' ' else i for i in text)


assert whitespace_changer("hello world") == "hello-world"
assert whitespace_changer("hello-world") == "hello-world"


# 14. Cut a string in half and swap halves
def cut_and_flip(text):
    first_half = text[:len(text) // 2]
    second_half = text[len(text) // 2:].lstrip()
    return second_half + ' ' + first_half


assert cut_and_flip("hello world") == "world hello"
assert cut_and_flip("h e l l 6 6 6") == "l 6 6 6 h e l "


# 15. Check if the sum of numbers is smaller than a given number
def is_smaller_than_number(to_check):
    def if_sum_is_smaller(*numbers):
        return sum(numbers) < to_check

    return if_sum_is_smaller


smaller_than_100 = is_smaller_than_number(100)
assert smaller_than_100(100, 233, 443) == False
assert smaller_than_100(1, 2, 4) == True


# 16. Generator for three random letters
def letter_three_shot():
    letters = string.ascii_lowercase
    for _ in range(3):
        yield random.choice(letters)


loaded_gun = letter_three_shot()
shoots = [letter for letter in loaded_gun]
assert len(shoots) == 3
assert all(letter.isalpha() for letter in shoots)


# 17. Remove consecutive duplicate letters
def drop_same_letter(text):
    new_str = ''
    for i in range(len(text) - 1):
        if text[i] != text[i + 1]:
            new_str += text[i]
    new_str += text[-1]
    return new_str


assert drop_same_letter('hello world') == 'helo world'
assert drop_same_letter('helo world') == 'helo world'


# 18. Duplicate a letter if the next letter is different
def mumble_creator(text):
    new_str = ''
    for i in range(len(text) - 1):
        if text[i] == text[i + 1]:
            pass
        else:
            new_str += text[i] + text[i]
    new_str += text[-1] + text[-1]
    return new_str


assert mumble_creator('hello') == 'hheelloo'
assert mumble_creator('hellooo') == 'hheelloo'


# 19. Duplicate each digit of a number a specified number of times
def copy_number_chosen_amount(number, amount_of_copy):
    return int(''.join(item * amount_of_copy for item in str(number)))


assert copy_number_chosen_amount(42, 2) == 4422
assert copy_number_chosen_amount(666, 4) == 666666666666


# 20. Create a dictionary of copies with incremental keys
def dict_of_copies_creator(key, value, number_of_copies):
    dict_of_pseudo_copies = {}
    for i in range(1, number_of_copies + 1):
        dict_of_pseudo_copies.update({f'{key}{i}': f"{value}{i}"})
    return dict_of_pseudo_copies


assert len(dict_of_copies_creator('key', 'value', 3)) == 3
assert len(dict_of_copies_creator('key', 'value', 66)) == 66


# 21. Fetch currency rate in PLN
def currency_rate_in_pln(currency):
    url = f'https://api.nbp.pl/api/exchangerates/rates/a/{currency}/'
    try:
        response = requests.get(url)
        return response.json()
    except ValueError:
        return None


assert isinstance(currency_rate_in_pln('USD'), dict)
assert currency_rate_in_pln('blablabla') is None


# 22. Multiply a string by a given number
def multiply_string(text, number):
    return text * number


assert multiply_string('hello world', 2) == 'hello worldhello world'


# 23. Import Zen of Python and reverse it
def import_siht():
    import contextlib
    import io
    import importlib
    with contextlib.redirect_stdout(io.StringIO()):
        this = importlib.import_module('this')
    return this.s[::-1]


assert isinstance(import_siht(), str)


# 24. Pressure unit conversion
def pressure_conversion(*, bar=None, psi=None):
    if bar is None:
        return round(psi * 0.0689476, 2)
    if psi is None:
        return round(bar * 14.5038, 2)
    else:
        return 'dont play with me'


assert pressure_conversion(bar=2.5) == 36.26
assert pressure_conversion(psi=36) == 2.48
assert pressure_conversion(psi=3.2, bar=34.2) == 'dont play with me'


# 25. email closing statement
def closing_statement(name, type_of_mail='official'):
    if type_of_mail == 'official':
        return f"""
        Thank you for your time and consideration.  
        I look forward to your reply.  

        Yours sincerely,  
        {name.title()}
        """
    if type_of_mail == 'unofficial':
        return f"""Let me know if you need any more details.  
        Looking forward to catching up!  

        Cheers,  
        {name.title()}
        """


assert contains(closing_statement('jesus chris'), 'I look forward to your reply.')
assert contains(closing_statement('jesus chris', 'unofficial'), 'Cheers')


# 26. random name creator
def random_name(sex='boy'):
    male_names = ["James", "John", "Robert", "Michael", "William", "David", "Joseph", "Charles", "Thomas",
                  "Christopher"]
    female_names = ["Mary", "Patricia", "Jennifer", "Linda", "Elizabeth", "Susan", "Jessica", "Sarah", "Karen", "Nancy"]
    if sex == 'boy':
        return random.choice(male_names)
    elif sex == 'girl':
        return random.choice(female_names)


assert isinstance(random_name(), str)


# 27. Calculate a percentage of a number
def calculate_percentage_of_number(base, percentage):
    return round(base * percentage / 100, 2)


assert calculate_percentage_of_number(200, 2) == 4


# 28. Calculate what percentage a part is of the whole
def calculate_percentage_part(part, whole):
    return round(part * 100 / whole, 2)


assert calculate_percentage_part(50, 200) == 25
assert calculate_percentage_part(75, 100) == 75


# 29 mean of list
def median_from_list_deco(func):
    def wrapper(list_of_numbers):
        list_of_numbers = sorted(list_of_numbers)
        if len(list_of_numbers) % 2 != 0:
            return list_of_numbers[len(list_of_numbers) // 2]
        else:
            center_1 = list_of_numbers[len(list_of_numbers) // 2 - 1]
            center_2 = list_of_numbers[len(list_of_numbers) // 2]
            return (center_1 + center_2) / 2

    return wrapper


@median_from_list_deco
def median_from_list(list_of_numbers):
    pass


assert median_from_list([1, 2, 3, 4, 5]) == 3
assert median_from_list([657, 32, 49, 124, 99, 12]) == 74


# 30 mean of list
def mean_from_list(list_of_numbers):
    return round(sum(list_of_numbers) / len(list_of_numbers), 2)


assert mean_from_list([1, 2, 3, 4, 5]) == 3
assert mean_from_list([657, 32, 49, 124, 99, 12]) == 162.17


# 31. 1 quantile
def first_quantile(list_of_numbers):
    sorted_numbers = sorted(list_of_numbers)
    position = (len(sorted_numbers) + 1) / 4
    lower_index = int(position) - 1
    if position % 1 > 0:
        return sorted_numbers[lower_index] + (position % 1) * (
                sorted_numbers[lower_index + 1] - sorted_numbers[lower_index])
    else:
        return sorted_numbers[lower_index]


assert first_quantile([1, 3, 4, 6, 12]) == 2
assert first_quantile([657, 32, 49, 124, 99]) == 40.5


# 32 2nd quantile
@median_from_list_deco
def second_quantile(list_of_numbers):
    return list_of_numbers


assert second_quantile([1, 2, 3, 4, 5]) == 3
assert second_quantile([657, 32, 49, 124, 99, 12]) == 74


# 33 3rd quantile
def third_quantile(list_of_numbers):
    sorted_numbers = sorted(list_of_numbers)
    position = ((3 * (len(sorted_numbers) + 1)) / 4)
    lower_index = int(position) - 1
    fraction = position % 1
    if fraction > 0:
        return sorted_numbers[lower_index] + fraction * (sorted_numbers[lower_index + 1] - sorted_numbers[lower_index])
    else:
        return sorted_numbers[lower_index]


assert third_quantile([1, 2, 3, 4, 5]) == 4.5
assert third_quantile([12, 32, 49, 99, 124, 657]) == 257.25


# 34 4th quantile
def fourth_quantile(list_of_numbers):
    return sorted(list_of_numbers)[-1]


assert fourth_quantile([1, 2, 3, 4, 5]) == 5
assert fourth_quantile([12, 32, 49, 99, 124, 657]) == 657


# 35 km to miles
def km_to_miles(number):
    return round(number * 0.621371, 2)
assert km_to_miles(100) == 62.14
assert km_to_miles(20) == 12.43

# 36. miles to km
def miles_to_km(number):
    return round(number * 1.60934, 2)

assert miles_to_km(10) == 16.09
assert miles_to_km(50) == 80.47


#37. currency counter
def currency_counter(amount,exchange_rate):
    from decimal import Decimal
    return round(float(Decimal(f'{amount}') * Decimal(f'{exchange_rate}')),2)

assert currency_counter(254, 4.3319) == 1100.30
assert currency_counter(65, 0.24223) == 15.74