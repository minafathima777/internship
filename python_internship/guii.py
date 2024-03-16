# from tkinter import *

# root = Tk()
# root.mainloop() 
# from tkinter import *

# root=Tk()
# root.title("welcome to python lobby")
# root.geometry("300x200")
# lbl=Label(root, text ='hello my name is akshay' , font=("helvetica",13),fg = 'white' , bg = 'black')
# lbl.pack()
# root.mainloop()

# from tkinter import *
# root=Tk()
# root.title("welcome to python lobby")
# def clicked():
#     print("i am clicked")
# btn = Button(root, text="click me", command = clicked)
# btn.pack()
# root.geometry('250x200')
# root.mainloop()

# from tkinter import *
# root = Tk()
# root.title ("welcome to python lobby")
# root.geometry('300x200')
# entry = Entry(root, bg="yellow",fg="red",bd=5)

# entry.place(x=100,y=200)
# entry.mainloop()

from tkinter import *
root = Tk()
root.title ("welcome to facebook")
root.geometry("300x200")
lbl1=Label(root,text='Facebook',font=("blod",15),fg = 'blue',bg = 'white')
lbl1.place(x=100,y=100)

lbl2=Label(root,text='username',font=("bold",15),fg = 'black',bg = 'white')
lbl2.place(x=100,y=200)
entry = Entry(root,bg="white",fg="black",bd=5)
entry.place(x=250,y=250)

lbl3=Label(root,text='password',font=("blod",15),fg = 'black',bg = 'white')
lbl3.place(x=100,y=200)
entry = Entry(root,bg="white",fg="black",bd=5)
entry.place(x=250,y=250)
root.mainloop()




