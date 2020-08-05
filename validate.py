import tkinter as tk


def clear_board(board):
    for i in range(9):
        for j in range(9):
            # if board.cells[(i,j)].cget("state")=="normal":
            board.cells[(i, j)].delete(0, tk.END)


def validate_board(board):
    #check rows
    for i in range(9):
        temp = []
        for j in range(9):
            if board.cells[(i, j)].cget("state") == "disabled":
                temp.append(board.cells[(i, j)].get())
        for k in range(9):
            if board.cells[(i, k)].cget("state") == "normal":
                if board.cells[(i, k)].get() not in temp:
                    temp.append(board.cells[(i, k)].get())
                else:
                    if board.cells[(i, k)].get() != '':
                        board.cells[(i, k)].config(bg="red")

    #check columns
    for i in range(9):
        temp = []
        for j in range(9):
            if board.cells[(j, i)].cget("state") == "disabled":
                temp.append(board.cells[(j, i)].get())
        for k in range(9):
            if board.cells[(k, i)].get() not in temp:
                temp.append(board.cells[(k, i)].get())
            else:
                if board.cells[(k, i)].get() != '':
                    board.cells[(k, i)].config(bg="red")

    #check cube 'cells'
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            temp = []
            for x in range(i, i+3):
                for k in range(j, j+3):
                    if board.cells[(x, k)].cget("state") == "disabled":
                        temp.append(board.cells[(x, k)].get())
            for x in range(i, i+3):
                for y in range(j, j+3):
                    if board.cells[(x, y)].cget("state") == "normal":
                        if board.cells[(x, y)].get() not in temp:
                            temp.append(board.cells[(x, y)].get())
                        else:
                            if board.cells[(x, y)].get() != '':
                                board.cells[(x, y)].config(bg="red")
