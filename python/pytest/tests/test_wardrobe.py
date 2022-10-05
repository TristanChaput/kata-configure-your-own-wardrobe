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

    @pytest.mark.parametrize("combination, exist",
                             [([Size.FIFTY, Size.FIFTY, Size.FIFTY, Size.FIFTY, Size.FIFTY], True)])
    def test_combination_should_be_already_exist(self, combination, exist):
        wardrobe = Wardrobe()
        assert wardrobe.check_is_exist(combination) is exist

    def test_can_add_number_to_combination(self):
        wardrobe = Wardrobe()
        expected_available_numbers = [Size.FIFTY, Size.SEVENTY_FIVE, Size.HUNDRED, Size.HUNDRED_TWENTY]
        assert wardrobe.can_add_number([Size.FIFTY]) == expected_available_numbers
