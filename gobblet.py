import tkinter as tk
from tkinter import font, PhotoImage
from PIL import ImageTk, Image
from globals import *

cells = [0] * 9
stacks1 = [0] * 3
stacks2 = [0] * 3

def main():
    helloScreen = tk.Tk()
    helv16 = font.Font(root = helloScreen, family="Helvetica", size=16,
                  weight="bold")
    helloScreen.geometry("800x400")
    imgFrame = tk.Frame(helloScreen, width=800, height=500)
    imgFrame.place(anchor="center")
    imgFrame.pack()
    startingImg = ImageTk.PhotoImage(Image.open("gobbletgobblers.jpg"))

    imgLabel = tk.Label(imgFrame, image=startingImg)
    imgLabel.pack()
    #TODO: change command to a function allowing to select modes (human vs
    # AI, AI vs AI)
    startButton = tk.Button(helloScreen, text = "Start",
                            command=lambda: setGameModes(helloScreen),
                            width=7, height=3,
                            font=helv16,
                            activeforeground="red", bg="light green")
    startButton.place(x=650, y=300)

    helloScreen.mainloop()




def setGameModes(prevWindow):

    prevWindow.destroy()
    selectionScreen = tk.Tk()
    selectionScreen.geometry("500x300")
    helv32 = font.Font(root = selectionScreen, family="Helvetica", size=32,
                  weight="bold")
    helv16 = font.Font(root = selectionScreen, family="Helvetica", size=16,
                  weight="bold")
    selectQuestion = tk.Label(text="Choose a Game Mode:", fg="black",
                              font=helv32)
    selectQuestion.pack(anchor="center")

    #TODO: set functions that set up players for each button
    HumanButton = tk.Button(selectionScreen, text = "Human vs AI",
                            command=lambda: humanVsAi(selectionScreen),
                            width=10, height=5,
                            font=helv16,
                            activeforeground="red", bg="light blue")

    AiButton = tk.Button(selectionScreen, text = "AI vs AI",
                            command=selectionScreen.destroy,
                            width=10, height=5,
                            font=helv16,
                            activeforeground="red", bg="light blue")
    HumanButton.place(x=60, y=100)
    AiButton.place(x=300,y = 100)

def humanVsAi(prevWindow):
    prevWindow.destroy()
    gameScreen = tk.Tk()
    gameScreen.geometry("400x550")
    for i in range(9):
        if i < 2:
            yCor = 100
        if 3 <= i < 6:
            yCor = 220
        if i >= 6:
            yCor = 340
        cells[i]=tk.Button(gameScreen,
                            width=15, height=7, highlightcolor="black")
        cells[i].place(x=25+115*(i%3), y=yCor)

    for i in range(3):
        stacks1[i]=tk.Button(gameScreen,
                            width=9, height=4, bg="blue", command=lambda:
            removeFromStack(i))
        stacks1[i].place(x=70 + i*90, y=15)

    for i in range(3):
        stacks2[i]=tk.Button(gameScreen,
                            width=9, height=4, bg="red")
        stacks2[i].place(x=70 + i*90, y=470)

def removeFromStack(stackIndex: int) -> None:
    print(stacks1[stackIndex].winfo_height())
    if stacks1[stackIndex].winfo_width() == 73:
        stacks1[stackIndex].config(width = MEDIUM_STACK_W)
        stacks1[stackIndex].config(height=MEDIUM_STACK_H)






if __name__ == '__main__':
    main()
