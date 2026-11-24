
import random

def reverse_number(number):
    s = str(number)
    return (s[::-1])

def reverse_decimal(number):
    s = str(number)
    parts = s.split('.')
    return f"{parts[1]}.{parts[0]}"

def print_squares(numbers):
    for n in numbers:
        if  1 <= n <= 10:
             print(n**2)

def print_average(numbers):
    if len(numbers) == 0:
        print("No numbers to average.")
    else:
        s = sum(numbers)
        avg = s / len(numbers)
        print(avg)  

def calculate(items):
    a, op, b = items

    if op == "+":
        print(a + b)
    elif op == "-":
        print(a - b)    
    elif op == "*":   
        print(a * b)
    elif op == "/": 
        if b == 0:
            print("Error: Division by zero.")
        else:
            print(a / b)    
    elif op == "%": 
        if b == 0:
            print("Error: Division by zero.")
        else:
            print(a % b)
    else:
        print("Unknown operator")

def filter_by_four_ver1(numbers):
    result = [] 
    for n in numbers:
        if n % 4 == 0:
            result.append(n)    
    return result

def filter_by_four_ver2(numbers):
    return [n for n in numbers if n % 4 == 0]

def print_median(numbers):
    mid = len(numbers) // 2
    if len(numbers) % 2 == 1:
       print(numbers[mid])
    else:
        print((numbers[mid - 1] + numbers[mid]) / 2)

def shuffled_words(songwords):
    words = songwords.split()
    random.shuffle(words)
    return words

def print_shuffled_words(songwords):
    for word in shuffled_words(songwords):
        print(word)

def longest_string(strings):
    longest = strings[0]
    for s in strings:
        if len(s) > len(longest):
            longest = s
    return longest

def find_strings(strings, search):
    result = []
    for s in strings:
        if search in s:
            result.append(s)
    return result

def print_top_student(data):
    grades = data[0]
    names = data[1]
    best = 0
    for i in range(len(grades)):
        if int(grades[i]) > int(grades[best]):
            best = i
    print(grades[best], names[best])

def print_second_top_number(numbers):
    unique = sorted(set(numbers))
    if len(unique) < 2:
        print("Not enough numbers.")
        return
    print(unique[-2])
