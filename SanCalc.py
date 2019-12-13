from tkinter import *
san="" # san=global variable
def number(n):
    global san
    san=san+str(n)
    input.set(san)

def calculate(n1):
    try:
        res=eval(n1)
        input.set(res)
    except:
        input.set("Error!!!")

def cancel(c):
    global san
    input.set("")
    san=""

root = Tk()
root.configure(bg='yellow')
root.iconbitmap("calculator.ico")
root.title("Calculator")
#root.iconbitmap("calculator.ico")
root.geometry("298x400")
root.resizable(0,0)
input=StringVar()
s1=Entry(root,bg="aliceblue",fg="black",font="Times",width=33,textvariable=input).grid(row=0,column=0,rowspan=2,columnspan=4,padx=10,pady=10)
b1=Button(root,text="1",font="times",bg="dodgerblue",fg="black",width=5,command=lambda:number(1)).grid(row=2,column=0,padx=5,pady=5)
b2=Button(root,text="2",font="Times",bg="dodgerblue",fg="black",width=5,command=lambda:number(2)).grid(row=2,column=1,padx=5,pady=5)
b3=Button(root,text="3",font="Times",bg="dodgerblue",fg="black",width=5,command=lambda:number(3)).grid(row=2,column=2,padx=5,pady=5)
b4=Button(root,text="+",font="Times",bg="red",fg="white",width=5,command=lambda:number("+")).grid(row=2,column=3,padx=5,pady=5)
b5=Button(root,text="4",font="Times",bg="dodgerblue",fg="black",width=5,command=lambda:number(4)).grid(row=3,column=0,padx=5,pady=5)
b6=Button(root,text="5",font="Times",bg="dodgerblue",fg="black",width=5,command=lambda:number(5)).grid(row=3,column=1,padx=5,pady=5)
b7=Button(root,text="6",font="Times",bg="dodgerblue",fg="black",width=5,command=lambda:number(6)).grid(row=3,column=2,padx=5,pady=5)
b8=Button(root,text="-",font="Times",bg="red",fg="white",width=5,command=lambda:number("-")).grid(row=3,column=3,padx=5,pady=5)
b9=Button(root,text="7",font="Times",bg="dodgerblue",fg="black",width=5,command=lambda:number(7)).grid(row=4,column=0,padx=5,pady=5)
b10=Button(root,text="8",font="Times",bg="dodgerblue",fg="black",width=5,command=lambda:number(8)).grid(row=4,column=1,padx=5,pady=5)
b11=Button(root,text="9",font="Times",bg="dodgerblue",fg="black",width=5,command=lambda:number(9)).grid(row=4,column=2,padx=5,pady=5)
b12=Button(root,text="*",font="Times",bg="red",fg="white",width=5,command=lambda:number("*")).grid(row=4,column=3,padx=5,pady=5)
b13=Button(root,text="0",font="Times",bg="dodgerblue",fg="black",width=5,command=lambda:number("0")).grid(row=5,column=0,padx=5,pady=5)
b14=Button(root,text=".",font="Times",bg="aliceblue",fg="black",width=5,command=lambda:number(".")).grid(row=5,column=1,padx=5,pady=5)
b15=Button(root,text="Clear",font="Times,20",bg="brown",fg="white",width=5,command=lambda:cancel("san")).grid(row=5,column=2,padx=5,pady=5)
b16=Button(root,text="/",font="Times",bg="red",fg="white",width=5,command=lambda:number("/")).grid(row=5,column=3,padx=5,pady=5)
b17=Button(root,text="Mod",font='Times',bg="brown",fg="white",width=5,command=lambda:number("%")).grid(row=6,column=0,padx=10,pady=10)
b18=Button(root,text="Int",font='Times',bg="brown",fg="white",width=5,command=lambda:number("//")).grid(row=6,column=1,padx=10,pady=10)
b19=Button(root,text="Exp",font='Times',bg="brown",fg="white",width=5,command=lambda:number("**")).grid(row=6,column=2,padx=10,pady=10)
b20=Button(root,text="OFF",font='Times',bg="brown",fg="white",width=5,command=root.quit).grid(row=6,column=3,padx=10,pady=10)
b21=Button(root,text="=",bg="green",fg="white",font='Times',width=30,command=lambda:calculate(san)).grid(row=7,column=0,rowspan=2,
columnspan=4,padx=10,pady=10)


label1=Label(root,text="Copyright@2019.Sanjay Kr Pandit",font=("Times",12),height=1,width=200,bg="black",fg="aliceblue")
label1.place(relx=0.10, rely=0.85, height=25, width=240)
root.mainloop()

