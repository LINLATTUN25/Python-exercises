def show_type(value):
    print(type(value))

show_type(25)
show_type("hello")


def int_to_float(n):
    print(float(n))

int_to_float(7)


def str_to_int(s):
    print(int(s))

str_to_int("25")


def check_bool(value):
    print(bool(value))

check_bool(0)
check_bool("hello")
check_bool("")


def combine_strings(s1, s2):
    print(s1 + " " + s2)

combine_strings("Hello", "World")


def get_type_info(value):
    print("Type:", type(value))

    if isinstance(value, list):
        print("Mutable: True")
    else:
        print("Mutable: False")

get_type_info([1, 2, 3])
get_type_info((1, 2, 3))


def swap_without_temp(a, b):
    print("Before: a=" + str(a) + ", b=" + str(b))

    a, b = b, a

    print("After: a=" + str(a) + ", b=" + str(b))

swap_without_temp(5, 10)


def celsius_to_fahrenheit(c):
    print(round(c * 9 / 5 + 32, 2))

celsius_to_fahrenheit(37)


def concat_and_repeat(s1, s2, n):
    print((s1 + s2) * n)

concat_and_repeat("ab", "cd", 3)


def type_caster(value):
    try:
        print("int conversion:", int(value))
    except:
        print("int conversion: Failed")

    try:
        print("float conversion:", float(value))
    except:
        print("float conversion: Failed")

    print("bool conversion:", bool(value))

type_caster("25")
type_caster("hello")


def is_positive(n):
    if n > 0:
        print("Positive")
    elif n < 0:
        print("Negative")
    else:
        print("Zero")

is_positive(-5)
is_positive(0)
is_positive(8)


def is_even(n):
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")

is_even(7)
is_even(10)


def is_equal(a, b):
    if a == b:
        print("Equal")
    else:
        print("Not Equal")

is_equal(5, 5)
is_equal(5, 6)


def check_age(age):
    if age >= 18:
        print("Adult")
    else:
        print("Minor")

check_age(16)
check_age(20)


def is_empty_string(s):
    if s == "":
        print("Empty String")
    else:
        print("Not Empty")

is_empty_string("")
is_empty_string("hi")


def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

print(is_leap_year(2024))
print(is_leap_year(2023))


def grade_calculator(marks):
    if marks >= 80:
        print("Grade: A")
    elif marks >= 70:
        print("Grade: B")
    elif marks >= 60:
        print("Grade: C")
    elif marks >= 50:
        print("Grade: D")
    else:
        print("Grade: F")

grade_calculator(85)
grade_calculator(42)


def largest_of_three(a, b, c):
    if a >= b and a >= c:
        print("Largest:", a)
    elif b >= a and b >= c:
        print("Largest:", b)
    else:
        print("Largest:", c)

largest_of_three(4, 9, 7)


def check_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        print("Valid Triangle")
    else:
        print("Not a Valid Triangle")

check_triangle(3, 4, 5)
check_triangle(1, 2, 10)


def vowel_or_consonant(char):
    if char.lower() in "aeiou":
        print("Vowel")
    else:
        print("Consonant")

vowel_or_consonant("a")
vowel_or_consonant("b")


def add_numbers(a, b):
    print(a + b)

add_numbers(4, 6)


def subtract_numbers(a, b):
    print(a - b)

subtract_numbers(10, 4)


def multiply_numbers(a, b):
    print(a * b)

multiply_numbers(3, 5)


def divide_numbers(a, b):
    print(a / b)

divide_numbers(10, 4)


def find_remainder(a, b):
    print(a % b)

find_remainder(10, 3)


def calculator(a, b, operator):
    if operator == "+":
        print(a + b)
    elif operator == "-":
        print(a - b)
    elif operator == "*":
        print(a * b)
    elif operator == "/":
        if b == 0:
            print("Error: Division by zero")
        else:
            print(a / b)
    elif operator == "%":
        print(a % b)
    elif operator == "//":
        print(a // b)
    elif operator == "**":
        print(a ** b)
    else:
        print("Invalid operator")

calculator(10, 3, "+")
calculator(10, 3, "**")
calculator(10, 0, "/")


def bitwise_demo(a, b):
    print("AND:", a & b)
    print("OR:", a | b)
    print("XOR:", a ^ b)
    print("NOT a:", ~a)
    print("Left Shift (a<<1):", a << 1)
    print("Right Shift (a>>1):", a >> 1)

bitwise_demo(6, 3)


def compare_numbers(a, b):
    if a > b:
        print(a, "is greater than", b)
    elif a < b:
        print(a, "is less than", b)
    else:
        print(a, "is equal to", b)

compare_numbers(5, 8)


def logical_operator_check(a, b):
    print("a and b:", a and b)
    print("a or b:", a or b)
    print("not a:", not a)

logical_operator_check(True, False)


def is_divisible(a, b):
    if a % b == 0:
        print(a, "is divisible by", b)
    else:
        print(a, "is not divisible by", b)

is_divisible(10, 5)
is_divisible(10, 3)


def print_1_to_n(n):
    for i in range(1, n + 1):
        print(i)

print_1_to_n(5)


def print_n_to_1(n):
    for i in range(n, 0, -1):
        print(i)

print_n_to_1(5)


def print_even_numbers(n):
    for i in range(1, n + 1):
        if i % 2 == 0:
            print(i)

print_even_numbers(10)


def count_down(n):
    for i in range(n, -1, -1):
        print(i)

    print("Liftoff!")

count_down(3)


def repeat_message(msg, times):
    for i in range(times):
        print(msg)

repeat_message("Hi", 3)


def sum_of_natural_numbers(n):
    total = 0

    for i in range(1, n + 1):
        total = total + i

    print("Sum:", total)

sum_of_natural_numbers(5)


def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result = result * i

    print("Factorial:", result)

factorial(5)


def print_multiplication_table(n):
    for i in range(1, 11):
        print(n, "x", i, "=", n * i)

print_multiplication_table(5)


def count_digits(n):
    print("Number of digits:", len(str(n)))

count_digits(48293)


def fizzbuzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

fizzbuzz(15)