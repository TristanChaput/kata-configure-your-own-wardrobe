from app.size import Size


class Wardrobe:
    WALL_SIZE = 250
    __combinations: list[list[Size]]

    def __init__(self):
        self.__combinations = []
        self.configure_wardrobe()

    def create_combination(self):
        return [Size.FIFTY, Size.FIFTY, Size.FIFTY, Size.FIFTY, Size.FIFTY]

    def add_combination(self, combination: list[Size]):
        if not self.check_is_exist(combination):
            self.__combinations.append(combination)
            return True
        return False

    def configure_wardrobe(self):
        self.add_combination(self.create_combination())

    def list_of_combinations(self):
        return self.__combinations

    def check_is_exist(self, new_combination: list[Size]):
        for valid_combination in self.__combinations:
            valid_combination.sort()
            new_combination.sort()
            if new_combination == valid_combination:
                return True

        return False
