from functools import partial
from tkinter import font
from PIL import ImageTk, Image
from action import Action
from Board import Board
from gobblet import manual_move
from piece import *

cells = [0] * 9
stacks = {color: [0]*STACKS_NUM for color in COLORS}


def build_main_window():
    helloScreen = tk.Tk()
    helv16 = font.Font(root=helloScreen, family="Helvetica", size=16,
                       weight="bold")
    helloScreen.geometry("800x400")
    imgFrame = tk.Frame(helloScreen, width=800, height=500)
    imgFrame.place(anchor="center")
    imgFrame.pack()
    startingImg = ImageTk.PhotoImage(Image.open("gobbletgobblers.jpg"))

    imgLabel = tk.Label(imgFrame, image=startingImg)
    imgLabel.pack()
    # TODO: change command to a function allowing to select modes (human vs
    # AI, AI vs AI)
    startButton = tk.Button(helloScreen, text="Start",
                            command=lambda: setGameModes(helloScreen, startButton, imgFrame),

                            font=helv16,
                            activeforeground="red", bg="light green")
    startButton.place(x=650, y=300)

    helloScreen.mainloop()


def setGameModes(prevWindow, button, image):
    # prevWindow.destroy()
    button.destroy()
    image.destroy()
    prevWindow.geometry("500x300")
    helv32 = font.Font(root=prevWindow, family="Helvetica", size=32,
                       weight="bold")
    helv16 = font.Font(root=prevWindow, family="Helvetica", size=16,
                       weight="bold")
    selectQuestion = tk.Label(text="Choose a Game Mode:", fg="black",
                              font=helv32)
    selectQuestion.pack(anchor="center")

    # TODO: set functions that set up players for each button
    HumanButton = tk.Button(prevWindow, text="Human vs AI",
                            command=lambda: buildBoard(prevWindow, HumanButton,
                                                       AiButton, selectQuestion),
                            width=10, height=5,
                            font=helv16,
                            activeforeground="red", bg="light blue")

    AiButton = tk.Button(prevWindow, text="AI vs AI",
                         command=lambda: buildBoard(prevWindow, HumanButton,
                                                    AiButton, selectQuestion),
                         width=10, height=5,
                         font=helv16,
                         activeforeground="red", bg="light blue")
    HumanButton.place(x=60, y=100)
    AiButton.place(x=300, y=100)


def buildBoard(prevWindow, button1, button2, question):

    question.destroy()
    button1.destroy()
    button2.destroy()
    red_large_square = ImageTk.PhotoImage(Image.open(
        'Images/Large_Red_Square.png').resize((70, 70)))

    blue_large_square = ImageTk.PhotoImage(Image.open(
        'Images/Large_Blue_Square.png').resize((70, 70)))
    white_square = ImageTk.PhotoImage(Image.open(
        'Images/whiteSquare.png').resize((110, 110)))

    prevWindow.geometry("400x550")
    for i in range(9):
        if i < 2:
            yCor = 100
        if 3 <= i < 6:
            yCor = 220
        if i >= 6:
            yCor = 340
        cells[i] = tk.Button(prevWindow, highlightcolor="black", bg="white", image=white_square,
                             command=partial(manual_move, False, i))
        cells[i].image = white_square
        cells[i].place(x=25 + 115 * (i % 3), y=yCor)

    for i in range(STACKS_NUM):
        stacks[BLUE][i] = tk.Button(prevWindow, image=blue_large_square, command=partial(manual_move, True, i, BLUE))
        stacks[BLUE][i].image = blue_large_square
        stacks[BLUE][i] .place(x=110 + i * 90, y=15)

    for i in range(STACKS_NUM):
        stacks[RED][i] = tk.Button(prevWindow,
                                           image=red_large_square,
                                           command=partial(manual_move, True, i, RED))
        stacks[RED][i].image = red_large_square
        stacks[RED][i].place(x=110 + i * 90, y=470)


def removeFromStack(color: str, stackIndex: int, newSize: int) -> None:
    red_large_square = ImageTk.PhotoImage(Image.open(
        'Images/Large_Red_Square.png').resize((70, 70)))

    blue_large_square = ImageTk.PhotoImage(Image.open(
        'Images/Large_Blue_Square.png').resize((70, 70)))
    red_medium_square = ImageTk.PhotoImage(Image.open(
        'Images/Medium_Red_Square.png').resize((70, 70)))

    blue_medium_square = ImageTk.PhotoImage(Image.open(
        'Images/Medium_Blue_Square.png').resize((70, 70)))
    red_small_square = ImageTk.PhotoImage(Image.open(
        'Images/Small_Red_Square (5).png').resize((70, 70)))

    blue_small_square = ImageTk.PhotoImage(Image.open(
        'Images/Small_Blue_Square.png').resize((70, 70)))
    white_square = ImageTk.PhotoImage(Image.open(
        'Images/whiteSquare.png').resize((70, 70)))
    if newSize == LARGE:
        if color == BLUE:
            stacks[BLUE][stackIndex].config(image=blue_large_square)
            stacks[BLUE][stackIndex].image = blue_large_square
        else:
            stacks[RED][stackIndex].config(image=red_large_square)
            stacks[RED][stackIndex].image = red_large_square
    elif newSize == MEDIUM:
        if color == BLUE:
            stacks[BLUE][stackIndex].config(image=blue_medium_square)
            stacks[BLUE][stackIndex].image = blue_medium_square
        else:
            stacks[RED][stackIndex].config(image=red_medium_square)
            stacks[RED][stackIndex].image = red_medium_square
    elif newSize == SMALL:
        if color == BLUE:
            stacks[BLUE][stackIndex].config(image=blue_small_square)
            stacks[BLUE][stackIndex].image = blue_small_square
        else:
            stacks[RED][stackIndex].config(image=red_small_square)
            stacks[RED][stackIndex].image = red_small_square
    elif newSize == NONE:
        if color == BLUE:
            stacks[BLUE][stackIndex].config(image=white_square)
            stacks[BLUE][stackIndex].image = white_square
        else:
            stacks[RED][stackIndex].config(image=white_square)
            stacks[RED][stackIndex].image = white_square



def changeCell(cellIndex: Location, newSize: int, color: str) -> None:
    red_large_square = ImageTk.PhotoImage(Image.open(
        'Images/Large_Red_Square.png').resize((110, 110)))

    blue_large_square = ImageTk.PhotoImage(Image.open(
        'Images/Large_Blue_Square.png').resize((110, 110)))
    red_medium_square = ImageTk.PhotoImage(Image.open(
        'Images/Medium_Red_Square.png').resize((110, 110)))

    blue_medium_square = ImageTk.PhotoImage(Image.open(
        'Images/Medium_Blue_Square.png').resize((110, 110)))
    red_small_square = ImageTk.PhotoImage(Image.open(
        'Images/Small_Red_Square (5).png').resize((110, 110)))

    blue_small_square = ImageTk.PhotoImage(Image.open(
        'Images/Small_Blue_Square.png').resize((110, 110)))
    white_square = ImageTk.PhotoImage(Image.open(
        'Images/whiteSquare.png').resize((110, 110)))

    index = cellIndex.row * 3 + cellIndex.col
    if newSize == LARGE:
        if color == BLUE:
            cells[index].config(image=blue_large_square)
            cells[index].image = blue_large_square
        else:
            cells[index].config(image=red_large_square)
            cells[index].image = red_large_square
    elif newSize == MEDIUM:
        if color == BLUE:
            cells[index].config(image=blue_medium_square)
            cells[index].image = blue_medium_square
        else:
            cells[index].config(image=red_medium_square)
            cells[index].image = red_medium_square
    elif newSize == SMALL:
        if color == BLUE:
            cells[index].config(image=blue_small_square)
            cells[index].image = blue_small_square
        else:
            cells[index].config(image=red_small_square)
            cells[index].image = red_small_square
    elif newSize == NONE:
        cells[index].config(image=white_square)
        cells[index].image = white_square


def apply_action(action: Action, board: Board):
    source = action.src

    if source.is_outside():
        stackIndex = action.piece.stack_index
        newSize = None
        if action.piece.size == LARGE:
            newSize = MEDIUM
        elif action.piece.size == MEDIUM:
            newSize = SMALL
        else:
            newSize = NONE
        # manipulate stack gui
        removeFromStack(action.piece.color, stackIndex, newSize)

    else:  # inside
        srcCellIndex = source
        srcNewSize = None
        newColor = None
        if board.get_cell(source).stack.get_size() > 1:
            srcNewSize = board.get_cell(source).stack.pieces[-2].size
            newColor = board.get_cell(source).stack.pieces[-2].color
        else:
            srcNewSize = NONE
        changeCell(srcCellIndex, srcNewSize, newColor)

    destination = action.dest
    destCellIndex = destination

    destNewSize = action.piece.size
    newColor = action.piece.color

    changeCell(destCellIndex, destNewSize, newColor)


def markWinner(l1: Location, l2: Location, l3: Location):
    # cell1bg = cells[l1.row * 2 + l1.col].cget("background")
    # cell2bg = cells[l2.row * 2 + l2.col].cget("background")
    # cell3bg = cells[l3.row * 2 + l3.col].cget("background")

    # TODO: how to make this flash?
    #TODO: how to increase border size?

    cells[l1.row * 3 + l1.col].config(bg="green")
    # cells[l1.row*2+l1.col].after(200, lambda: cells[
    #     l1.row*2+l1.col].config(
    #     background=cell1bg))
    cells[l2.row * 3 + l2.col].config(bg="green")
    # cells[l2.row*2+l2.col].after(200, lambda: cells[
    #     l2.row*2+l2.col].config(
    #     background=cell2bg))
    cells[l3.row * 3 + l3.col].config(bg="green")
    # cells[l3.row*2+l3.col].after(200, lambda: cells[
    #     l3.row*2+l3.col].config(
    #     background=cell3bg))
