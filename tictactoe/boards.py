import math


class GameOver(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


class Board:
    def __init__(self, position=None) -> None:
        self.position = position or [[" "] * 3 for _ in range(3)]

    def __str__(self) -> str:
        return "\n".join("|" + "|".join(row) + "|" for row in self.position)

    @classmethod
    def new(cls):
        return cls()

    @property
    def empty_cells(self) -> list[tuple[int, int]]:
        return [
            (y, x)
            for y, row in enumerate(self.position)
            for x, cell in enumerate(row)
            if cell == " "
        ]

    def is_won(self, player: str) -> bool:
        lines = (
            self.position
            + [list(col) for col in zip(*self.position)]
            + [
                [self.position[i][i] for i in range(3)],
                [self.position[i][2 - i] for i in range(3)],
            ]
        )
        return any(all(cell == player for cell in line) for line in lines)

    def play_turn(self, player: str, pos_y: int, pos_x: int):
        if self.position[pos_y][pos_x] != " ":
            raise ValueError("Cell is already taken")
        self.position[pos_y][pos_x] = player

        if self.is_won(player):
            raise GameOver(f"{player} won")
        if not self.empty_cells:
            raise GameOver("Draw")

    def minimax(self, is_maximizing: bool) -> int:
        if self.is_won("O"):
            return 1
        if self.is_won("X"):
            return -1
        if not self.empty_cells:
            return 0

        best_score = -math.inf if is_maximizing else math.inf
        for y, x in self.empty_cells:
            self.position[y][x] = "O" if is_maximizing else "X"
            score = self.minimax(not is_maximizing)
            self.position[y][x] = " "
            best_score = (
                max(score, best_score) if is_maximizing else min(score, best_score)
            )
        return best_score

    def best_move(self) -> tuple[int, int]:
        best_score = -math.inf
        move = None
        for y, x in self.empty_cells:
            self.position[y][x] = "O"
            score = self.minimax(False)
            self.position[y][x] = " "
            if score > best_score:
                best_score, move = score, (y, x)
        return move
