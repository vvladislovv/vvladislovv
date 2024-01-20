from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
def chenge_theme(theme):
    text_fild['bg'] = view_colors[theme]['text_bg']
    text_fild['fg'] = view_colors[theme]['text_fg']
    text_fild['insertbackground'] = view_colors[theme]['cursor']
    text_fild['selectbackground'] = view_colors[theme]['select_bg']


def chenge_fonts(fontser):
    text_fild['font'] = fonts[fontser]['font']


def notepad_exit():
    answer = messagebox.askokcancel('Exit','Do you want to get out?')

    if answer:
        root.destroy()
        
def open_file():
    file_path = filedialog.askopenfilename(title='Find file', filetypes=(('Text document(*.txt)','*.txt'), ('All file','*.*')))        
    if file_path:
        text_fild.delete('1.0', END)
        text_fild.insert('1.0', open(file_path, encoding='utf-8').read())

def save_file():
    file_path = filedialog.asksaveasfile(filetypes=(('Text document(*.txt)','*.txt'), ('All file','*.*')))
    f = open(file_path, 'w', encoding='utf-8')
    text = text_fild.get('1.0', END)
    f.write(text)
    f.close()

root = Tk()
root.title('Текстовый редактор')
root.geometry('600x700')
#root.iconbitmap('')

main_menu = Menu(root)
root.config(menu=main_menu)

#File

file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label='Open', command=open_file)
file_menu.add_command(label='Save', command=save_file)
file_menu.add_separator()
file_menu.add_command(label='Close', command=notepad_exit)
root.config(menu=file_menu)

#View
view_menu = Menu(main_menu, tearoff=0)
view_menu_sub = Menu(view_menu, tearoff=0)
font_menu_sub = Menu(view_menu, tearoff=0)
view_menu_sub.add_command(label='Black', command=lambda: chenge_theme('Dark'))
view_menu_sub.add_command(label='Lite', command=lambda: chenge_theme('Lite'))
view_menu.add_cascade(label='Thream', menu=view_menu_sub)

#Font
font_menu_sub.add_command(label='Arial',command=lambda: chenge_fonts('Arial'))
font_menu_sub.add_command(label='Comic Sans MS',command=lambda: chenge_fonts('CSMS'))
font_menu_sub.add_command(label='Times New Roman',command=lambda: chenge_fonts('TNR'))
view_menu.add_cascade(label='Font', menu=font_menu_sub)
root.config(menu=view_menu)


# Add list menu
main_menu.add_cascade(label='File', menu=file_menu)
main_menu.add_cascade(label='View', menu=view_menu)
root.config(menu=main_menu)


f_text = Frame(root)
f_text.pack(fill=BOTH, expand=1)

view_colors = {
    'Dark': {
        'text_bg': 'Black', 
        'text_fg': 'White', 
        'cursor': 'White', 
        'select_bg': '#adc0de'
    },
    'Lite': {
        'text_bg': 'White',
        'text_fg': 'Black', 
        'cursor': 'Black', 
        'select_bg': '#adc0de'
    }
}
fonts = {
     'Arial': {
         'font':'Arial 12 bold'
     },
     'CSMS': {
         'font':('Comic Sans MS', 12,'bold')
     },
     'TNR': {
         'font':('Times New Romans',12,'bold')
     },
 }   
    
    


text_fild = Text(f_text, 
                 bg='White', 
                 fg='Black', 
                 padx=5, pady=5, 
                 wrap=WORD, 
                 insertbackground='#f59aa8',
                 selectbackground='#adc0de',
                 spacing3=1.5, 
                 width=30,
                 font='Arial 12 bold'
                 ) # темы + цвет текста

text_fild.pack(expand=1, 
               fill=BOTH, 
               side='left')

scroll = Scrollbar(f_text, command=text_fild.yview)
scroll.pack(side=LEFT,fill=Y)
text_fild.config(yscrollcommand=scroll.set)

root.mainloop()