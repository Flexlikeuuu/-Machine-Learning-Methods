bakery_data = {
    "Торт": ["Мука, сахар, крем, ягоды", 4.5, 1500],
    "Пирожное": ["Шоколад, бисквит, глазурь", 2.0, 800],
    "Маффин": ["Мука, изюм, корица", 1.2, 1200],
    "Рулет": ["Бисквит, джем, орехи", 3.0, 600]
}


def show_description():
    for name, info in bakery_data.items():
        print(f"{name} — {info[0]}")


def show_price():
    for name, info in bakery_data.items():
        print(f"{name} — {info[1]} руб.")


def show_quantity():
    for name, info in bakery_data.items():
        print(f"{name} — {info[2]} г.")


def show_all_info():
    for name, info in bakery_data.items():
        print(f"{name}: Состав ({info[0]}), Цена/100г: {info[1]} руб., Остаток: {info[2]} г.")


def process_purchase():
    total_cost = 0.0
    while True:
        name = input("Введите название продукции (или 'n' для выхода): ").strip().capitalize()
        if name.lower() == 'n':
            break

        if name not in bakery_data:
            print("Такого товара нет!")
            continue

        try:
            grams = float(input(f"Введите количество (г) для '{name}': "))
            if grams <= 0 or grams > bakery_data[name][2]:
                print("Некорректное количество или недостаточно товара!")
                continue

            cost = (grams / 100.0) * bakery_data[name][1]
            bakery_data[name][2] -= grams
            total_cost += cost
            print(f"Добавлено: {name} ({grams} г) на сумму {cost:.2f} руб.")
        except ValueError:
            print("Ошибка ввода!")

    print(f"\nИтоговая сумма: {total_cost:.2f} руб.")
    print("Остатки товаров:")
    for name, info in bakery_data.items():
        print(f"{name}: {info[2]} г.")


def main():
    while True:
        print(
            "\n1. Просмотр описания\n2. Просмотр цены\n3. Просмотр количества\n4. Вся информация\n5. Покупка\n6. До свидания")
        choice = input("Выберите пункт меню (1-6): ").strip()

        if choice == '1':
            show_description()
        elif choice == '2':
            show_price()
        elif choice == '3':
            show_quantity()
        elif choice == '4':
            show_all_info()
        elif choice == '5':
            process_purchase()
        elif choice == '6':
            print("До свидания!")
            break


if __name__ == "__main__":
    main()