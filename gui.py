import tkinter as tk
from tkinter import font, PhotoImage
from PIL import ImageTk, Image
from globals import *
from location import *

cells = [0] * 9
stacks = [0] * 6



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
                            command=lambda: buildBoard(prevWindow,HumanButton,
                                              AiButton,selectQuestion),
                            width=10, height=5,
                            font=helv16,
                            activeforeground="red", bg="light blue")

    AiButton = tk.Button(prevWindow, text="AI vs AI",
                         command=lambda: buildBoard(prevWindow,HumanButton,
                                              AiButton,selectQuestion),
                         width=10, height=5,
                         font=helv16,
                         activeforeground="red", bg="light blue")
    HumanButton.place(x=60, y=100)
    AiButton.place(x=300, y=100)


def buildBoard(prevWindow, button1, button2, question):
    l1 = Location(0,2)
    l2 = Location(1,2)
    l3 = Location(2,2)

    question.destroy()
    button1.destroy()
    button2.destroy()
    # global red_large_square, blue_large_square
    red_large_square =  ImageTk.PhotoImage(Image.open(
        'Images/Large_Red_Square.png').resize((70, 70)))

    blue_large_square = ImageTk.PhotoImage(Image.open(
        'Images/Large_Blue_Square.png').resize((70, 70)))
    white_square = ImageTk.PhotoImage(Image.open(
        'Images/whiteSquare.png').resize((110, 110)))

    # prevWindow.destroy()
    # gameScreen = tk.Tk()
    prevWindow.geometry("400x550")
    for i in range(9):
        if i < 2:
            yCor = 100
        if 3 <= i < 6:
            yCor = 220
        if i >= 6:
            yCor = 340
        #TODO: set command to the right one with cell or piecesStack
        cells[i] = tk.Button(prevWindow,highlightcolor="black",
                             bg="white",image=white_square,
                             command=lambda:changeCell(Location(2,1),SMALL,
                                                       RED))
        cells[i].image = white_square
        cells[i].place(x=25 + 115 * (i % 3), y=yCor)

    for i in range(3):
        #TODO: change the command to move to piecesStack.pop
        stacks[i] = tk.Button(prevWindow,
                                image=blue_large_square, command=lambda:
            removeFromStack(i, "Small"))
        stacks[i].image = blue_large_square
        stacks[i].place(x=70 + i * 90, y=15)

    for i in range(3):
        stacks[i+3] = tk.Button(prevWindow,
                               image=red_large_square)
        stacks[i+3].image = red_large_square
        stacks[i+3].place(x=70 + i * 90, y=470)


def removeFromStack(stackIndex: int, newSize: int) -> None:
    red_large_square =  ImageTk.PhotoImage(Image.open(
        'Images/Large_Red_Square.png').resize((70, 70)))

    blue_large_square = ImageTk.PhotoImage(Image.open(
        'Images/Large_Blue_Square.png').resize((70, 70)))
    red_medium_square =  ImageTk.PhotoImage(Image.open(
        'Images/Medium_Red_Square.png').resize((70, 70)))

    blue_medium_square = ImageTk.PhotoImage(Image.open(
        'Images/Medium_Blue_Square.png').resize((70, 70)))
    red_small_square =  ImageTk.PhotoImage(Image.open(
        'Images/Small_Red_Square (5).png').resize((70, 70)))

    blue_small_square = ImageTk.PhotoImage(Image.open(
        'Images/Small_Blue_Square.png').resize((70, 70)))

    if newSize == LARGE:
        if stackIndex < 3:
            stacks[stackIndex].config(image = blue_large_square)
            stacks[stackIndex].image = blue_large_square
        else:
            stacks[stackIndex].config(image = red_large_square)
            stacks[stackIndex].image = red_large_square
    elif newSize == MEDIUM:
        if stackIndex < 3:
            stacks[stackIndex].config(image = blue_medium_square)
            stacks[stackIndex].image = blue_medium_square
        else:
            stacks[stackIndex].config(image = red_medium_square)
            stacks[stackIndex].image = red_medium_square
    elif newSize == SMALL:
        if stackIndex < 3:
            stacks[stackIndex].config(image = blue_small_square)
            stacks[stackIndex].image = blue_small_square
        else:
            stacks[stackIndex].config(image = red_small_square)
            stacks[stackIndex].image = red_small_square

def changeCell(cellIndex: Location, newSize: int, color: str):
    red_large_square =  ImageTk.PhotoImage(Image.open(
        'Images/Large_Red_Square.png').resize((110, 110)))

    blue_large_square = ImageTk.PhotoImage(Image.open(
        'Images/Large_Blue_Square.png').resize((110, 110)))
    red_medium_square =  ImageTk.PhotoImage(Image.open(
        'Images/Medium_Red_Square.png').resize((110, 110)))

    blue_medium_square = ImageTk.PhotoImage(Image.open(
        'Images/Medium_Blue_Square.png').resize((110, 110)))
    red_small_square =  ImageTk.PhotoImage(Image.open(
        'Images/Small_Red_Square (5).png').resize((110, 110)))

    blue_small_square = ImageTk.PhotoImage(Image.open(
        'Images/Small_Blue_Square.png').resize((110, 110)))

    index = cellIndex.row*3 + cellIndex.col
    if newSize == LARGE:
        if color == BLUE:
            cells[index].config(image = blue_large_square)
            cells[index].image = blue_large_square
        else:
            cells[index].config(image = red_large_square)
            cells[index].image = red_large_square
    elif newSize == MEDIUM:
        if color == BLUE:
            cells[index].config(image = blue_medium_square)
            cells[index].image = blue_medium_square
        else:
            cells[index].config(image = red_medium_square)
            cells[index].image = red_medium_square
    if newSize == SMALL:
        if color == BLUE:
            cells[index].config(image = blue_small_square)
            cells[index].image = blue_small_square
        else:
            cells[index].config(image = red_small_square)
            cells[index].image = red_small_square


def markWinner(l1: Location, l2: Location, l3: Location):
    # cell1bg = cells[l1.row * 2 + l1.col].cget("background")
    # cell2bg = cells[l2.row * 2 + l2.col].cget("background")
    # cell3bg = cells[l3.row * 2 + l3.col].cget("background")

    #TODO: how to make this flash?

    cells[l1.row*3 + l1.col].config(bg="green")
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







if __name__ == '__main__':
    # red_large_square = Image.open('Images/red_square.png').resize((70, 70), Image.ANTIALIAS)
    #
    # blue_large_square = Image.open('Images/blue_square.png').resize((70, 70), Image.ANTIALIAS)
    # red_medium_square = ImageTk.PhotoImage(
    #     Image.open('Images/red_square.png').resize((50, 50), Image.ANTIALIAS))
    # red_small_square = ImageTk.PhotoImage(
    #     Image.open('Images/red_square.png').resize((30, 30), Image.ANTIALIAS))

    # main()
    pass
