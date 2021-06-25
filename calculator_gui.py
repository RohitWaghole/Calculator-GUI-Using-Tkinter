from tkinter import *

lst = [["C","**","%","/"],["7","8","9","*"],["4","5","6","-"],["1","2","3","+"],[".","00","(",")"],["0","="]]

def click(event):
    global scrnvalue
    text = event.widget.cget("text")
    value = scrnvalue.get()
    
    if text == "C":
        value = ""
    elif text == "=":
        if scrnvalue.get().isdigit():
            value = scrnvalue.get()
        else:
            try:
                value = eval(scrnvalue.get())
            except:
                value = "Error"
    else:
        value = scrnvalue.get()+text
    
    scrnvalue.set(value)
    screen.update()

root = Tk()
root.minsize(330,480)
root.geometry("330x480")
root.maxsize(330,480)
root.title("Calculator by Rohit")
root.configure(bg="yellow")

scrnvalue = StringVar()
scrnvalue.set("")

screen = Entry(root,textvariable=scrnvalue,font="lucida 30",borderwidth=5,fg="blue")
screen.pack(fill=X,pady=20)

for i in lst:
    f = Frame(root)
    for j in i:
        
        if j=="C":
            b = Button(f,text=j,font="lucida 20",borderwidth=5,bg="black",fg="red")
        elif j=="**" or j=="%" or j=="/":
            b = Button(f,text=j,font="lucida 20",borderwidth=5,bg="black",fg="blue")
        elif j=="(" or j==")":
            b = Button(f,text=j,font="lucida 20",borderwidth=5,bg="black",fg="blue",padx=4)
        elif j=="*" or j=="-":
            b = Button(f,text=j,font="lucida 20",borderwidth=5,bg="black",fg="blue",padx=9)
        elif j=="=":
            b = Button(f,text=j,font="lucida 20",borderwidth=5,bg="blue",fg="white",padx=40)
        elif j=="+":
            b = Button(f,text=j,font="lucida 20",borderwidth=5,bg="black",fg="blue",padx=5)
        elif j=="0":
            b = Button(f,text=j,font="lucida 20",borderwidth=5,bg="black",fg="white",padx=10)
        else:
            b = Button(f,text=j,font="lucida 20",borderwidth=5,bg="black",fg="white")
        b.pack(side=LEFT)
        b.bind("<Button-1>",click)
    f.pack()

root.mainloop()
