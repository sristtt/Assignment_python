### 1. Sum of Two Numbers
python
def sum_two_numbers():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("The sum is:", num1 + num2)

sum_two_numbers()


### 2. Check Even or Odd
python
def check_even_odd():
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print(f"{num} is even.")
    else:
        print(f"{num} is odd.")

check_even_odd()


### 3. Factorial of a Number
python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

num = int(input("Enter a number: "))
print("Factorial is:", factorial(num))


### 4. Greeting Message
python
def greet_user():
    name = input("Enter your name: ")
    print(f"Hello, {name}!")

greet_user()


### 5. Write String to a Text File
python
def write_string_to_file():
    user_input = input("Enter a string: ")
    with open("output.txt", "w") as file:
        file.write(user_input)

write_string_to_file()


### 6. Read Content of a Text File
python
def read_file_content():
    with open("output.txt", "r") as file:
        content = file.read()
    print(content)

read_file_content()


### 7. Length of a String
python
def string_length():
    user_input = input("Enter a string: ")
    print("The length of the string is:", len(user_input))

string_length()


### 8. Concatenate Two Strings
python
def concatenate_strings():
    str1 = input("Enter first string: ")
    str2 = input("Enter second string: ")
    print("Concatenated string is:", str1 + str2)

concatenate_strings()


### 9. Check Substring Presence
python
def check_substring():
    main_str = input("Enter the main string: ")
    sub_str = input("Enter the substring: ")
    if sub_str in main_str:
        print(f"'{sub_str}' is present in the main string.")
    else:
        print(f"'{sub_str}' is not present in the main string.")

check_substring()


### 10. Convert String to Uppercase
python
def convert_to_uppercase():
    user_input = input("Enter a string: ")
    print("Uppercase string is:", user_input.upper())

convert_to_uppercase()


### 11. Fibonacci Sequence
python
def fibonacci(n):
    fib_seq = [0, 1]
    while len(fib_seq) < n:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq[:n]

n = int(input("Enter the number of Fibonacci numbers to generate: "))
print(fibonacci(n))


### 12. Sum of Digits
python
def sum_of_digits():
    num = input("Enter a number: ")
    digit_sum = sum(int(digit) for digit in num)
    print("Sum of digits is:", digit_sum)

sum_of_digits()


### 13. Calculate Age
python
def calculate_age():
    birth_year = int(input("Enter your birth year: "))
    current_year = 2024  # Or use datetime module to get current year
    age = current_year - birth_year
    print("Your age is:", age)

calculate_age()


### 14. Read Multiple Lines
python
def read_multiple_lines():
    print("Enter multiple lines (press Enter on an empty line to finish):")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    print("You entered:")
    for line in lines:
        print(line)

read_multiple_lines()


### 15. Read CSV File
python
import csv

def read_csv_file(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(', '.join(row))

# Call the function with the path to your CSV file
read_csv_file('data.csv')


### 16. Character Frequency in a String
python
def char_frequency(s):
    frequency = {}
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

user_input = input("Enter a string: ")
print(char_frequency(user_input))


### 17. Convert String to Title Case
python
def to_title_case(s):
    return s.title()

user_input = input("Enter a string: ")
print(to_title_case(user_input))


### 18. Check Anagrams
python
def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
print("The strings are anagrams:", are_anagrams(str1, str2))


### 19. Remove Punctuation
python
import string

def remove_punctuation(s):
    return s.translate(str.maketrans('', '', string.punctuation))

user_input = input("Enter a string: ")
print(remove_punctuation(user_input))


### 20. Sum of a List of Numbers
python
def sum_of_list(nums):
    return sum(nums)

nums = list(map(int, input("Enter a list of numbers separated by space: ").split()))
print("Sum of the list is:", sum_of_list(nums))


### 21. Count Occurrences in a List
python
def count_occurrences(nums, element):
    return nums.count(element)

nums = list(map(int, input("Enter a list of numbers separated by space: ").split()))
element = int(input("Enter the element to count: "))
print(f"{element} occurs {count_occurrences(nums, element)} times in the list.")


### 22. Min and Max in a List
python
def min_and_max(nums):
    return min(nums), max(nums)

nums = list(map(int, input("Enter a list of numbers separated by space: ").split()))
min_val, max_val = min_and_max(nums)
print(f"Minimum value is: {min_val}")
print(f"Maximum value is: {max_val}")


### 23. Temperature Conversion
python
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

choice = input("Convert from (C)elsius or (F)ahrenheit? ")
if choice.lower() == 'c':
    c = float(input("Enter temperature in Celsius: "))
    print("Temperature in Fahrenheit is:", celsius_to_fahrenheit(c))
elif choice.lower() == 'f':
    f = float(input("Enter temperature in Fahrenheit: "))
    print("Temperature in Celsius is:", fahrenheit_to_celsius(f))
else:
    print("Invalid choice.")


### 24. Simple Calculator
python
def simple_calculator():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operator = input("Enter operator (+, -, *, /): ")

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Error: Division by zero."
    else:
        return "Invalid operator."

    return result

print("Result:", simple_calculator())


### 25. Copy Text File Content
python
def copy_file_content(src, dst):
    with open(src, 'r') as source_file:
        content = source_file.read()
    with open(dst, 'w') as destination_file:
        destination_file.write(content)

copy_file_content('source.txt', 'destination.txt')


### 26. Check Prefix or Suffix
python
def check_prefix_suffix(s, prefix, suffix):
    return s.startswith(prefix), s.endswith(suffix)

s = input("Enter a string: ")
prefix = input("Enter the prefix: ")
suffix = input("Enter the suffix: ")
starts_with, ends_with = check_prefix_suffix(s, prefix, suffix)
print(f"Starts with {prefix}: {starts_with}")
print(f"Ends with {suffix}: {ends_with}")


### 27. Convert String to List of Characters
python
def string_to_list_of_characters(s):
    return list(s)

user_input = input("Enter a string: ")
print(string_to_list_of_characters(user_input))
