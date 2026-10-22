import tkinter as tk
import tkinter.messagebox as msg
top = tk.Tk()
CheckVar1=StringVar()
C=tk.Checkbutton(top,text="Gender, check kalau laki2",
variable=CheckVar1,offvalue="Tampan",offrelief="Cantik",height=5)
C.pack()
L1=tk.Label(top,text="Nama");L1.pack()
E1=tk.Entry(top, bd=5);E1.pack

def helloCalBack():
    msg.showinfo("Belejar GUI","Assalamu alaikum" + E1.get() + "! Kamu " + CheckVar1.get() + "sekali hari ini !")

    W1=tk.Button(top, text="Click Me!", command=helloCalBack)
    W1.pack()
    top.mainloop()