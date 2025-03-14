import tkinter as tk
from boards import Board, GameOver
from tkinter import messagebox


class TicTacToeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.board = Board.new()
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_widgets()

    def create_widgets(self):
        for row in range(3):
            for col in range(3):
                button = tk.Button(
                    self.root,
                    width=5,
                    height=2,
                    command=lambda r=row, c=col: self.play_turn(r, c),
                )
                button.grid(row=row, column=col, padx=2, pady=2)
                self.buttons[row][col] = button

    def play_turn(self, row, col):
        try:
            if self.board.position[row][col] != " ":
                return

            self.board.play_turn("X", row, col)
            self.update_board()

            ai_move = self.board.best_move()
            if ai_move:
                self.board.play_turn("O", *ai_move)
                self.update_board()

        except GameOver as e:
            self.update_board()
            messagebox.showinfo("Game Over", e.message)
            self.reset_game()

    def reset_game(self):
        self.board = Board.new()
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text="")

    def update_board(self):
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text=self.board.position[row][col])


def main():
    root = tk.Tk()
    app = TicTacToeApp(root)
    root.mainloop()
    # C'est un très bon début (injection de tk.Tk() en paramètre de l'app)
    # Pour aller plus loin, on aime bien séparer complètement la partie "vue" de la partie logique.
    # C'est surtout
    # self.buttons = [[None for _ in range(3)] for _ in range(3)]
    # self.create_widgets()
    # qui me fait dire ca : ici vous avez choisi une classe TicTacToeApp composée d'un Board et d'une vue tk.Tk()
    # Typiquement ici si on fait un Board de 4*4 au lieu de 3*3 il faudrait tout changer.
    # On peut par exemple imaginer une classe Graphics qui hérite de tk.Tk et c'est elle qui serait chargée
    # de create_widgets en fonction du Board.
    # La classe TicTacToeApp aurait toujours lieu d'être, simplement cela ressemblerait à quelque chose comme
    # class TicTacToeApp:
    #   def __init__(self, graphic_class):
    #       self.board = Board.new()
    #       self.graphic = graphic_class(board)
    #       self.graphic.create_widgets()
    #
    # et dans la class Graphic quelque chose comme
    # def create_widgets(self):
    #   for row in range(self.board.height):
    #       for col in range(self.board.width):
    #           ...
    #
    # D'autres implémentations seraient possible,
    # l'important est que cela soit logique, adapté au problème
    # et simple à maintenir en cas de modifications


if __name__ == "__main__":
    main()
