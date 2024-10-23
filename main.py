import json


# Базовый класс Animal
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        """Базовый звук для всех животных."""
        return "Звук животного"

    def eat(self):
        return f"{self.name} ест."


# Подкласс Bird
class Bird(Animal):
    def __init__(self, name, age, wing_span):
        super().__init__(name, age)
        self.wing_span = wing_span

    def make_sound(self):
        return f"{self.name} чирикает."

    def fly(self):
        return f"{self.name} летит."


# Подкласс Mammal
class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        return f"{self.name} рычит."


# Подкласс Reptile
class Reptile(Animal):
    def __init__(self, name, age, is_poisonous):
        super().__init__(name, age)
        self.is_poisonous = is_poisonous

    def make_sound(self):
        return f"{self.name} шипит."


# Функция демонстрации полиморфизма
def animal_sound(animals):
    for animal in animals:
        print(animal.make_sound())


# Класс Zoo для композиции
class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Животное {animal.name} добавлено в зоопарк {self.name}.")

    def add_staff(self, staff):
        self.staff.append(staff)
        print(f"Сотрудник {staff.name} добавлен в зоопарк {self.name}.")

    def save_zoo(self, filename):
        """Сохраняет информацию о зоопарке в файл JSON."""
        data = {
            "animals": [{"name": a.name, "age": a.age, "type": type(a).__name__} for a in self.animals],
            "staff": [{"name": s.name, "type": type(s).__name__} for s in self.staff]
        }
        with open(filename, 'w') as f:
            json.dump(data, f)
        print(f"Информация о зоопарке сохранена в файл {filename}.")

    def load_zoo(self, filename):
        """Загружает информацию о зоопарке из файла JSON."""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            for a in data['animals']:
                if a['type'] == 'Bird':
                    self.animals.append(Bird(a['name'], a['age'], 1))
                elif a['type'] == 'Mammal':
                    self.animals.append(Mammal(a['name'], a['age'], 'brown'))
                elif a['type'] == 'Reptile':
                    self.animals.append(Reptile(a['name'], a['age'], False))
            print(f"Информация о зоопарке загружена из файла {filename}.")
        except FileNotFoundError:
            print(f"Файл {filename} не найден.")


# Классы сотрудников
class ZooKeeper:
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal):
        return f"Сотрудник {self.name} кормит животное {animal.name}."


class Veterinarian:
    def __init__(self, name):
        self.name = name

    def heal_animal(self, animal):
        return f"Ветеринар {self.name} лечит животное {animal.name}."


# Пример использования
if __name__ == "__main__":
    # Создаем зоопарк
    zoo = Zoo("Городской зоопарк")

    # Добавляем животных
    animal1 = Bird("Петя", 2, 1.2)
    animal2 = Mammal("Лев", 5, "желтый")
    animal3 = Reptile("Змей", 3, True)

    zoo.add_animal(animal1)
    zoo.add_animal(animal2)
    zoo.add_animal(animal3)

    # Добавляем сотрудников
    zookeeper = ZooKeeper("Анна")
    veterinarian = Veterinarian("Иван")

    zoo.add_staff(zookeeper)
    zoo.add_staff(veterinarian)

    # Демонстрация полиморфизма
    animals = [animal1, animal2, animal3]
    animal_sound(animals)

    # Сотрудники выполняют свои задачи
    print(zookeeper.feed_animal(animal1))
    print(veterinarian.heal_animal(animal2))

    # Сохранение и загрузка информации о зоопарке
    zoo.save_zoo("zoo_data.json")
    zoo.load_zoo("zoo_data.json")
