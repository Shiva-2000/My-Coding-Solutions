from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("Tic Tac Toe")

x_click=True
count=0
winner=False

def btn_click(btn):
    global x_click,count
    if(btn["text"]=="" and x_click==True):
        btn["text"]='X'
        x_click=False
        count+=1
        check_winner('X')
    elif(btn["text"]=="" and x_click==False):
        btn["text"]="O"
        x_click=True
        count+=1
        check_winner('O')
    else:
        messagebox.showerror("Tic Tac Toe Error","You clicked the wrong button!!")

def check_winner(s):
    global winner
    if(b1["text"]==s and b2["text"]==s and b3["text"]==s):
        b1["bg"]='yellow';b2["bg"]='yellow';b3["bg"]='yellow'
        winner=True
        s='Congratulation '+s+', You Won'
        messagebox.showinfo("Tic Tac Toe Winner",s)
        Restart_Game()
        
    elif(b4["text"]==s and b5["text"]==s and b6["text"]==s):
        b4["bg"]='yellow';b5["bg"]='yellow';b6["bg"]='yellow'
        winner=True
        s='Congratulation '+s+', You Won'
        messagebox.showinfo("Tic Tac Toe Winner",s)
        Restart_Game()
        
    elif(b7["text"]==s and b8["text"]==s and b9["text"]==s):
        b7["bg"]='yellow';b8["bg"]='yellow';b9["bg"]='yellow'
        winner=True
        s='Congratulation '+s+', You Won'
        messagebox.showinfo("Tic Tac Toe Winner",s)
        Restart_Game()
        
    elif(b1["text"]==s and b4["text"]==s and b7["text"]==s):
        b1["bg"]='yellow';b4["bg"]='yellow';b7["bg"]='yellow'
        winner=True
        s='Congratulation '+s+', You Won'
        messagebox.showinfo("Tic Tac Toe Winner",s)
        Restart_Game()
        
    elif(b2["text"]==s and b5["text"]==s and b8["text"]==s):
        b2["bg"]='yellow';b5["bg"]='yellow';b8["bg"]='yellow'
        winner=True
        s='Congratulation '+s+', You Won'
        messagebox.showinfo("Tic Tac Toe Winner",s)
        Restart_Game()
        
    elif(b3["text"]==s and b6["text"]==s and b9["text"]==s):
        b3["bg"]='yellow';b6["bg"]='yellow';b9["bg"]='yellow'
        winner=True
        s='Congratulation '+s+', You Won'
        messagebox.showinfo("Tic Tac Toe Winner",s)
        Restart_Game()
        
    elif(b1["text"]==s and b5["text"]==s and b9["text"]==s):
        b1["bg"]='yellow';b5["bg"]='yellow';b9["bg"]='yellow'
        winner=True
        s='Congratulation '+s+', You Won'
        messagebox.showinfo("Tic Tac Toe Winner",s)
        Restart_Game()

    elif(b3["text"]==s and b5["text"]==s and b7["text"]==s):
        b3["bg"]='yellow';b5["bg"]='yellow';b7["bg"]='yellow'
        winner=True
        s='Congratulation '+s+', You Won'
        messagebox.showinfo("Tic Tac Toe Winner",s)
        Restart_Game()
        
    elif(count==9 and winner==False):
        messagebox.showinfo("Tic Tac Toe Winner","uffs, No One Wins...")
        Restart_Game()

def Restart_Game():
    global x_click,count,winner
    count=0;x_click=True;winner=False
    b1["text"]="";b1["bg"]="red"
    b2["text"]="";b2["bg"]="red"
    b3["text"]="";b3["bg"]="red"
    b4["text"]="";b4["bg"]="red"
    b5["text"]="";b5["bg"]="red"
    b6["text"]="";b6["bg"]="red"
    b7["text"]="";b7["bg"]="red"
    b8["text"]="";b8["bg"]="red"
    b9["text"]="";b9["bg"]="red"

#Frames
f1=Frame(root,bg='powder blue')
f2=Frame(root,bg='powder blue')
f3=Frame(root,bg='powder blue')

#Buttons
b1=Button(f1,text="",font=("verdana",60),height=1,width=3,bg='red',command= lambda: btn_click(b1))
b2=Button(f1,text="",font=("verdana",60),height=1,width=3,bg='red',command= lambda: btn_click(b2))
b3=Button(f1,text="",font=("verdana",60),height=1,width=3,bg='red',command= lambda: btn_click(b3))

b4=Button(f2,text="",font=("verdana",60),height=1,width=3,bg='red',command= lambda: btn_click(b4))
b5=Button(f2,text="",font=("verdana",60),height=1,width=3,bg='red',command= lambda: btn_click(b5))
b6=Button(f2,text="",font=("verdana",60),height=1,width=3,bg='red',command= lambda: btn_click(b6))

b7=Button(f3,text="",font=("verdana",60),height=1,width=3,bg='red',command= lambda: btn_click(b7))
b8=Button(f3,text="",font=("verdana",60),height=1,width=3,bg='red',command= lambda: btn_click(b8))
b9=Button(f3,text="",font=("verdana",60),height=1,width=3,bg='red',command= lambda: btn_click(b9))

b1.pack(side=LEFT,padx=10,pady=10)
b2.pack(side=LEFT,padx=10,pady=10)
b3.pack(side=LEFT,padx=10,pady=10)

b4.pack(side=LEFT,padx=10,pady=10)
b5.pack(side=LEFT,padx=10,pady=10)
b6.pack(side=LEFT,padx=10,pady=10)

b7.pack(side=LEFT,padx=10,pady=10)
b8.pack(side=LEFT,padx=10,pady=10)
b9.pack(side=LEFT,padx=10,pady=10)

f1.pack()
f2.pack()
f3.pack()

root.mainloop()
