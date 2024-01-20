
lang = 'EN'
lang_oper = input('Enter L to change lannguage or ither key to continue:')

while lang_oper == 'L': #Выбор языка 
    if lang == 'EN':
        lang = 'RU'
        lang_oper = input('Enter L to cahnge language or other key to continue')
    else:
        lang = 'RU' 
        lang_oper = input('Введите L, чтобы сменить язык или любую клавишу, чтобы продолжить:')

if lang == 'EN': # 
    f = 'Enter first Number'
    o = 'Enter operation (+,-,/,*)'
    s = 'Enter second number:'
    r = 'Result'
    e = "Error"
    v = 'Enter "yes" to continue and other key to finish'
    
if lang == 'RU':
    f = 'Введите первое число:  '
    o = 'Введите операцию (+,-, /, *):  '
    s = 'Введите второе число:  '
    r = 'Результат: '
    e = 'Ошибка'
    v = 'Введите "yes", чтобы продолжить, и любую клавишу, чтобы закончить:  '
back = 'yes'

while back == 'yes':
    f_num = float(input(f))
    opener = input(o)
    s_num = float(input(s))
    if opener == "+":
        print(r,f_num + s_num)
    elif opener == '-':
        print(r,f_num - s_num)
    elif opener == '*':
        print(r,f_num * s_num)
    elif opener == '/':
        print(r,f_num / s_num)
    else:
        print(e)
    opener = input(v)