from game_board import Board


class Sudoku:
    def __init__(self):
        self.game = Board()

    def init_game(self):
        self.game.draw_board()
        self.game.load_puzzle()
        self.game.window.mainloop()


sudoku_game = Sudoku()
sudoku_game.init_game()







