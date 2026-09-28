"""
test_yahtzee.py — Starter Tests
==========================================================
How to run
----------
  pytest test_yahtzee.py -v

TDD workflow reminder
---------------------
For EACH part (1–8):
  1. Write / extend the test(s) in this file.
  2. Commit:  git commit -m "<Category> - failing"
  3. Implement the corresponding logic in yahtzee.py.
  4. Re-run pytest — all tests must pass.
  5. Commit:  git commit -m "<Category> - passing"
"""

import pytest
from yahtzee import score_lower, total_score


# ===========================================================================
# Part 1 — Three of a kind (0.4 points)
# ===========================================================================

class TestThreeOfAKind:
    def test_three_of_a_kind_basic(self):
        result = score_lower([3, 3, 3, 2, 1])
        assert result["Three of a kind"] == 12

    def test_not_three_of_a_kind(self):
        result = score_lower([3, 3, 2, 2, 1])
        assert result["Three of a kind"] == 0

    def test_three_of_a_kind_with_extra(self):
        result = score_lower([4, 4, 4, 4, 2])
        assert result["Three of a kind"] == 18

# ===========================================================================
# Part 2 — Four of a kind (0.4 points)
# ===========================================================================

class TestFourOfAKind:
    def test_four_of_a_kind_basic(self):
        result = score_lower([5, 5, 5, 5, 2])
        assert result["Four of a kind"] == 22

    def test_not_four_of_a_kind(self):
        result = score_lower([5, 5, 5, 2, 2])
        assert result["Four of a kind"] == 0

    def test_four_of_a_kind_with_extra(self):
        result = score_lower([6, 6, 6, 6, 6])
        assert result["Four of a kind"] == 30
        

# ===========================================================================
# Part 3 — Full house (0.4 points)
# ===========================================================================

class TestFullHouse:
    def test_full_house_basic(self):
        result = score_lower([2, 2, 3, 3, 3])
        assert result["Full house"] == 25

    def test_not_full_house(self):
        result = score_lower([2, 2, 2, 3, 4])
        assert result["Full house"] == 0

    def test_full_house_edge_case(self):
        result = score_lower([4, 4, 4, 4, 4])
        assert result["Full house"] == 0


# ===========================================================================
# Part 4 — Large straight (0.4 points)
# ===========================================================================

class TestLargeStraight:
    def test_large_straight_basic(self):
        result = score_lower([2, 3, 4, 5, 6])
        assert result["Large straight"] == 40

    def test_large_straight_basic_2(self):
        result = score_lower([1, 2, 3, 4, 5])
        assert result["Large straight"] == 40

    def test_not_large_straight(self):
        result = score_lower([1, 2, 3, 4, 6])
        assert result["Large straight"] == 0

    def test_large_straight_unorganized(self):
        result = score_lower([3, 5, 4, 2, 6])
        assert result["Large straight"] == 40

# ===========================================================================
# Part 5 — Small straight (0.5 points)
# ===========================================================================

class TestSmallStraight:
    def test_small_straight_basic(self):
        result = score_lower([2, 3, 2, 5, 4])
        assert result["Small straight"] == 30

    def test_small_straight_basic_2(self):
        result = score_lower([2, 3, 3, 4, 5])
        assert result["Small straight"] == 30

    def test_not_small_straight(self):
        result = score_lower([1, 2, 3, 5, 6])
        assert result["Small straight"] == 0

    def test_small_straight_edge_case(self):
        result = score_lower([1, 2, 3, 4, 5])
        assert result["Small straight"] == 0

# ===========================================================================
# Part 6 — Yahtzee (0.4 points)
# ===========================================================================

class TestYahtzee:
    def test_yahtzee_basic(self):
        result = score_lower([6, 6, 6, 6, 6])
        assert result["Yahtzee"] == 50

    def test_yahtzee_basic_2(self):
        result = score_lower([1, 1, 1, 1, 1])
        assert result["Yahtzee"] == 50

    def test_not_yahtzee(self):
        result = score_lower([6, 6, 6, 6, 5])
        assert result["Yahtzee"] == 0

# ===========================================================================
# Part 7 — Chance (0.5 points)
# ===========================================================================

class TestChance:
    def test_chance_basic(self):
        result = score_lower([1, 1, 2, 2, 5])
        assert result["Chance"] == 11

    def test_chance_basic_2(self):
        result = score_lower([1, 1, 3, 5, 6])
        assert result["Chance"] == 16

    def test_not_chance(self):
        result = score_lower([3, 3, 3, 2, 1])
        assert result["Chance"] == 0

# ===========================================================================
# Part 8 — Complete score map + total_score (1.0 point)
# ===========================================================================

class TestCompleteScoreMap:
    def test_full_map_returned(self):
        """score_lower must return ALL categories, with zeros for non-matching ones."""


class TestTotalScore:
    def test_total_score_basic(self):
        """Write/extend test(s)"""