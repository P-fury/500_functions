# 1. Generator for multiplication (power operation)
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