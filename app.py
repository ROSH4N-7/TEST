from tkinter import*
app=Tk()
app.title("Add two numbers")
app.geometry('500x500')
e1=Entry(app)
e1.pack()
e2=Entry(app)
e2.pack()
result=Label(app,text="0")
result.pack()

def add_numbers():
    try:
        a=int(e1.get())
        b=int(e2.get())
        result.config(text=str(a+b))
    except ValueError:
        result.config(text="ERROR VAYOO")

btn=Button(app,text="Add", command=add_numbers)
btn.pack()

if __name__=="__main__":
    app.mainloop()