import pytest
from Test-Prioritization.prioritize_random import prioritize_random


def test_prioritize_random():
    Y = ["a", "b", "c", "d"]
    Y_ranked = prioritize_random(Y)
    assert len(Y) == len(Y_ranked)
    for y in Y:
        assert y in Y_ranked