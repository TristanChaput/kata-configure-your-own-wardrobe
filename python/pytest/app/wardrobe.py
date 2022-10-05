class Wardrobe:
    SIZE = 250
    __combinations: list[list[int]]

    def __init__(self):
        self.__combinations = []

    def list_of_combinations(self):
        self.__combinations.insert(0, [50, 50, 50, 50, 50])
        return self.__combinations
