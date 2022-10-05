import pytest
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
