"""
Yahtzee Scorer — Starter Code
==============================

Running the tests
-----------------
  pytest test_yahtzee.py -v   # run all tests with verbose output
"""

from collections import Counter

# ---------------------------------------------------------------------------
# Helper — feel free to add your own helpers below this line
# ---------------------------------------------------------------------------

def _counts(dice):
    """Return a Counter of how many times each face appears in *dice*."""
    return Counter(dice)


# ---------------------------------------------------------------------------
# Part 1–7  →  score_lower
# ---------------------------------------------------------------------------

def score_lower(dice):
    """Score *dice* against every lower-section Yahtzee category.

    Parameters
    ----------
    dice : list[int]
        A list of exactly 5 integers, each in the range 1–6.

    Returns
    -------
    dict
        A dictionary mapping every lower-section category name to its score.
        Categories that do not match the dice are scored as 0.

    Examples
    --------
    >>> score_lower([2, 3, 4, 4, 4])
    {'Three of a kind': 17, 'Four of a kind': 0, 'Full house': 0,
     'Large straight': 0, 'Small straight': 0, 'Yahtzee': 0, 'Chance': 0}

    >>> score_lower([2, 2, 5, 5, 5])
    {'Three of a kind': 19, 'Four of a kind': 0, 'Full house': 25,
     'Large straight': 0, 'Small straight': 0, 'Yahtzee': 0, 'Chance': 0}
    """
    counts = _counts(dice)
    total = sum(dice)

    # ------------------------------------------------------------------
    # Part 1: Implement "Three of a kind"
    # ------------------------------------------------------------------
    three_of_a_kind = 0
    for count in counts.values():
        if count >= 3:
            three_of_a_kind = total

    # ------------------------------------------------------------------
    # Part 2: Implement "Four of a kind"
    # ------------------------------------------------------------------
    four_of_a_kind = 0
    for count in counts.values():
        if count >= 4:
            four_of_a_kind = total

    # ------------------------------------------------------------------
    # Part 3: Implement "Full house"
    # ------------------------------------------------------------------
    full_house = 0
    if 2 in counts.values() and 3 in counts.values():
        full_house = 25

    # ------------------------------------------------------------------
    # TODO Part 4: Implement "Large straight"
    # ------------------------------------------------------------------
    large_straight = 0   # replace with your implementation

    # ------------------------------------------------------------------
    # TODO Part 5: Implement "Small straight"
    # ------------------------------------------------------------------
    small_straight = 0   # replace with your implementation

    # ------------------------------------------------------------------
    # TODO Part 6: Implement "Yahtzee"
    yahtzee = 0          # replace with your implementation

    # ------------------------------------------------------------------
    # TODO Part 7: Implement "Chance"
    chance = 0           # replace with your implementation

    return {
        "Three of a kind": three_of_a_kind,
        "Four of a kind":  four_of_a_kind,
        "Full house":      full_house,
        "Large straight":  large_straight,
        "Small straight":  small_straight,
        "Yahtzee":         yahtzee,
        "Chance":          chance,
    }


# ---------------------------------------------------------------------------
# Part 8  →  total_score
# ---------------------------------------------------------------------------

def total_score(rounds):
    """Compute the total score over multiple rounds of Yahtzee.

    Parameters
    ----------
    rounds : list[list[int]]
        A list of dice configurations, each a list of 5 integers (1–6).

    Returns
    -------
    int
        The cumulative score across all rounds.

    Examples
    --------
    >>> total_score([[2, 3, 4, 4, 4], [6, 6, 6, 5, 5]])
    42
    """
    return 0  # replace with your implementation
