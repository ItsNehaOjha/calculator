from tkinter import *
root = Tk()
root.geometry("420x320")
root.title("Calculator by Neha ")
def click(event):
    global scvalue
    text= event.widget.cget("text")
    print(text)
    if text== "=":
        if scvalue.get().isdigit():
            value= int(scvalue.get())
        else:
            value= eval(screen.get())
        scvalue.set(value)
        screen.update()
    
    elif text=="C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() +text)
        screen.update()

scvalue= StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="lucida 30 bold", bg="RED")
screen.pack(fill=X, ipadx=5, pady=2, padx=5)
f= Frame(root, bg="BLACK")
b=Button (f, text="9",padx=28, pady=2, font="lucida 15 bold")
b.pack(side = LEFT, padx=10, pady=10 ,fill=X)
b.bind("<Button-1>", click)
b=Button (f, text="8",padx=28, pady=2, font="lucida 15 bold")
b.pack(side = LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)
b=Button (f, text="7",padx=28, pady=2, font="lucida 15 bold")
b.pack(side = LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)
b=Button (f, text="-",padx=28, pady=2, font="lucida 15 bold")
b.pack(side = RIGHT, padx=10, pady=10)
b.bind("<Button-1>", click)
f.pack()


f= Frame(root, bg="BLACK")
b=Button (f, text="6",padx=26, pady=2, font="lucida 15 bold")
b.pack(side = LEFT, padx=12, pady=10, fill=X)
b.bind("<Button-1>", click)
b=Button (f, text="5",padx=26, pady=2, font="lucida 15 bold")
b.pack(side = LEFT, padx=12, pady=10)
b.bind("<Button-1>", click)
b=Button (f, text="4",padx=26, pady=2, font="lucida 15 bold")
b.pack(side = LEFT, padx=12, pady=10)
b.bind("<Button-1>", click)
b=Button (f, text="/",padx=26, pady=2, font="lucida 15 bold")
b.pack(side = LEFT, padx=12, pady=10)
b.bind("<Button-1>", click)
f.pack()



f= Frame(root, bg="BLACK")
b=Button (f, text="3",padx=26, pady=2, font="lucida 15 bold")
b.pack(side = LEFT, padx=11, pady=10)
b.bind("<Button-1>", click)
b=Button (f, text="2",padx=26, pady=2, font="lucida 15 bold")
b.pack(side = LEFT, padx=11, pady=10)
b.bind("<Button-1>", click)
b=Button (f, text="1",padx=26, pady=2, font="lucida 15 bold")
b.pack(side = LEFT, padx=11, pady=10)
b.bind("<Button-1>", click)
b=Button (f, text="+",padx=26, pady=2, font="lucida 15 bold")
b.pack(side = LEFT, padx=11, pady=10)
b.bind("<Button-1>", click)
f.pack()

f= Frame(root, bg="BLACK")
b=Button (f, text="C",padx=26, pady=2, font="lucida 13 bold")
b.pack(side = LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)
b=Button (f, text="0",padx=28, pady=2, font="lucida 15 bold")
b.pack(side = LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)
b=Button (f, text="*",padx=28, pady=2, font="lucida 15 bold")
b.pack(side = LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)
b=Button (f, text="=",padx=28, pady=2, font="lucida 15 bold")
b.pack(side = LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)
f.pack()


root.mainloop()
