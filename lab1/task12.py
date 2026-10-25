import time
import sys


class TrafficLight:
    def __init__(self):
        self.__color = None

    def running(self):
        modes = [
            ("красный", 7),
            ("жёлтый", 2),
            ("зелёный", 5)
        ]

        expected_order = ["красный", "жёлтый", "зелёный"]

        for idx, (color_name, duration) in enumerate(modes):
            if expected_order[idx] != color_name:
                print(f"Ошибка! Нарушен порядок режимов. Ожидался: {expected_order[idx]}, получен: {color_name}")
                sys.exit()

            self.__color = color_name
            print(f"Светофор: {self.__color} (длительность {duration} сек.)")
            time.sleep(duration)


if __name__ == "__main__":
    traffic_light = TrafficLight()
    traffic_light.running()