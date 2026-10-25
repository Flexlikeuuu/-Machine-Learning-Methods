import random

def main():
    random_digits_str = "".join([str(random.randint(0, 9)) for _ in range(20)])
    print(f"Сгенерированная строка: {random_digits_str}")

    result_dict = {}
    for char in random_digits_str:
        digit = int(char)
        result_dict[digit] = result_dict.get(digit, 0) + 1

    print("Результат:", dict(sorted(result_dict.items())))

if __name__ == "__main__":
    main()