# 1. Generator for multiplication (power operation)
import string
import random
from curses.ascii import isalpha
from operator import contains


def multiplier_factor(number):
    def multiplier_n(base):
        return base ** number

    return multiplier_n


multi_2 = multiplier_factor(2)
assert multi_2(2)


# 2. Reversing a text
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


# 5. Division of even numbers
def division_of_even_numbers(dividend, divisor):
    if divisor % 2 == 0:
        return dividend / divisor
    else:
        return 'The divisor is an odd number'


assert division_of_even_numbers(2, 3) == 'The divisor is an odd number'
assert division_of_even_numbers(744, 744) == 1


# 6. Division of odd numbers
def division_of_odd_numbers(dividend, divisor):
    if divisor % 2 != 0:
        return dividend / divisor
    else:
        return 'The divisor is an even number'


assert division_of_odd_numbers(2, 2) == 'The divisor is an even number'
assert division_of_odd_numbers(743, 743) == 1


# 7. letter case switch
def letter_case_switch(text):
    return ''.join(letter.upper() if letter.islower()
                   else letter.lower() if letter.isupper() else letter for letter in text)


assert letter_case_switch("PoKEMoN") == "pOkemOn"
assert letter_case_switch("jezus666CHRYSTUS") == "JEZUS666chrystus"


# 8. odd or even checker
def odd_even_checker(number):
    if number % 2 == 0:
        return 'even number'
    else:
        return 'odd number'


assert odd_even_checker(2) == 'even number'
assert odd_even_checker(743) == 'odd number'


# 9. do string contains letters
def it_has_letters(string):
    if any(sign.isalpha() for sign in string):
        return 'it contains letters'
    else:
        return 'it does not contain letters'


assert it_has_letters('pokemon') == 'it contains letters'
assert it_has_letters('666') == 'it does not contain letters'


# 10. do string contains number
def it_has_number(string):
    if any(sign.isdigit() for sign in string):
        return 'it contains numbers'
    else:
        return 'it does not contain numbers'


assert it_has_number('666') == 'it contains numbers'
assert it_has_number('pokemon') == 'it does not contain numbers'


# 11. do string contains special
def it_has_special(string):
    if any(not sign.isalpha() and not sign.isdigit() for sign in string):
        return 'it has special characters'
    else:
        return 'it does not have special characters'


assert it_has_special('pokemon') == 'it does not have special characters'
assert it_has_special('6pok!!!!emon6') == 'it has special characters'


# 12. change 2 for 4 in number:
def change_two_for_four(number):
    return int(''.join(i if i != '2' else '4' for i in str(number)))


assert change_two_for_four(666) == 666
assert change_two_for_four(6226446) == 6446446


# 13. whitespace for '-'
def whitespace_changer(text):
    return ''.join('-' if i == ' ' else i for i in text)


assert whitespace_changer("hello world") == "hello-world"
assert whitespace_changer("hello-world") == "hello-world"


# 14. cut in half and switch sides in str

def cut_and_flip(text):
    first_half = text[:len(text) // 2]
    second_half = text[len(text) // 2:].lstrip()
    return second_half + ' ' + first_half


assert cut_and_flip("hello world") == "world hello"
assert cut_and_flip("h e l l 6 6 6") == "l 6 6 6 h e l "


# 15. if sum of numbers is smaller than chosen number
def is_smaller_than_number(to_check):
    def if_sum_is_smaller(*numbers):
        return sum(numbers) < to_check

    return if_sum_is_smaller


smaller_than_100 = is_smaller_than_number(100)
assert smaller_than_100(100, 233, 443) == False
assert smaller_than_100(1, 2, 4) == True

smaller_than_666 = is_smaller_than_number(666)
assert smaller_than_666(66, 66) == True
assert smaller_than_666(66, 66, 66, 66, 666, 666, 666) == False


# 16. three random letter gen gun
def letter_three_shot():
    letters = string.ascii_lowercase
    for _ in range(3):
        yield random.choice(letters)


loaded_gun = letter_three_shot()

shoots = [letter for letter in loaded_gun]
assert len(shoots) == 3
assert all(letter.isalpha() for letter in shoots)


# 17. double letters cutter
def drop_same_letter(text):
    new_str = ''
    for i in range(len(text) - 1):
        if text[i] != text[i + 1]:
            new_str += text[i]
    new_str += text[-1]
    return new_str


assert drop_same_letter('hello world') == 'helo world'
assert drop_same_letter('helo world') == 'helo world'


# 18. if next letter is different multiply the letter
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


# 19. duplicate number by chosen amount
def copy_number_chosen_amount(number, amount_of_copy):
    return int(''.join(item * amount_of_copy for item in str(number)))


assert copy_number_chosen_amount(42, 2) == 4422
assert copy_number_chosen_amount(666, 4) == 666666666666

# 20.
