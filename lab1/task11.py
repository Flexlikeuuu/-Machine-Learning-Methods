class CustomList:
    def __init__(self, initial_data=None):
        self.data = list(initial_data) if initial_data is not None else []

    def append(self, item):
        self.data.append(item)

    def remove(self, item):
        if item in self.data:
            self.data.remove(item)

    def get(self, index):
        if 0 <= index < len(self.data):
            return self.data[index]
        raise IndexError("Индекс за пределами списка")

    def clear(self):
        self.data = []

    def size(self):
        return len(self.data)

    def display(self):
        print(f"Список: {self.data}")


if __name__ == "__main__":
    my_list = CustomList([1, 2, 3])
    my_list.append(4)
    my_list.display()
    print(f"Элемент с индексом 1: {my_list.get(1)}")
    my_list.remove(2)
    my_list.display()
    print(f"Размер списка: {my_list.size()}")
    my_list.clear()
    my_list.display()