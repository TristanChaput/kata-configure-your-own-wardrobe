from app.size import Size


class Wardrobe:
    WALL_SIZE = 250
    __combinations: list[list[Size]]

    def __init__(self):
        self.__combinations = []

    def create_combination(self):
        return [Size.FIFTY, Size.FIFTY, Size.FIFTY, Size.FIFTY, Size.FIFTY]

    def add_combination(self, combination: list[Size]):
        self.__combinations.append(combination)

    def list_of_combinations(self):
        self.add_combination(self.create_combination())
        return self.__combinations