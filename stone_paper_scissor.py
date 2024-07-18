from tkinter import *
import random

def winner():
    global choice
    choicec = choice[random.randint(0, 2)]
    user = enter.get()
    computer = choicec
    if user=="stone":
        if computer == "paper":
            win = ""
            win += f"Lost\ncomputer has chosen {computer}"

        elif computer == "scissor":
            win = ""
            win += f"Yayyyy congratulations\ncomputer has chosen {computer}"

        else:
            win = ""
            win += f"Tie\ncomputer has chosen {computer}"


    elif user=="paper":
        if computer=="paper":
            win = ""
            win+=f"tie\ncomputer has chosen {computer}"

        elif computer=="scissor":
            win = ""
            win+=f"you lost\ncomputer has chosen {computer}"

        else:
            win = ""
            win+=f"Yayyyy Congratulaion\ncomputer has chosen {computer}"


    else:
        if computer=="paper":
            win = ""
            win+=f"Yayyyy Congratulaion\ncomputer has chosen {computer}"

        elif computer=="stone":
            win = ""
            win+=f"you lost\ncomputer has chosen {computer}"

        else:
            win = ""
            win+=f"tie\ncomputer has chosen {computer}"

    Label(root,text=win).pack()


def pl():
    global enter,entry_enter
    label_entry = Label(root, text="enter your choice", font="lucida 12 bold")
    label_entry.pack(pady=10)

    enter = StringVar()
    enter.set("")
    entry_enter.update()
    entry_enter = Entry(root, textvariable=enter, font="lucida 12 bold")
    entry_enter.pack()

    b = Button(root, text="click me to get result", command=winner)
    b.pack()


root = Tk()
root.geometry("600x500")
root.title("My Stone Paper Scissor Game")


choice = ["stone","paper","scissor"]

mainl = Label(root, text="Stone Paper Scissor Game", font="comicsansms 40 bold", borderwidth=3, relief=RIDGE)
mainl.pack(fill=X)
info = "Welcome to our GUI\nIn this GUI,you have to choose either from stone,paper or scissor and then computer chooses one from stone,paper or scissor.\nnow depending on your choice result will be declared and displayed who won.\nStone beats Scissor.\nPaper beats Stone\nScissor beats paper"
infolabel = Label(root, text=info, font="comicsansms 14 bold", borderwidth=3, relief=RIDGE)
infolabel.pack(fill=X)

label_entry = Label(root,text="enter your choice",font="lucida 12 bold")
label_entry.pack(pady=10)

enter = StringVar()
enter.set("")
entry_enter = Entry(root,textvariable=enter,font="lucida 12 bold")
entry_enter.pack()
b = Button(root,text="click me to get result",command=winner)
b.pack()


b2 = Button(root,text="play again",command=pl)
b2.pack(side=BOTTOM)
label_entry2 = Label(root,text="wanna play again",font="lucida 12 bold")
label_entry2.pack(pady=10,side=BOTTOM)
root.mainloop()