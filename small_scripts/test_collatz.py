import pytest

from collatz import collatz

def test_collatz_for_integer():
    assert collatz(2) == 1
    assert collatz(3) == 10
    assert collatz(-1) == -8
    assert collatz(-2) == -1


def test_collatz_for_string():
    assert collatz("grg") == TypeError
