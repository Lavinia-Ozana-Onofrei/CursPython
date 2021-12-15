from tkinter import *
import random
import time
from tkinter import messagebox

window = Tk()
window.geometry('1350x750')
window.title('Coffee Shop')
window.configure(background='#EBD2EF')
window.resizable(0, 0)

# -------------functii-------------
TotalCost = StringVar()
DateofOrder = StringVar()
DateofOrder.set(time.strftime("%d/%m/%Y"))


def f_Exit():
    command = messagebox.askyesno("Quit System", "Do you want to quit?")
    print(command)
    if command > 0:
        window.destroy()
        return


def f_Reset():
    TotalCost.set("")
    txtReceipt.delete("1.0", END)

    var_Latte.set(0)
    var_Irish.set(0)
    var_Espresso.set(0)
    var_Cappucciono.set(0)
    var_Americano.set('0')
    var_Mocaccino.set('0')
    var_IcedLatte.set('0')
    var_Mocha.set('0')
    var_IcedCoffee.set('0')
    var_BubbleTea.set('0')
    var_CafeFrappucino.set('0')
    var_CaramelMaciato.set('0')

    var0.set(0)
    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)

    txtLatte.configure(state=DISABLED)
    txtIrish.configure(state=DISABLED)
    txtEspresso.configure(state=DISABLED)
    txtCappucciono.configure(state=DISABLED)
    txtAmericano.configure(state=DISABLED)
    txtMocaccino.configure(state=DISABLED)
    txtIcedLatte.configure(state=DISABLED)
    txtMocha.configure(state=DISABLED)
    txtIcedCoffee.configure(state=DISABLED)
    txtBubbleTea.configure(state=DISABLED)
    txtCafeFrappucino.configure(state=DISABLED)
    txtCaramelMaciato.configure(state=DISABLED)


def CostOfItem():
    Item1 = float(var_Latte.get())
    Item2 = float(var_Irish.get())
    Item3 = float(var_Espresso.get())
    Item4 = float(var_Cappucciono.get())
    Item5 = float(var_Americano.get())
    Item6 = float(var_Mocaccino.get())
    Item7 = float(var_IcedLatte.get())
    Item8 = float(var_Mocha.get())
    Item9 = float(var_IcedCoffee.get())
    Item10 = float(var_BubbleTea.get())
    Item11 = float(var_CafeFrappucino.get())
    Item12 = float(var_CaramelMaciato.get())

    PriceOfItem = (Item1 * 5) + (Item2 * 4) + (Item3 * 4) + (Item4 * 7) + (Item5 * 8) + (Item6 * 6) + (Item7 * 9) + (Item8 * 7) + (Item9 * 9) + (Item10 * 12) + (Item11 * 12) + (Item12 * 9)
    TotalCost.set(PriceOfItem)


def f_receipt():
    txtReceipt.delete("1.0", END)
    txtReceipt.insert(END, 'Date \t\t\t\t\t' + DateofOrder.get() + '\n\n')
    txtReceipt.insert(END, 'Items \t\t\t\t\t' + 'Number of Items \n\n')
    if var0.get() != 0:
        txtReceipt.insert(END, 'Latte \t\t\t\t\t' + var_Latte.get() + '\n\n')
    if var1.get() != 0:
        txtReceipt.insert(END, 'Irish \t\t\t\t\t' + var_Irish.get() + '\n\n')
    if var2.get() != 0:
        txtReceipt.insert(END, 'Espresso \t\t\t\t\t' + var_Espresso.get() + '\n\n')
    if var3.get() != 0:
        txtReceipt.insert(END, 'Cappucciono \t\t\t\t\t' + var_Cappucciono.get() + '\n\n')
    if var4.get() != 0:
        txtReceipt.insert(END, 'Americano \t\t\t\t\t' + var_Americano.get() + '\n\n')
    if var5.get() != 0:
        txtReceipt.insert(END, 'Mocaccino \t\t\t\t\t' + var_Mocaccino.get() + '\n\n')
    if var6.get() != 0:
        txtReceipt.insert(END, 'IcedLatte \t\t\t\t\t' + var_IcedLatte.get() + '\n\n')
    if var7.get() != 0:
        txtReceipt.insert(END, 'Mocha \t\t\t\t\t' + var_Mocha.get() + '\n\n')
    if var8.get() != 0:
        txtReceipt.insert(END, 'IcedCoffee \t\t\t\t\t' + var_IcedCoffee.get() + '\n\n')
    if var9.get() != 0:
        txtReceipt.insert(END, 'BubbleTea \t\t\t\t\t' + var_BubbleTea.get() + '\n\n')
    if var10.get() != 0:
        txtReceipt.insert(END, 'CafeFrappucino \t\t\t\t\t' + var_CafeFrappucino.get() + '\n\n')
    if var11.get() != 0:
        txtReceipt.insert(END, 'CaramelMaciato \t\t\t\t\t' + var_CaramelMaciato.get() + '\n\n')
    txtReceipt.insert(END, 'Total \t\t\t\t\t' + TotalCost.get() + '\n\n')


def checkbutton():
    if var0.get() == 1:
        txtLatte.configure(state=NORMAL)
    elif var0.get() == 0:
        txtLatte.configure(state=DISABLED)
        var_Latte.set('0')
    if var1.get() == 1:
        txtIrish.configure(state=NORMAL)
    elif var1.get() == 0:
        txtIrish.configure(state=DISABLED)
        var_Irish.set('0')
    if var2.get() == 1:
        txtEspresso.configure(state=NORMAL)
    elif var2.get() == 0:
        txtEspresso.configure(state=DISABLED)
        var_Espresso.set('0')
    if var3.get() == 1:
        txtCappucciono.configure(state=NORMAL)
    elif var3.get() == 0:
        txtCappucciono.configure(state=DISABLED)
        var_Cappucciono.set('0')
    if var4.get() == 1:
        txtAmericano.configure(state=NORMAL)
    elif var4.get() == 0:
        txtAmericano.configure(state=DISABLED)
        var_Americano.set('0')
    if var5.get() == 1:
        txtMocaccino.configure(state=NORMAL)
    elif var5.get() == 0:
        txtMocaccino.configure(state=DISABLED)
        var_Mocaccino.set('0')
    if var6.get() == 1:
        txtIcedLatte.configure(state=NORMAL)
    elif var6.get() == 0:
        txtIcedLatte.configure(state=DISABLED)
        var_IcedLatte.set('0')
    if var7.get() == 1:
        txtMocha.configure(state=NORMAL)
    elif var7.get() == 0:
        txtMocha.configure(state=DISABLED)
        var_Mocha.set('0')
    if var8.get() == 1:
        txtIcedCoffee.configure(state=NORMAL)
    elif var8.get() == 0:
        txtIcedCoffee.configure(state=DISABLED)
        var_IcedCoffee.set('0')
    if var9.get() == 1:
        txtBubbleTea.configure(state=NORMAL)
    elif var9.get() == 0:
        txtBubbleTea.configure(state=DISABLED)
        var_BubbleTea.set('0')
    if var10.get() == 1:
        txtCafeFrappucino.configure(state=NORMAL)
    elif var10.get() == 0:
        txtCafeFrappucino.configure(state=DISABLED)
        var_CafeFrappucino.set('0')
    if var11.get() == 1:
        txtCaramelMaciato.configure(state=NORMAL)
    elif var11.get() == 0:
        txtCaramelMaciato.configure(state=DISABLED)
        var_CaramelMaciato.set('0')


input_frame = Frame(window, bg='#EBD2EE', width=1350, height=100, bd=14, relief='raise')
input_frame.pack(side=TOP)

frame1 = Frame(window, bg='#EBD2EE', width=900, height=650, bd=8, relief='raise')
frame1.pack(side=LEFT)

frame2 = Frame(window,  bg='#EBD2EE', width=440, height=650, bd=8, relief='raise')
frame2.pack(side=RIGHT)

frame1a = Frame(frame1, bg='#EBD2EE', width=900, height=330, bd=8, relief='raise')
frame1a.pack(side=TOP)

frame2a = Frame(frame1, bg='#EBD2EE', width=100, height=100, bd=6, relief='raise')
frame2a.pack(side=BOTTOM)

frame1HotDrinks = Frame(frame1a, bg='#EBD2EE', width=500, height=650, bd=16, relief='raise')
frame1HotDrinks.pack(side=LEFT)

frame1ColdDrinks = Frame(frame1a, bg='#EBD2EE', width=500, height=650, bd=16, relief='raise')
frame1ColdDrinks.pack(side=RIGHT)

frame2Receipt = Frame(frame2, bg='#EBD2EE', width=440, height=450, bd=12, relief='raise')
frame2Receipt.pack(side=TOP)

frame2Total = Frame(frame2, bg='#EBD2EE', width=440, height=250, bd=12, relief='raise')
frame2Total.pack(side=BOTTOM)

title = Label(input_frame, font=('arial', 50, 'bold',), bg='#D0B9D3', text='Coffe Shop Management System', fg='#F9F7F7', bd=10)
title.grid(row=0, column=0)

var0 = IntVar()
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()

var_Latte = StringVar()
var_Irish = StringVar()
var_Espresso = StringVar()
var_Cappucciono = StringVar()
var_Americano = StringVar()
var_Mocaccino = StringVar()
var_IcedLatte = StringVar()
var_Mocha = StringVar()
var_IcedCoffee = StringVar()
var_BubbleTea = StringVar()
var_CafeFrappucino = StringVar()
var_CaramelMaciato = StringVar()

var_Latte.set('0')
var_Irish.set('0')
var_Espresso.set('0')
var_Cappucciono.set('0')
var_Americano.set('0')
var_Mocaccino.set('0')
var_IcedLatte.set('0')
var_Mocha.set('0')
var_IcedCoffee.set('0')
var_BubbleTea.set('0')
var_CafeFrappucino.set('0')
var_CaramelMaciato.set('0')

# ---------------HotDrinks-------------
Latte = Checkbutton(frame1HotDrinks, text='Latte \t', variable=var0, onvalue=1, offvalue=0,
                    font=('arial', 20, 'bold'), bg='#EBD2EE', command=checkbutton)
Latte.grid(row=0, sticky=W)
txtLatte = Entry(frame1HotDrinks, font=('arial', 12, 'bold'), bd=5, width=6, justify='left', textvariable=var_Latte,
                 state=DISABLED)
txtLatte.grid(row=0, column=1)

Irish = Checkbutton(frame1HotDrinks, text='Irish \t', variable=var1, onvalue=1, offvalue=0,
                    font=('arial', 20, 'bold'), bg='#EBD2EE', command=checkbutton)
Irish.grid(row=1, sticky=W)
txtIrish = Entry(frame1HotDrinks, font=('arial', 12, 'bold'), bd=5, width=6, justify='left', textvariable=var_Irish,
                 state=DISABLED)
txtIrish.grid(row=1, column=1)

Espresso = Checkbutton(frame1HotDrinks, text='Espresso \t', variable=var2, onvalue=1, offvalue=0,
                       font=('arial', 20, 'bold'), bg='#EBD2EE', command=checkbutton)
Espresso.grid(row=2, sticky=W)
txtEspresso = Entry(frame1HotDrinks, font=('arial', 12, 'bold'), bd=5, width=6, justify='left',
                    textvariable=var_Espresso, state=DISABLED)
txtEspresso.grid(row=2, column=1)

Cappucciono = Checkbutton(frame1HotDrinks, text='Cappuccino \t', variable=var3, onvalue=1, offvalue=0,
                          font=('arial', 20, 'bold'), bg='#EBD2EE', command=checkbutton)
Cappucciono.grid(row=3, sticky=W)
txtCappucciono = Entry(frame1HotDrinks, font=('arial', 12, 'bold'), bd=5, width=6, justify='left', textvariable=var_Cappucciono, state=DISABLED)
txtCappucciono.grid(row=3, column=1)

Americano = Checkbutton(frame1HotDrinks, text='Americano \t', variable=var4, onvalue=1, offvalue=0,
                        font=('arial', 20, 'bold'), bg='#EBD2EE', command=checkbutton)
Americano.grid(row=4, sticky=W)
txtAmericano = Entry(frame1HotDrinks, font=('arial', 12, 'bold'), bd=5, width=6, justify='left',
                     textvariable=var_Americano, state=DISABLED)
txtAmericano.grid(row=4, column=1)

Mocaccino = Checkbutton(frame1HotDrinks, text='Mocaccino \t', variable=var5, onvalue=1, offvalue=0,
                        font=('arial', 20, 'bold'), bg='#EBD2EE', command=checkbutton)
Mocaccino.grid(row=5, sticky=W)
txtMocaccino = Entry(frame1HotDrinks, font=('arial', 12, 'bold'), bd=5, width=6, justify='left',
                     textvariable=var_Mocaccino, state=DISABLED)
txtMocaccino.grid(row=5, column=1)

# ----------ColdDrinks------
IcedLatte = Checkbutton(frame1ColdDrinks, text='Iced Latte \t', variable=var6, onvalue=1, offvalue=0,
                        font=('arial', 20, 'bold'), bg='#EBD2EE', command=checkbutton)
IcedLatte.grid(row=0, sticky=W)
txtIcedLatte = Entry(frame1ColdDrinks, font=('arial', 12, 'bold'), bd=5, width=6, justify='left',
                     textvariable=var_IcedLatte, state=DISABLED)
txtIcedLatte.grid(row=0, column=1)

Mocha = Checkbutton(frame1ColdDrinks, text='Mocha \t', variable=var7, onvalue=1, offvalue=0,
                    font=('arial', 20, 'bold'), bg='#EBD2EE', command=checkbutton)
Mocha.grid(row=1, sticky=W)
txtMocha = Entry(frame1ColdDrinks, font=('arial', 12, 'bold'), bd=5, width=6, justify='left', textvariable=var_Mocha,
                 state=DISABLED)
txtMocha.grid(row=1, column=1)

IcedCoffee = Checkbutton(frame1ColdDrinks, text='Iced Coffee \t', variable=var8, onvalue=1, offvalue=0,
                         font=('arial', 20, 'bold'), bg='#EBD2EE', command=checkbutton)
IcedCoffee.grid(row=2, sticky=W)
txtIcedCoffee = Entry(frame1ColdDrinks, font=('arial', 12, 'bold'), bd=5, width=6, justify='left',
                      textvariable=var_IcedCoffee, state=DISABLED)
txtIcedCoffee.grid(row=2, column=1)

BubbleTea = Checkbutton(frame1ColdDrinks, text='Bubble Tea \t', variable=var9, onvalue=1, offvalue=0,
                        font=('arial', 20, 'bold'), bg='#EBD2EE', command=checkbutton)
BubbleTea.grid(row=3, sticky=W)
txtBubbleTea = Entry(frame1ColdDrinks, font=('arial', 12, 'bold'), bd=5, width=6, justify='left',
                     textvariable=var_BubbleTea, state=DISABLED)
txtBubbleTea.grid(row=3, column=1)

CafeFrappucino = Checkbutton(frame1ColdDrinks, text='Cafe Frappucino \t', variable=var10, onvalue=1, offvalue=0,
                             font=('arial', 20, 'bold'), bg='#EBD2EE', command=checkbutton)
CafeFrappucino.grid(row=4, sticky=W)
txtCafeFrappucino = Entry(frame1ColdDrinks, font=('arial', 12, 'bold'), bd=5, width=6, justify='left',
                          textvariable=var_CafeFrappucino, state=DISABLED)
txtCafeFrappucino.grid(row=4, column=1)

CaramelMaciato = Checkbutton(frame1ColdDrinks, text='Caramel Maciato \t', variable=var11, onvalue=1, offvalue=0,
                             font=('arial', 20, 'bold'), bg='#EBD2EE', command=checkbutton)
CaramelMaciato.grid(row=5, sticky=W)
txtCaramelMaciato = Entry(frame1ColdDrinks, font=('arial', 12, 'bold'), bd=5, width=6, justify='left',
                          textvariable=var_CaramelMaciato, state=DISABLED)
txtCaramelMaciato.grid(row=5, column=1)

# information
label_Receipt = Label(frame2Receipt, font=('arial', 12, 'bold'), text='Receipt', bg='#EBD2EE', bd=2)
label_Receipt.grid(row=0, column=0, sticky=W)
txtReceipt = Text(frame2Receipt, width=59, height=22, bg='#EBD2EE', bd=8, font=('arial', 11, 'bold'))
txtReceipt.grid(row=1, column=0)

# button
button_Total = Button(frame2Total, padx=16, pady=1, bd=4, bg='#9BEE97',  fg='black', font=('arial', 16, 'bold'), width=5, text='Total', command=CostOfItem)
button_Total.grid(row=0, column=0)

button_Reset = Button(frame2Total, padx=16, pady=1, bd=4, bg='#E9DD8C', fg='black', font=('arial', 16, 'bold'), width=5, text='Reset', command=f_Reset)
button_Reset.grid(row=0, column=1)

button_Exit = Button(frame2Total, padx=16, pady=1, bd=4, bg='#E07E6D', fg='black', font=('arial', 16, 'bold'), width=5, text='Exit',
                     command=f_Exit)
button_Exit.grid(row=0, column=2)
button_Receipt = Button(frame2a, padx=16, pady=1, bd=4, bg='#E9DD8C', fg='black', font=('arial', 16, 'bold'), width=5, text='Receipt', command=f_receipt)
button_Receipt.grid(row=1, column=0)

# cost
label_TotalCost = Label(frame2a, font=('arial', 16, 'bold'), text='TOTAL COST', bg='#EBD2EE')
label_TotalCost.grid(row=3, column=0, sticky=W)
txtTotalCost = Entry(frame2a, font=('arial', 16, 'bold'), bg='#EBD2EE', bd=8, textvariable=TotalCost)
txtTotalCost.grid(row=4, column=0, sticky=W)

window.mainloop()
