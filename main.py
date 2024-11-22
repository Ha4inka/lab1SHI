import math


def compute_function(x):
    if x <= 0:
        denominator = 1 - math.exp(x)
        if denominator == 0:
            return "Знаменник 1 - e^x дорівнює нулю"
        return f"tg(x / (1 - e^x)): {math.tan(x / denominator)}"

    elif x > 1:
        if x - 3 <= 0:
            return "Підкореневий вираз ln(x - 3) від'ємний або дорівнює нулю"
        return f"sqrt(ln(x - 3)): {math.sqrt(math.log(x - 3))}"
    else:
        return "Функція не визначена для цього значення x"


def main():
    print("Ця програма обчислює значення складної функції залежно від введеного аргументу.")
    key_x = float(input("Введіть ключове значення x: "))
    try:
        while True:
            x = float(input("Введіть значення x: "))
            if x == key_x:
                print("Ви ввели ключове значення x. Програма завершується.")
                break
            result = compute_function(x)
            print(result)

    except ValueError:
        print("Введено некоректне значення аргументу")


if __name__ == "__main__":
    main()
