import math

def calculate_with_for(n, x):
    try:
        result = 0
        for i in range(1, n+1):
            if i % 2 == 1:
                result += (n - i) / math.cos(i * x)
            else:
                result -= (n - i) / math.sin(i * x)
        return True, result
    except (ZeroDivisionError, ValueError):
        return False, None

def calculate_with_while(n, x):
    try:
        result = 0
        i = 1
        while i <= n:
            if i % 2 == 1:
                result += (n - i) / math.cos(i * x)
            else:
                result -= (n - i) / math.sin(i * x)
            i += 1
        return True, result
    except (ZeroDivisionError, ValueError):
        return False, None

def calculate_with_recursion(n, x, i=1, result=0):
    try:
        if i > n:
            return True, result
        if i % 2 == 1:
            result += (n - i) / math.cos(i * x)
        else:
            result -= (n - i) / math.sin(i * x)
        return calculate_with_recursion(n, x, i + 1, result)
    except (ZeroDivisionError, ValueError):
        return False, None

n = int(input("Введіть n (натуральне число): "))
x = float(input("Введіть x (дійсне число): "))

success_for, result_for = calculate_with_for(n, x)
success_while, result_while = calculate_with_while(n, x)
success_recursion, result_recursion = calculate_with_recursion(n, x)

if success_for:
    print(f"Результат обчислення за допомогою for: {result_for}")
else:
    print("Помилка обчислення в циклі for.")

if success_while:
    print(f"Результат обчислення за допомогою while: {result_while}")
else:
    print("Помилка обчислення в циклі while.")

if success_recursion:
    print(f"Результат обчислення за допомогою рекурсії: {result_recursion}")
else:
    print("Помилка обчислення в рекурсії.")
