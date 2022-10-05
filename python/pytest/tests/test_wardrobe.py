import pytest
from app.wardrobe import Wardrobe


class TestWardrobe:

    def test_is_a_valid_combination(self):
        wardrobe = Wardrobe()
        assert sum(wardrobe.list_of_combinations()[0]) == 250
