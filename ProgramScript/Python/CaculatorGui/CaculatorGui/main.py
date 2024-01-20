from tkinter import *

window = Tk()
window.title('Caculator Beta')
window.geometry('400x400')

def math_input(symbol):
    entry.insert(END, symbol)

def clear():
   entry.delete(0,END)

def count_result():
    text = entry.get()
    result = 0
    if '+' in text:
        splitted = text.split('+')
        first = float(splitted[0])
        second = float(splitted[0])
        result = first+second
    elif '-' in text:
        splitted = text.split('-')
        first = float(splitted[0])
        second = float(splitted[0])
        result = first-second
    elif '*' in text:
        splitted = text.split('*')
        first = float(splitted[0])
        second = float(splitted[0])
        result = first*second
    elif '/' in text:
        splitted = text.split('/')
        first = float(splitted[0])
        second = float(splitted[0])
        result = first/second
    elif result >= 0:
        result
        
    clear()
    entry.insert(0, result)
entry = Entry(window, width=17, font=('',20))
entry.place(x = 50, y = 60)


# основные кнопки 
bnt0 = Button(window, bg='black', fg='white', text='0', command=lambda : math_input('0'))
bnt0.place(x=50,y=100, width=50, height=50)

bnt1 = Button(window, bg='black', fg='white', text='1', command=lambda : math_input('1'))
bnt1.place(x=100,y=100, width=50, height=50)

bnt2 = Button(window, bg='black', fg='white', text='2',command=lambda : math_input('2'))
bnt2.place(x=150,y=100, width=50, height=50)

bnt3 = Button(window, bg='black', fg='white', text='3', command=lambda : math_input('3'))
bnt3.place(x=200,y=100, width=50, height=50)

bnt4 = Button(window, bg='black', fg='white', text='4', command=lambda : math_input('4'))
bnt4.place(x=100,y=150, width=50, height=50)

bnt5 = Button(window, bg='black', fg='white', text='5', command=lambda : math_input('5'))
bnt5.place(x=150,y=150, width=50, height=50)

bnt6 = Button(window, bg='black', fg='white', text='6', command=lambda : math_input('6'))
bnt6.place(x=200,y=150, width=50, height=50)

bnt7 = Button(window, bg='black', fg='white', text='7', command=lambda : math_input('7'))
bnt7.place(x=100,y=200, width=50, height=50)

bnt8 = Button(window, bg='black', fg='white', text='8', command=lambda : math_input('8'))
bnt8.place(x=150,y=200, width=50, height=50)

bnt9 = Button(window, bg='black', fg='white', text='9', command=lambda : math_input('9'))
bnt9.place(x=200,y=200, width=50, height=50)

# Дополнительные кнопки 
bntPLC = Button(window, bg='black', fg='white', text='+', command=lambda : math_input('+'))
bntPLC.place(x=250,y=100, width=50, height=50)

bntMIS = Button(window, bg='black', fg='white', text='-', command=lambda : math_input('-'))
bntMIS.place(x=250,y=150, width=50, height=50)

bntPLCK = Button(window, bg='black', fg='white', text='/', command=lambda : math_input('/'))
bntPLCK.place(x=250,y=200, width=50, height=50)

bntEMN = Button(window, bg='black', fg='white', text='*', command=lambda : math_input('*'))
bntEMN.place(x=250,y=250, width=50, height=50)

bntTOX = Button(window, bg='black', fg='white', text='.', command=lambda : math_input('.'))
bntTOX.place(x=100,y=250, width=50, height=50)

bntPLCK = Button(window, bg='black', fg='white', text='CE', command = clear)
bntPLCK.place(x=150,y=250, width=50, height=50)

bntRav = Button(window, bg='black', fg='white', text='=', command=count_result)
bntRav.place(x=200,y=250, width=50, height=50)

window.mainloop()