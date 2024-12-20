from random import choice
from enum import Enum

from main.colors import style, Colors

HELPER = '''Choices:
    [r]ock
    [p]aper
    [s]cissors
    [q]uit to exit the game'''


class Choices(Enum):
    r = 1, "ROCK"
    p = 3, "PAPER"
    s = 2, "SCISSORS"
    q = 99, "QUIT"


class Player:
    def __init__(self, name: str):
        self.score = 0
        self.name = name
        self.available_choices = Choices._member_names_

    def choose(self) -> str:
        while True:
            player_input = input(f"{self.name}, take your pick: ")[:1].lower()
            if player_input in self.available_choices:
                return player_input
            print(style("INVALID: please enter one of the available options:", Colors.WARNING))
            print(HELPER)


class Computer:
    def __init__(self):
        self.score = 0
        self.available_choices = [_.name for _ in Choices if _ != Choices.q]

    def choose(self) -> str:
        return choice(self.available_choices)


class Game:
    def __init__(self):
        self.player_name = input("Enter your name: ").title()
        self.round = 0
        self.player = Player(self.player_name)
        self.computer = Computer()

    def determine_and_display_winner(self, player_input: str, computer_input: str) -> (str, Player | Computer):
        dif = Choices[player_input].value[0] - Choices[computer_input].value[0]
        if dif in (-1, 2):
            return style(f"{self.player_name} wins", Colors.WIN), self.player
        elif dif in (-2, 1):
            return style("Computer wins.", Colors.LOSS), self.computer
        elif dif == 0:
            return style("Draw.", Colors.DRAW), None

    def update_scores(self, winner: Player | Computer):
        if winner == self.player:
            self.player.score += 1
        elif winner == self.computer:
            self.computer.score += 1

    def display_scores(self):
        print(style(f"Scores: {self.player_name} {self.player.score} | Computer {self.computer.score}\n", Colors.INFO))

    def play(self):
        print(HELPER)
        while True:
            self.round += 1
            print(f"------ Round {self.round} ------")
            player_input = self.player.choose()
            if player_input == Choices.q.name:
                print("Thanks for playing!")
                break
            computer_input = self.computer.choose()
            print(f"Computer pick: {Choices[computer_input].value[1]}")
            winner = self.determine_and_display_winner(player_input, computer_input)
            self.update_scores(winner[1])
            print(winner[0])
            self.display_scores()


if __name__ == "__main__":
    game = Game()
    game.play()
