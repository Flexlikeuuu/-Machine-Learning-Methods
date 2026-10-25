def get_chinese_zodiac(year: int) -> str:
    animals = ["Обезьяна", "Петух", "Собака", "Свинья", "Крыса", "Бык",
               "Тигр", "Заяц", "Дракон", "Змея", "Лошадь", "Овца"]
    return animals[year % 12]


def process_years():
    while True:
        try:
            user_input = input("Введите год (или 0 для выхода): ").strip()
            year = int(user_input)

            if year == 0:
                print("Завершение работы программы.")
                break
            if year < 0:
                raise ValueError("Год не может быть отрицательным!")

            animal = get_chinese_zodiac(year)
            print(f"{year} год — год по китайскому календарю: {animal}")

        except ValueError as e:
            print(f"Ошибка ввода: {e}. Пожалуйста, введите целое положительное число.")
        finally:
            print("-" * 30)


if __name__ == "__main__":
    process_years()