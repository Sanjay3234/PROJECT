import tkinter.ttk as tkrtk
import tkinter as tkr
import os
def chooseImage():
    os.system("Explorer")


# Creatink window for gui
root=tkr.Tk()

# Edating  window for gui
root.title("Chit-Chat")
root.geometry("450x450")
root.iconbitmap("chat.ico")
root.resizable(0,0)
root.configure(background="aliceblue")
# setting path of the image that is to be encrypted
path= tkr.StringVar()
message= tkr.StringVar()

# creating menubar

notebook=tkrtk.Notebook(root)

# creating tab for encoding and decoding in menubar for message
tb1=tkrtk.Frame(notebook)
tb2=tkrtk.Frame(notebook)

# now adding tab of encoding and decoding in menubar for message
notebook.add(tb1, text="Encryption")
notebook.add(tb2, text="Decryption")
notebook.pack(fill="both", expand="yes")

# now adding  label1  for showing title ( WELCOME TO IMAGE - MESSAGE ENCRYPTION PROCESS )
label1=tkr.Label(tb1,text="WELCOME TO IMAGE - MESSAGE ENCRYPTION PROCESS",font=("Times",12),height=1,bg="green",)
label1.pack(padx=10,pady=15)

# now adding  button1  for choosing image from the browser for encryption
b1= tkr.Button(tb1, text="Choose Image", font=("times",12),bg="dodgerblue", fg="black",width=1,command=lambda:chooseImage())
b1.place(relx=0.30, rely=0.15, height=40, width=194)


# now adding  entry1 to show the path of image selected from browser for encryption
e1 = tkr.Entry(tb1, textvariable=path, background="black", fg="red", font=("Times",12))
e1.place(relx=0.10, rely=0.29, height=30, width=355)


# now adding  label1  for showing title ( WELCOME TO IMAGE - MESSAGE ENCRYPTION PROCESS )
label2=tkr.Label(tb1,text="Enter Your Message To Be Encoded Below !",font=("Times",12),height=1,width=200,bg="yellow",)
label2.place(relx=0.10, rely=0.40, height=25, width=355)

# now adding  entry2 to write the message that should be encrypted in the image selected
e2 = tkr.Entry(tb1, textvariable=message, background="black", fg="red", font=("Times",12))
e2.place(relx=0.10, rely=0.50, height=30, width=355)

# now adding  button2  to encrypt the message in the selected image from file explorer
b2= tkr.Button(tb1, text="Encrypt", font=("times",12),bg="brown", fg="black",width=1)
b2.place(relx=0.10, rely=0.70, height=40, width=95)

# now adding  button3  to Save the message which is encrypted in the selected image from file explorer
b3= tkr.Button(tb1, text="Save", font=("times",12),bg="orange", fg="black",width=1)
b3.place(relx=0.70, rely=0.70, height=40, width=95)



# now adding  label3  to show the copy copyright of the program
label3=tkr.Label(tb1,text="Copyright@2019.Sanjay Kumar Pandit",font=("Times",12),height=1,width=200,bg="black",fg="aliceblue")
label3.place(relx=0.10, rely=0.90, height=25, width=355)
# tb2 code starts


# now adding  label1  for showing title ( WELCOME TO IMAGE - MESSAGE DECRYPTION PROCESS )
label1=tkr.Label(tb2,text="WELCOME TO IMAGE - MESSAGE DECRYPTION PROCESS",font=("Times",12),height=1,bg="green",)
label1.pack(padx=10,pady=15)

# now adding  button1  for choosing image from the browser for encryption
b1= tkr.Button(tb2, text="Choose Image", font=("times",12),bg="dodgerblue", fg="black",width=1,command=lambda:chooseImage())
b1.place(relx=0.30, rely=0.15, height=40, width=194)

# now adding  entry1 to show the path of image selected from browser for encryption
e1 = tkr.Entry(tb2, textvariable=path, background="black", fg="red", font=("Times",12))
e1.place(relx=0.10, rely=0.29, height=30, width=355)


# now adding  label2  for ( showing title Your Decrypted Message Is Shown Below ! )
label2=tkr.Label(tb2,text="Your Decrypted Message Is Shown Below !",font=("Times",12),height=1,width=200,bg="yellow",)
label2.place(relx=0.10, rely=0.40, height=25, width=355)

# now adding  entry2 to show the message that was encrypted in the image selected
e2 = tkr.Entry(tb2, textvariable=message, background="black", fg="red", font=("Times",12))
e2.place(relx=0.10, rely=0.50, height=30, width=355)

# now adding  button2  to Decrypt  the message which was encrypted in the selected image from file explorer
b2= tkr.Button(tb2, text="Decrypt", font=("times",12),bg="red", fg="black",width=1)
b2.place(relx=0.40, rely=0.65, height=40, width=95)

# now adding  label3  to show the copy copyright of the program
label3=tkr.Label(tb2,text="Copyright@2019.Sanjay Kumar Pandit",font=("Times",12),height=1,width=200,bg="black",fg="aliceblue")
label3.place(relx=0.10, rely=0.90, height=25, width=355)
root.mainloop()