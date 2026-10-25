def main():
    numbers = [3, -2, 0, 5, -1, 4, 0, -8, 10]
    print("Исходный список:", numbers)

    pos_sum = sum(x for x in numbers if x > 0)
    print(f"Сумма положительных элементов: {pos_sum}")

    if 0 in numbers:
        first_zero_index = numbers.index(0)
        elements_after_zero = numbers[first_zero_index + 1:]
        print(f"Сумма элементов после первого нуля: {sum(elements_after_zero)}")
    else:
        print("Сумму посчитать нельзя")

    non_negative_numbers = [x for x in numbers if x >= 0]
    print("Список после удаления отрицательных элементов:", non_negative_numbers)

if __name__ == "__main__":
    main()