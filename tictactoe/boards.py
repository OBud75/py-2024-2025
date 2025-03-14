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
    # Pas vraiment utile du coup.

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

    def is_full(self) -> bool:
        return not any(cell == " " for row in self.position for cell in row)

    def make_move(self, pos_y: int, pos_x: int, player: str) -> "Board":
        new_board = Board([row[:] for row in self.position])
        new_board.position[pos_y][pos_x] = player
        return new_board

    def get_empty_cells(self) -> list[tuple[int, int]]:
        return self.empty_cells
        # empty_cells est publique (par convention on préfixe d'un _ les variables privées)
        # Dans tous les cas ici empty_cells est une propriété, on ne peut donc pas faire
        # board.empty_cells = toto et c'est surtout ca qui compte dans l'aspect public/privé.

    def play_turn(self, player: str, pos_y: int, pos_x: int):
        if self.position[pos_y][pos_x] != " ":
            raise ValueError("Cell is already taken")
        self.position[pos_y][pos_x] = player

        if self.is_won(player):
            raise GameOver(f"{player} won")
            # Gardez raise pour les erreurs ici on peut quit(f"{player} won") par exemple.
            # Créer vos propres exceptions adaptées au programmes est apprécié.
            # Typiquement une exception CoordinatesOutOfBoard, CellDoesNotExists
            # ou meme CellAlreadyTaken aurait peut être été plus approprié.
        if not self.empty_cells:
            raise GameOver("Draw")

    def minimax(self, board, depth: int, is_maximizing: bool) -> int:
        if board.is_won("X"):
            return -10 + depth
        if board.is_won("O"):
            return 10 - depth
        if board.is_full():
            return 0

        if is_maximizing:
            best_score = -float("inf")
            for row, col in board.get_empty_cells():
                result = self.minimax(board.make_move(row, col, "O"), depth + 1, False)
                best_score = max(best_score, result)
            return best_score
        else:
            best_score = float("inf")
            for row, col in board.get_empty_cells():
                result = self.minimax(board.make_move(row, col, "X"), depth + 1, True)
                best_score = min(best_score, result)
            return best_score

    def best_move(self) -> tuple[int, int]:
        best_score = -float("inf")
        move = None
        for row, col in self.get_empty_cells():
            test_board = self.make_move(row, col, "O")
            score = self.minimax(test_board, 0, False)
            if score > best_score:
                best_score, move = score, (row, col)
        return move
