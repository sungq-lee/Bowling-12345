import pytest

from game import Game


def test_create_game():
    game = Game()
    assert game is not None