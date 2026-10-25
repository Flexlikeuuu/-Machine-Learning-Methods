def main():
    numbers_tuple = (-5, 12, 0, 7, -3, 9, 14, -1, 2)
    print("Кортеж:", numbers_tuple)
    positive_count = sum(1 for x in numbers_tuple if x > 0)
    print(f"Количество положительных элементов: {positive_count}")

if __name__ == "__main__":
    main()