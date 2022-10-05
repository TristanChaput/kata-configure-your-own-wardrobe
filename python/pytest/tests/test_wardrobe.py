import pytest

from app.size import Size
from app.wardrobe import Wardrobe


class TestWardrobe:

    def test_all_valid_combination(self):
        wardrobe = Wardrobe()
        valid = True
        for combination in wardrobe.list_of_combinations():
            if sum(combination) != Wardrobe.WALL_SIZE:
                valid = False
        if not valid:
            pytest.fail("Combinations are not valid", pytrace=True)

    def test_combination_should_be_already_exist(self):
        wardrobe = Wardrobe()
        assert wardrobe.add_combination([Size.FIFTY, Size.FIFTY, Size.FIFTY, Size.FIFTY, Size.FIFTY]) is False
