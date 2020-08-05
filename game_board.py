from validate import *


class Board:
    def __init__(self):
        self.window = tk.Tk()
        self.window.config(bg="dim gray")
        self.cells = {}
        self.draw_board()
        self.load_puzzle()
        self.reset_btn = tk.Button(text="Reset", command=lambda: clear_board(self), width=3, height=1, fg="tan4",
                                   bg="misty rose", master=self.window)
        self.reset_btn.grid(row=9, column=0, columnspan=3)
        self.check_btn = tk.Button(text="Check", command=lambda: validate_board(self), width=3, height=1, fg="tan4",
                                   bg="misty rose", master=self.window)
        self.check_btn.grid(row=9, column=6, columnspan=3)

    def draw_board(self):
        for i in range(9):
            for j in range(9):
                cell = tk.Entry(
                    master=self.window,
                    relief=tk.SUNKEN,
                    width=4
                )
                cell.grid(row=i, column=j, ipady=4)
                if i in [2, 5]:
                    cell.grid(pady=(0, 4))

                if j in [2, 5]:
                    cell.grid(padx=(0, 4))

                self.cells[(i, j)] = cell

    def load_puzzle(self):
        puzzle = [
            ['', '', '', '', '2', '9', '', '1', '6'],
            ['', '', '', '', '', '', '3', '', '2'],
            ['5', '3', '', '', '1', '', '', '', ''],
            ['8', '', '', '', '6', '3', '4', '5', '9'],
            ['', '', '', '8', '', '7', '', '', ''],
            ['3', '9', '1', '2', '4', '', '', '', '8'],
            ['', '', '', '', '7', '', '', '3', '5'],
            ['9', '', '8', '', '', '', '', '', ''],
            ['4', '7', '', '9', '5', '', '', '', '']
        ]
        for i in range(9):
            for j in range(9):
                if puzzle[i][j] != '':
                    self.cells[(i, j)].insert(0, f"{puzzle[i][j]}")
                    self.cells[(i, j)].config(state='disabled')
                else:
                    self.cells[(i, j)].bind("<BackSpace>", lambda event, c=self.cells[(i, j)]: c.configure(bg="white"))
