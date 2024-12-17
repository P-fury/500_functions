# 1. Generator for exponentiation
import re
import string
import random
import io
import sys
from enum import Enum
from idlelib.colorizer import prog_group_name_to_tag
from operator import contains
import math
from tempfile import tempdir
from typing import Callable, List, Any, Tuple
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


# # 21. Fetch currency rate in PLN
# def currency_rate_in_pln(currency):
#     url = f'https://api.nbp.pl/api/exchangerates/rates/a/{currency}/'
#     try:
#         response = requests.get(url)
#         return response.json()
#     except ValueError:
#         return None
#
#
# assert isinstance(currency_rate_in_pln('USD'), dict)
# assert currency_rate_in_pln('blablabla') is None


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


# 30 median of list
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


# 37. currency counter
def currency_counter(amount, exchange_rate):
    from decimal import Decimal
    return round(float(Decimal(f'{amount}') * Decimal(f'{exchange_rate}')), 2)


assert currency_counter(254, 4.3319) == 1100.30
assert currency_counter(65, 0.24223) == 15.74


# 38. word counter
def word_counter(text):
    return len(text.split())


assert word_counter('hello world') == 2
assert word_counter('hello world hello worldhello world') == 5


# 39. carbonation
def fib(n):
    a = 0
    b = 1
    if n == 0:
        return 0
    elif n == 1:
        return b
    else:
        for i in range(1, n):
            c = a + b
            a = b
            b = c
        return b


assert fib(121) == 8670007398507948658051921
assert fib(21) == 10946


# 40. power
def power(n):
    x = 1
    for number in range(1, n + 1):
        x = x * number
    return x


assert power(5) == 120
assert power(12) == 479001600


# 41. list division from left or right
def left_or_right_list_division(list_of_numbers: list, *, side: str = 'left') -> float:
    if side == 'left':
        result = list_of_numbers[0]
        for number in list_of_numbers[1:]:
            result /= number
        return round(result, 8)
    if side == 'right':
        result = list_of_numbers[-1]
        for number in reversed(list_of_numbers[:-1]):
            result /= number
        return round(result, 8)
    else:
        raise ValueError("Invalid value for side. Use 'left' or 'right'.")


assert left_or_right_list_division([23, 24, 27, 28]) == 0.00126764
assert left_or_right_list_division([33, 35, 37, 31], side='right') == 0.0007254


# 42. list step multiplicator
def list_step_multiply(list_of_numbers: list, step: int = 2) -> int:
    result = list_of_numbers[0]
    for number in list_of_numbers[1::step]:
        result *= number
    return result


assert list_step_multiply([2, 2, 2, 2, 2, 2], 2) == 16
assert list_step_multiply([2, 2, 2, 2, 2, 2], 3) == 8


# 43. distance calc meters, feet
def distance_calc(distance: float, base: str = 'm') -> float:
    if base == 'm':
        return round(distance * 3.2808, 2)
    else:
        return round(distance / 3.281, 2)


assert distance_calc(2.5) == 8.20
assert distance_calc(666, base='feet') == 202.99


# 44. random string creator
def random_string(length: int, number_of_words: int = 1, separator: str = '') -> str:
    letters = string.ascii_lowercase
    result = ''
    step = 0
    for _ in range(number_of_words):
        result += ''.join(random.choice(letters) for i in range(length))
        step += 1
        if step != length:
            result += separator
    return result


assert len(random_string(2)) == 2
assert len(random_string(3, 3, '$')) == 11


# 45. random string in range
def random_str_in_range(length: int = 1) -> str:
    length = random.randint(1, length)
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))


assert len(random_str_in_range(2)) <= 2
assert len(random_str_in_range(666)) <= 666
assert isinstance(random_str_in_range(23), str)


# 46. random string in range create from random word range
def ultra_random_str(length: int = 1, words: int = 1, separator: str = ' ') -> str:
    result = []
    words_number = random.randint(1, words)
    for _ in range(words_number):
        letters_length = random.randint(1, length)
        word = ''.join(random.choice(string.ascii_lowercase) for _ in range(letters_length))
        result.append(word)
    return separator.join(result)


assert isinstance(ultra_random_str(), str)
assert len(ultra_random_str(10, 2, '!')) <= 21


# 47. simple decorator
def before_and_after(funk):
    def wrapper(text):
        print('before funk')
        result = funk(text)
        print('after funk')
        return result

    return wrapper


@before_and_after
def say_text(text: str = 'hello world') -> str:
    print(f'{text} from the heart')
    return f'{text}'


# tests:
captured_output = io.StringIO()
sys.stdout = captured_output

say_text('hello world')

sys.stdout = sys.__stdout__
output = captured_output.getvalue()

assert "hello world" in output
assert 'before funk' in output
assert 'after funk' in output
assert 'heart' in output


# 48. biggest number from list
def biggest_from_lst(lst: list) -> int:
    memory = lst[0]
    for index in range(1, len(lst)):
        if lst[index] > memory:
            memory = lst[index]
    return memory


assert biggest_from_lst([55, 1, 2, 3, 4, 5]) == 55
assert biggest_from_lst([34, 56, 873, 2, 34, 467 * 5, 1202]) == 467 * 5


# 49. smallest from list
def smallest_from_lst(lst: list) -> int:
    memory = lst[0]
    for index in range(1, len(lst)):
        if lst[index] < memory:
            memory = lst[index]
    return memory


assert smallest_from_lst([55, 1, 2, 3, 4, 5]) == 1
assert smallest_from_lst([2342, 43324, 5554, 123, 4332, 45221, 432]) == 123


# 50. prime number
def prime_number_checker(number: int) -> bool:
    division_lst = []
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            division_lst.append(i)
    if len(division_lst) > 1:
        return False
    else:
        return True


assert prime_number_checker(1000003) == True
assert prime_number_checker(28) == False


# 51. faster prime number
def faster_prime_number_checker(number: int) -> bool:
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False

    for i in range(3, int((number ** 0.5)) + 1, 2):
        if number % i == 0:
            return False
    return True


assert faster_prime_number_checker(1000003) == True
assert faster_prime_number_checker(2147483647) == True
assert faster_prime_number_checker(28) == False


# 52. punkty rozproszeone w danym przedziale
def range_with_float_distance(start: float, end: float, distance: float) -> list:
    result = []
    memory = start
    while memory <= end:
        result.append(memory)
        memory += distance
    return result


assert range_with_float_distance(1, 2, 1) == [1, 2]
assert len(range_with_float_distance(1, 2, 0.25)) == 5


# 53. armstrong number
def armstrong(number: int) -> bool:
    return number == sum(int(i) ** len(str(number)) for i in str(number))


assert armstrong(1000003) == False
assert armstrong(153) == True


# 54. if armstrong in lst
def armstrong_list():
    def decorator(func):
        def wrapper(numbers: list) -> list:
            return [number for number in numbers if func(number)]

        return wrapper

    return decorator


@armstrong_list()
def armstrong(number):
    return number == sum(int(i) ** len(str(number)) for i in str(number))


assert armstrong([1, 2, 3, 123, 154, 153, 666, 748]) == [1, 2, 3, 153]
assert armstrong([23, 435, 4356, 3334, 532]) == []


# 55. perfect number
def is_perfect_number(number: int) -> bool:
    result = [i for i in range(1, number + 1) if number % i == 0][:-1]
    return number == sum(result)


assert is_perfect_number(28) == True
assert is_perfect_number(1000003) == False
assert is_perfect_number(8128) == True


# 56. perfect number in list
def funk_on_list(funk: Callable[[int], bool], list_of_numbers: list) -> list:
    result = []
    for number in list_of_numbers:
        result.append(funk(number))

    return result


assert True in funk_on_list(is_perfect_number, [5, 6, 7, 8, 9])
assert not True in funk_on_list(is_perfect_number, [14, 10, 23, 54])


# 57. happy number
def is_happy_number(number: int) -> bool:
    def sum_of_squares(numb: int) -> int:
        return sum(int(digit) ** 2 for digit in str(numb))

    checked = set()
    while number != 1 and number not in checked:
        checked.add(number)
        number = sum_of_squares(number)
    return number == 1


assert is_happy_number(2147483647) == False
assert is_happy_number(19) == True

# 58. happy number in list
assert True in funk_on_list(is_happy_number, [5, 6, 7, 8, 9])
assert False in funk_on_list(is_happy_number, [14, 10, 23, 54])


# 59. is palindromic number
def is_palindromic_number(number: int) -> bool:
    return str(number) == str(number)[::-1]


assert is_palindromic_number(2147483647) == False
assert is_palindromic_number(6574756) == True


# 60. is palindromic lst decorator


def is_palindromic_for_list(funk: Callable[[int], bool]) -> Callable[[list], list[bool]]:
    def wrapper(numbers: list) -> list[bool]:
        return [funk(number) for number in numbers]

    return wrapper


@is_palindromic_for_list
def is_palindromic_number(number: int) -> bool:
    return str(number) == str(number)[::-1]


assert False in (is_palindromic_number([12, 2, 3, 4, 5]))
assert is_palindromic_number([123321, 666, 1233442]) == [True, True, False]


# 61. is Harshad number
def is_harshad_number(number: int) -> bool:
    return (number / (sum(int(digit) for digit in str(number)))) % 2 == 0


assert is_harshad_number(3) == False
assert is_harshad_number(18) == True


# 62. is Harshad number in list

def for_list(funk: Callable[[int], bool]) -> Callable[[list], list[bool]]:
    def wrapper(numbers: list) -> list[bool]:
        return [funk(number) for number in numbers]

    return wrapper


@for_list
def is_harshad_number(number: int) -> bool:
    return (number / (sum(int(digit) for digit in str(number)))) % 2 == 0


assert is_harshad_number([3, 18, 21]) == [False, True, False]
assert sum(is_harshad_number([123, 43, 52, 674])) == False


# 63. Amicable Numbers
def amicable_number(number1: int, number2: int) -> bool:
    divisors_lst = []
    for i in range(1, int(number1 / 2 + 1)):
        if number1 % i == 0:
            divisors_lst.append(i)

    return sum(divisors_lst) == number2


assert amicable_number(1, 2) == False
assert amicable_number(220, 284) == True


# 64. Twin Primes (nie uzywac dwoch typow danych)
def is_twin_primes(number1: int, number2: int) -> str | bool:
    if not prime_number_checker(number1):
        return 'first number is not prime'
    if not prime_number_checker(number2):
        return 'second number is not prime'
    return abs(number1 - number2) == 2


assert is_twin_primes(4, 2) == True
assert is_twin_primes(12, 2) == 'first number is not prime'


# 65. Deficient Number
def is_deficient_number(number: int) -> bool:
    return sum(i for i in range(1, int((number / 2) + 1)) if number % i == 0) < number


assert is_deficient_number(12) == False
assert is_deficient_number(10) == True


# 66. Deficient Number for list
def is_deficient_number_from_list(lst: List[int]) -> Tuple[List[bool], List[int]]:
    result_lst = []
    for number in lst:
        divisors_sum = sum(i for i in range(1, int((number / 2) + 1)) if number % i == 0)
        result_lst.append(divisors_sum < number)
    return result_lst, lst


assert is_deficient_number_from_list([1, 2]) == ([True, True], [1, 2])
assert is_deficient_number_from_list([83676, 54, 6])[0] == [False, False, False]


# 67.Abundant Numbers
def is_abundant_number(number: int) -> bool:
    return sum(i for i in range(1, int((number / 2) + 1)) if number % i == 0) > number


assert is_abundant_number(24) == True
assert is_abundant_number(9) == False


# 68. Abundant Numbers on list
def is_deficient_number_from_list(lst: List[int]) -> Tuple[List[bool], List[int]]:
    result_lst = []
    for number in lst:
        divisors_sum = sum(i for i in range(1, int((number / 2) + 1)) if number % i == 0)
        result_lst.append(divisors_sum > number)
    return result_lst, lst


assert is_deficient_number_from_list([1, 2]) == ([False, False], [1, 2])
assert is_deficient_number_from_list([83676, 54, 102])[0] == [True, True, True]


# 69. Kaprekar Numbers
def is_kaprekar_number(number: int) -> bool:
    squared = number ** 2
    half_of_length = int(len(str(squared)) / 2)
    return int(str(squared)[:half_of_length]) + int(str(squared)[half_of_length:]) == number


assert is_kaprekar_number(461539) == True
assert is_kaprekar_number(30884184) == True
assert is_kaprekar_number(72) == False


# 70. is Automorphic Numbers
def is_automorphic_number(number: int) -> bool:
    squared = number ** 2
    length_of_number = len(str(number))
    return int(str(squared)[-length_of_number:]) == number


assert is_automorphic_number(2) == False
assert is_automorphic_number(5) == True
assert is_automorphic_number(76) == True


# 71. how many sticks needed for a number
def amount_of_sticks_for_number(number: int) -> int:
    segments = {
        0: 6,
        1: 2,
        2: 5,
        3: 5,
        4: 4,
        5: 5,
        6: 6,
        7: 3,
        8: 7,
        9: 6
    }
    return sum(segments[int(i)] for i in str(number))


assert amount_of_sticks_for_number(1111) == 8
assert amount_of_sticks_for_number(999000111) == 42

# 72. lambda add
add = lambda x, y: x + y
assert (add(1, 2)) == 3
assert (add(132, 132)) == 264


# 73. sum all args
def sum_all(*args):
    return sum(args)


assert sum_all(1, 2, 3) == 6
assert sum_all(2, 2, 2, 2, 2, 2, 2, 2, 2) == 18


# 75. Class for converting distances between various units
class Distance:
    # 76. Constructor to initialize distance in meters
    def __init__(self, distance: float):
        self.distance_m = distance

    # 77. Property to get the distance in meters
    @property
    def distance_m(self):
        return f'{self._distance_m:.2f} meters'

    # 78. Setter to set the distance in meters
    @distance_m.setter
    def distance_m(self, value):
        if value <= 0:
            raise ValueError('Distance must be greater than 0')
        self._distance_m = value

    # 79. Property to get the distance in feet
    @property
    def distance_ft(self):
        return f'{3.28084 * self._distance_m:.2f} feet'

    # 80. Setter to set the distance in feet
    @distance_ft.setter
    def distance_ft(self, value):
        self.distance_m = value / 3.28084

    # 81. Property to get the distance in millimeters
    @property
    def distance_mm(self):
        return f'{1000 * self._distance_m:.2f} millimeters'

    # 82. Setter to set the distance in millimeters
    @distance_mm.setter
    def distance_mm(self, value):
        self.distance_m = value / 1000

    # 83. Property to get the distance in centimeters
    @property
    def distance_cm(self):
        return f'{100 * self._distance_m:.2f} centimeters'

    # 84. Setter to set the distance in centimeters
    @distance_cm.setter
    def distance_cm(self, value):
        self.distance_m = value / 100

    # 85. Property to get the distance in inches
    @property
    def distance_in(self):
        return f'{39.3700787402 * self._distance_m:.2f} inches'

    # 86. Setter to set the distance in inches
    @distance_in.setter
    def distance_in(self, value):
        self.distance_m = value / 39.3700787402

    # 87. Property to get the distance in yards
    @property
    def distance_yd(self):
        return f'{1.093613298338 * self._distance_m:.2f} yards'

    # 88. Setter to set the distance in yards
    @distance_yd.setter
    def distance_yd(self, value):
        self.distance_m = value / 1.093613298338

    # 89. String representation of the distance in meters
    def __str__(self):
        return str(self.distance_m)


distance1 = Distance(12)
assert distance1.distance_m == '12.00 meters'
assert distance1.distance_ft == '39.37 feet'
assert distance1.distance_mm == '12000.00 millimeters'
assert distance1.distance_cm == '1200.00 centimeters'
assert distance1.distance_in == '472.44 inches'
assert distance1.distance_yd == '13.12 yards'

distance1.distance_mm = 10
assert distance1.distance_m == '0.01 meters'
assert distance1.distance_mm == '10.00 millimeters'

distance1.distance_cm = 100
assert distance1.distance_m == '1.00 meters'
assert distance1.distance_cm == '100.00 centimeters'

distance1.distance_in = 12
assert distance1.distance_m == '0.30 meters'
assert distance1.distance_in == '12.00 inches'

distance1.distance_yd = 1
assert distance1.distance_m == '0.91 meters'
assert distance1.distance_yd == '1.00 yards'
