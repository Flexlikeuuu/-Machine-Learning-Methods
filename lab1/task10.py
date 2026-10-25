def safe_divide_and_index():
    print("--- Демонстрация работы try / except / finally ---")
    data = [10, 20, 30]

    try:
        num1 = float(input("Введите делимое число: "))
        num2 = float(input("Введите делитель: "))
        res = num1 / num2
        print(f"Результат деления: {res}")

        idx = int(input(f"Введите индекс элемента списка (0-{len(data) - 1}): "))
        print(f"Элемент с индексом {idx}: {data[idx]}")

    except ZeroDivisionError:
        print("Перехвачена ошибка: Деление на ноль невозможно!")
    except ValueError:
        print("Перехвачена ошибка: Введено нечисловое значение!")
    except IndexError:
        print("Перехвачена ошибка: Выход за пределы массива (неверный индекс)!")
    except Exception as e:
        print(f"Перехвачено непредвиденное исключение: {e}")
    finally:
        print("Блок FINALLY: Этот код выполняется всегда, независимо от ошибок.")


if __name__ == "__main__":
    safe_divide_and_index()