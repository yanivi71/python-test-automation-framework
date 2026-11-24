import pytest

from exercises.final_functions import (
    find_strings,
    longest_string,
    reverse_decimal,
    reverse_number,
    shuffled_words,
)


@pytest.mark.parametrize("number, expected", [
    (12345, "54321"),
    (100, "001"),
    (7, "7"),
])
def test_reverse_number(number, expected):
    assert reverse_number(number) == expected


def test_reverse_decimal():
    assert reverse_decimal(12.34) == "34.12"

def test_longest_string():
    assert longest_string(["apple", "banana", "cherry"]) == "banana"

@pytest.mark.parametrize("search, expected", [
    ("an", ["banana"]),
    pytest.param("e", ["apple", "cherry", "date"], id="matches_three"),
    ("x", []),
])
def test_find_strings(search, expected):
    strings = ["apple", "banana", "cherry", "date"]
    assert find_strings(strings, search) == expected

def test_shuffled_words():
    songwords = "Twinkle twinkle little star"
    result = shuffled_words(songwords)
    assert sorted(result) == sorted(songwords.split())  

def test_shuffled_words_order_varies():
    songwords = "one two three four five"

    orders = set()
    for _ in range(20):
        orders.add(tuple(shuffled_words(songwords)))

    assert len(orders) > 1