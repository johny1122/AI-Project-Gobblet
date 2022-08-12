import tkinter as tk
from tkinter import font, PhotoImage
from PIL import ImageTk, Image
from globals import *

cells = [0] * 9
stacks = [0] * 6



def main():
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
                            command=lambda: humanVsAi(prevWindow,HumanButton,AiButton,selectQuestion),
                            width=10, height=5,
                            font=helv16,
                            activeforeground="red", bg="light blue")

    AiButton = tk.Button(prevWindow, text="AI vs AI",
                         command=prevWindow.destroy,
                         width=10, height=5,
                         font=helv16,
                         activeforeground="red", bg="light blue")
    HumanButton.place(x=60, y=100)
    AiButton.place(x=300, y=100)


def humanVsAi(prevWindow, button1, button2, question):
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
                             command=lambda:changeCell(4,
                                                                   "Medium",
                                                                   "Red"))
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


def removeFromStack(stackIndex: int, newSize: str) -> None:
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

    if newSize == "Large":
        if stackIndex < 3:
            stacks[stackIndex].config(image = blue_large_square)
            stacks[stackIndex].image = blue_large_square
        else:
            stacks[stackIndex].config(image = red_large_square)
            stacks[stackIndex].image = red_large_square
    elif newSize == "Medium":
        if stackIndex < 3:
            stacks[stackIndex].config(image = blue_medium_square)
            stacks[stackIndex].image = blue_medium_square
        else:
            stacks[stackIndex].config(image = red_medium_square)
            stacks[stackIndex].image = red_medium_square
    elif newSize == "Small":
        if stackIndex < 3:
            stacks[stackIndex].config(image = blue_small_square)
            stacks[stackIndex].image = blue_small_square
        else:
            stacks[stackIndex].config(image = red_small_square)
            stacks[stackIndex].image = red_small_square

def changeCell(cellIndex: int, newSize: int, color: str):
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

    if newSize == "Large":
        if color == "Blue":
            cells[cellIndex].config(image = blue_large_square)
            cells[cellIndex].image = blue_large_square
        else:
            cells[cellIndex].config(image = red_large_square)
            cells[cellIndex].image = red_large_square
    elif newSize == "Medium":
        if color == "Blue":
            cells[cellIndex].config(image = blue_medium_square)
            cells[cellIndex].image = blue_medium_square
        else:
            cells[cellIndex].config(image = red_medium_square)
            cells[cellIndex].image = red_medium_square
    if newSize == "Small":
        if color == "Blue":
            cells[cellIndex].config(image = blue_small_square)
            cells[cellIndex].image = blue_small_square
        else:
            cells[cellIndex].config(image = red_small_square)
            cells[cellIndex].image = red_small_square








if __name__ == '__main__':
    # red_large_square = Image.open('Images/red_square.png').resize((70, 70), Image.ANTIALIAS)
    #
    # blue_large_square = Image.open('Images/blue_square.png').resize((70, 70), Image.ANTIALIAS)
    # red_medium_square = ImageTk.PhotoImage(
    #     Image.open('Images/red_square.png').resize((50, 50), Image.ANTIALIAS))
    # red_small_square = ImageTk.PhotoImage(
    #     Image.open('Images/red_square.png').resize((30, 30), Image.ANTIALIAS))

    main()
