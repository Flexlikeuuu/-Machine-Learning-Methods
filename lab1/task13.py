class Stationery:
    def __init__(self, title: str):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print(f"Отрисовка ручкой '{self.title}': синяя тонкая линия.")


class Pencil(Stationery):
    def draw(self):
        print(f"Отрисовка карандашом '{self.title}': серый эскизный штрих.")


class Handle(Stationery):
    def draw(self):
        print(f"Отрисовка маркером '{self.title}': яркая широкая полоса.")


if __name__ == "__main__":
    base_item = Stationery("Базовый предмет")
    pen = Pen("ErichKrause")
    pencil = Pencil("Koh-i-Noor")
    marker = Handle("Textsurfer")

    base_item.draw()
    pen.draw()
    pencil.draw()
    marker.draw()