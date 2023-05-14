from tkinter import *
frm = Tk()
frm.geometry('450x670+400+150')
frm.config(bg ='cadet blue')
frm.title('Mostafa Caculator')
display = StringVar()
global x
x=0
obj = Entry(frm, relief=RIDGE, textvariable=display, justify='right',
         font='arial 40 bold', bd=10, bg='powder blue', width=20)
obj.place(x=25, y=10, width=400, height=80)
z=110
for exp in ('789*', '456/', '123+', 'c0.-'):
    r=10
    frame=Frame(frm, bd=10, bg='silver')
    frame.place(x=30, y=z, width=390, height=105)
    z = z + 110
    for char in exp:
        butt=Button(frame,text=char, bg='white',font='arial 30 bold',
        bd=10, command=lambda ch=char: getbutt(ch,display,x))
        butt.place(x=r, y=5, width=80, height=80)
        r = r + 90

frame2 = Frame(frm, bd=10, bg='silver')
frame2.place(x=30, y=550, width=390, height=100)
Clearbutton = Button(frm, text='C', bg='white', font='arial 30 bold',
            bd=5, command=lambda: display.set(""))
Clearbutton.place(x=50, y=560, width=80, height=80 )
equal = Button(frm, text='=', bg='white', font='arial 30 bold', bd=5,
               command=lambda: evaluated(display))
equal.place(x=140, y=560, width=80, height=80)
percentbutton = Button(frm, text='%', bg='white', font='arial 30 bold',
         bd=5, command=lambda: display.set(eval(display.get())/100)
                 if display.get() != '' else evaluated(display))
percentbutton.place(x=230, y=560, width=80, height=80)
minustbutton = Button(frm, bg='white', font='arial 30 bold', bd=5,
             command=lambda: display.set('') if display.get() ==''
             else display.set(float(display.get()) * (-1)))
minustbutton.place(x=320, y=560, width=80, height=80)
im=PhotoImage(file='plusminus.gif')
minustbutton.config(image=im)
def getbutt(c,d,y):
    global x
    op_list = ('*', '/', '+', '-')
    op_list1 = ('*', '/', '+', '-', '0')
    # شرط عدم بدء عملية حسابية جديدة باستخدام أزرار العمليات الحسابية أو الصفر ولكن يجب البدء برقم
    if c in op_list1 and d.get()== '':
        d.set('')
        return d
    # مسح الشاشة تماما عند الضغط على أي رقم بعد الانتهاء من كل عملية حسابية بالضغط على زر =
    if y and c not in op_list :
        d.set('')
        x=0
    d.set(d.get() + c)
    x = 0
    # لحذف آخر رقم أو رمز تم إدخاله
    if c=='c':
        d.set(d.get()[:-2])
    return x
def evaluated(stored):
    global x
    try:
        result = eval(stored.get())
        result = round(result,4)
        stored.set(result)
        #stored.set(eval(stored.get()))
        x = 1
        return x
    except:
        stored.set('ERROR')
        x = 1
        return x
frm.mainloop()

