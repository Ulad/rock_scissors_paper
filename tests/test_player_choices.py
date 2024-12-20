from main.rock_scissors_paper import Computer


def test_computer_input():
    computer = Computer()
    i = computer.choose()
    assert i not in "q"
