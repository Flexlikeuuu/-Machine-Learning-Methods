def process_data(data):
    try:
        if isinstance(data, list):
            new_list = [x for x in data if x >= 0]
            print(f"Список без отрицательных элементов: {new_list}")

            if 0 in new_list:
                zero_index = new_list.index(0)
                sum_after_zero = sum(new_list[zero_index + 1:])
                print(f"Сумма элементов после первого нуля: {sum_after_zero}")
            else:
                print("В списке нет нулевых элементов.")

        elif isinstance(data, tuple):
            if not data:
                raise ValueError("Кортеж пуст!")

            temp_list = list(data)
            max_val = max(temp_list)
            min_val = min(temp_list)

            max_idx = temp_list.index(max_val)
            min_idx = temp_list.index(min_val)

            temp_list[max_idx], temp_list[min_idx] = temp_list[min_idx], temp_list[max_idx]
            result_tuple = tuple(temp_list)

            print(f"Исходный кортеж: {data}")
            print(f"Максимум: {max_val}, Минимум: {min_val}")
            print(f"Кортеж после замены мест: {result_tuple}")

        elif isinstance(data, (int, float)) and not isinstance(data, bool):
            num_str = str(abs(int(data)))
            odd_sum = sum(int(digit) for digit in num_str if int(digit) % 2 != 0)
            print(f"Сумма нечетных цифр числа {data}: {odd_sum}")

        elif isinstance(data, str):
            words = data.split()
            even_length_count = sum(1 for word in words if len(word) % 2 == 0)
            print(f"Количество слов с четной длиной: {even_length_count}")

        else:
            raise TypeError("Передан неподдерживаемый тип данных!")

    except Exception as e:
        print(f"Произошла ошибка при обработке: {e}")
    finally:
        print("Обработка элемента завершена.\n")


if __name__ == "__main__":
    process_data([3, -2, 0, 5, -1, 4, 10])
    process_data((10, 2, 8, 1, 5))
    process_data(135782)
    process_data("Питон это отличный язык программирования")
    process_data({})