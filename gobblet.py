import tkinter as tk
from tkinter import font, PhotoImage
from PIL import ImageTk, Image
from globals import *

cells = [0] * 9
stacks1 = [0] * 3
stacks2 = [0] * 3


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
    red_large_square =  ImageTk.PhotoImage(Image.open('Images/red_square.png').resize((70, 70)))

    blue_large_square = ImageTk.PhotoImage(Image.open('Images/blue_square.png').resize((70, 70)))

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
        cells[i] = tk.Button(prevWindow,
                             width=15, height=7, highlightcolor="black", bg="white")
        cells[i].place(x=25 + 115 * (i % 3), y=yCor)

    for i in range(3):
        stacks1[i] = tk.Button(prevWindow,
                                image=blue_large_square, command=lambda: removeFromStack(i))
        stacks1[i].image = blue_large_square
        stacks1[i].place(x=70 + i * 90, y=15)

    for i in range(3):
        stacks2[i] = tk.Button(prevWindow,
                               image=red_large_square)
        stacks2[i].image = red_large_square
        stacks2[i].place(x=70 + i * 90, y=470)


def removeFromStack(stackIndex: int) -> None:
    pass
    # print(stacks1[stackIndex].winfo_height())
    # if stacks1[stackIndex].winfo_width() == 73:
    #     stacks1[stackIndex].config(width=MEDIUM_STACK_W)
    #     stacks1[stackIndex].config(height=MEDIUM_STACK_H)


if __name__ == '__main__':
    # red_large_square = Image.open('Images/red_square.png').resize((70, 70), Image.ANTIALIAS)
    #
    # blue_large_square = Image.open('Images/blue_square.png').resize((70, 70), Image.ANTIALIAS)
    # red_medium_square = ImageTk.PhotoImage(
    #     Image.open('Images/red_square.png').resize((50, 50), Image.ANTIALIAS))
    # red_small_square = ImageTk.PhotoImage(
    #     Image.open('Images/red_square.png').resize((30, 30), Image.ANTIALIAS))

    main()
