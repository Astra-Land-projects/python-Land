from tkinter import * 
from tkinter import messagebox
window = Tk()
window.title("first tkinter")
window.geometry("400x300+200+150")
window.config(bg='pink')

def f():
    username=e1.get() # type: ignore
    password=e2.get() # type: ignore
    if username=="alireza" and password=="123456":
        messagebox.showinfo("ok","username and password is correct")
    else:
        messagebox.showerror("error","username or password is incorrect")  
ibiuser = Label (window, text="enter user:",font=('arial',14,'bold'))  
ibiuser.grid(row=0 , column=0) 

e1=Entry(window,font=('arial',14,'bold'))
e1.grid(row=0 , column=1)

ibiuser = Label (window, text="enter password:",font=('arial',14,'bold'))  
ibiuser.grid(row=1 , column=0) 

e2=Entry(window, show='*' , font=('arial',14,'bold'))
e2.grid(row=1 , column=1)

b1=Button(window,text="ok",font=('arial',14,'bold'),padx=10,pady=5,command=f)
b1.grid(row=2,column=1)

window.mainloop()
#مشکل دارد