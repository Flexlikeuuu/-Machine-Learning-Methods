def is_decreasing_from_right(number: int) -> bool:
    s = str(number)
    for i in range(len(s) - 1, 0, -1):
        if int(s[i - 1]) < int(s[i]):
            return False
    return True


def main():
    try:
        num = int(input("Введите натуральное число: "))
        if num <= 0:
            print("Ошибка: число должно быть натуральным.")
            return

        if is_decreasing_from_right(num):
            print(f"Последовательность цифр числа {num} справа налево упорядочена по убыванию.")
        else:
            print(f"Последовательность цифр числа {num} справа налево НЕ является упорядоченной по убыванию.")
    except ValueError:
        print("Ошибка: введено не целое число.")


if __name__ == "__main__":
    main()