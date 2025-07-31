import pytest

from game_ans import Game


#@pytest.mark.skip
def test_모두0점획득():
    game = Game()
    for i in range(20):
        game.roll(0)

    assert 0 == game.score()


# @pytest.mark.skip
def test_각1점씩획득():
    game = Game()
    for i in range(20):
        game.roll(1)

    assert 20 == game.score()


#@pytest.mark.skip
def test_스페어():
    game = Game()
    game.roll(5)
    game.roll(5)  # spare
    game.roll(3)
    for i in range(3, 20):
        game.roll(0)

    assert 16 == game.score()


#@pytest.mark.skip
def test_스트라이크():
    game = Game()
    for i in range(12):
        game.roll(10)

    assert 300 == game.score()


#@pytest.mark.skip
def test_샘플게임():
    game = Game()
    game.roll(1)
    game.roll(4)
    game.roll(4)
    game.roll(5)
    game.roll(6)
    game.roll(4)
    game.roll(5)
    game.roll(5)
    game.roll(10)
    game.roll(0)
    game.roll(1)
    game.roll(7)
    game.roll(3)
    game.roll(6)
    game.roll(4)
    game.roll(10)
    game.roll(2)
    game.roll(8)
    game.roll(6)

    assert 133 == game.score()
