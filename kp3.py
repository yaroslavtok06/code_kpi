class Sonar:
    def __init__(self, frequency: float):
        """Ініціалізація ехолота з заданою частотою."""
        self.frequency = frequency  # Частота ехолота в кГц
        self.depth = 0.0  # Глибина вимірювання в метрах

    def measure_depth(self) -> float:
        """Вимірює глибину, повертаючи випадкове значення."""
        import random
        self.depth = random.uniform(0.5, 100.0)  # Випадкова глибина від 0.5 до 100 метрів
        return self.depth

    def get_frequency(self) -> float:
        """Повертає частоту ехолота."""
        return self.frequency


class Map:
    def __init__(self):
        """Ініціалізація карти дна."""
        self.depths = []  # Список виміряних глибин

    def add_depth(self, depth: float):
        """Додає виміряну глибину на карту."""
        self.depths.append(depth)

    def display_map(self):
        """Виводить карту дна (виміряні глибини)."""
        print("Карта дна:")
        for i, depth in enumerate(self.depths):
            print(f"Точка {i + 1}: {depth:.2f} м")


class Echosounder:
    def __init__(self, frequency: float):
        """Ініціалізація ехолота з частотою та створення карти дна."""
        self.sonar = Sonar(frequency)  # Створює екземпляр Sonar
        self.map = Map()  # Створює екземпляр Map

    def perform_measurement(self):
        """Виконує вимірювання глибини та додає його до карти."""
        depth = self.sonar.measure_depth()  # Вимірює глибину
        self.map.add_depth(depth)  # Додає глибину до карти

    def display_results(self):
        """Виводить результати вимірювань і карту дна."""
        print(f"Частота ехолота: {self.sonar.get_frequency()} кГц")
        self.map.display_map()


# Основна частина програми
if __name__ == "__main__":
    # Створення ехолота з частотою 200 кГц
    echosounder = Echosounder(frequency=200.0)

    # Виконання 5 вимірювань
    for _ in range(5):
        echosounder.perform_measurement()

    # Виведення результатів
    echosounder.display_results()
