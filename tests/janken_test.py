from lib.janken import Rock, Paper, Scissor


def test_eq():
    assert Rock() == Rock()
    assert Rock() != Paper()
    assert Rock() != Scissor()


def test_gt():
    assert Rock() > Scissor()
    assert Paper() > Rock()
    assert Scissor() > Paper()


def test_lt():
    assert Rock() < Paper()
    assert Scissor() < Rock()
    assert Paper() < Scissor()
