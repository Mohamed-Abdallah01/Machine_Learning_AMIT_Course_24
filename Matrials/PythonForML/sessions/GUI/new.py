from tkinter import *
import webbrowser


def myfun():
    link = mytext.get()
    webbrowser.open(link)


myframe = Tk()
myframe.title("All Will Found Here")
myframe.geometry('950x550')


mylabe = Label(myframe, text="Google First Version",font="sans" , padx=20 , pady=10)
mylabe.pack(padx=20)


mytext = Entry(myframe , width=50)
mytext.pack(pady=20)

mybutton = Button(myframe , text="Enter Here" , fg="white" , bg="black" , font="sans " , padx=20,pady=5 ,command=myfun)
mybutton.pack()


myframe.mainloop()