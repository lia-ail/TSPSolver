import customtkinter
import tkinter as tk
import operator



def calc(root, is_calc):
    if is_calc:
        def on_calc_close():
            nonlocal is_calc
            nonlocal calc_window
            is_calc -= 1
            calc_window.destroy()

        def percentage(hpv, pv):
            return (hpv/pv)*100

        def p1():
            calcarea.insert(tk.END, '1')

        def p2():
            calcarea.insert(tk.END, '2')

        def p3():
            calcarea.insert(tk.END, '3')

        def p4():
            calcarea.insert(tk.END, '4')

        def p5():
            calcarea.insert(tk.END, '5')

        def p6():
            calcarea.insert(tk.END, '6')

        def p7():
            calcarea.insert(tk.END, '7')

        def p8():
            calcarea.insert(tk.END, '8')

        def p9():
            calcarea.insert(tk.END, '9')

        def p0():
            calcarea.insert(tk.END, '0')

        def plus():
            if calcarea.get('end-2c') in '+-*/%':
                calcarea.delete('end-2c')
                calcarea.insert(tk.END, '+')
            else:
                calcarea.insert(tk.END, '+')

        def minus():
            if calcarea.get('end-2c') in '+-*/%':
                calcarea.delete('end-2c')
                calcarea.insert(tk.END, '-')
            else:
                calcarea.insert(tk.END, '-')

        def mult():
            if calcarea.get('end-2c') in '+-*/%':
                calcarea.delete('end-2c')
                calcarea.insert(tk.END, '*')
            else:
                calcarea.insert(tk.END, '*')

        def div():
            if calcarea.get('end-2c') in '+-*/%':
                calcarea.delete('end-2c')
                calcarea.insert(tk.END, '/')
            else:
                calcarea.insert(tk.END, '/')

        def c():
            calcarea.delete('1.0', 'end')

        def parl():
            calcarea.insert(tk.END, '(')

        def parr():
            calcarea.insert(tk.END, ')')

        def dot():
            calcarea.insert(tk.END, '.')

        def percsym():
            if calcarea.get('end-2c') in '+-*/%':
                calcarea.delete('end-2c')
                calcarea.insert(tk.END, '%')
            else:
                calcarea.insert(tk.END, '%')

        def backsp():
            calcarea.delete('end-2c')

        def eqv():
            expr = calcarea.get('1.0', tk.END)
            ops = {'+' : (operator.add, 0), '-' : (operator.sub, 0), '*' : (operator.mul, 1), '/' : (operator.truediv, 1),
                   '%' : (percentage, 1)}
            stack, opst, pars = [], [], []
            num = ''
            isneg = False
            for ch in expr:
                if ch.isdecimal() or ch == '.':
                    num = num + ch
                elif ch in ops:
                    if (ch == '-' and expr.index(ch) == 0) or (ch == '-' and pars[-1] == '(' and not num):
                        isneg = True
                    else:
                        if pars:
                            pars.append(ch)
                        else:
                            if num:
                                if isneg:
                                    num = '-' + num
                                    isneg = False
                                stack.append(num)
                                num = ''
                            while opst and ops[ch][1] <= ops[opst[-1]][1]:
                                stack.append(opst.pop(-1))
                            opst.append(ch)
                    if num:
                        if isneg:
                            num = '-' + num
                            isneg = False
                        stack.append(num)
                        num = ''
                elif ch == '(':
                    pars.append(ch)
                elif ch == ')':
                    if num:
                        if isneg:
                            num = '-' + num
                            stack.append(num)
                            num = ''
                            isneg = False
                        else:
                            stack.append(num)
                            num = ''
                    while pars[-1] != '(':
                        stack.append(pars.pop(-1))
                    pars.pop(-1)
            if num:
                if isneg:
                    num = '-' + num
                    stack.append(num)
                else:
                    stack.append(num)
            stack.extend(list(reversed(opst)))
            res = []
            for i in stack:
                if i not in ops:
                    res.append(float(i))
                else:
                    res.append(ops[i][0](res.pop(-2), res.pop(-1)))
            calcarea.delete('1.0', "end")
            calcarea.insert(tk.END, res[0])

        calc_window = customtkinter.CTkToplevel(root)
        calc_window.geometry('220x275')
        calc_window.title('Calculator')
        calc_window.attributes('-topmost', True)
        for i in range(5):
            calc_window.columnconfigure(i, weight=1)
        calc_window.rowconfigure(0, weight=2)
        for i in range(1, 7):
            calc_window.columnconfigure(i, weight=1)
        calcarea = customtkinter.CTkTextbox(calc_window, width=200, height=40)
        calcarea.grid(column=0, row=0, columnspan=5)
        mc = customtkinter.CTkButton(calc_window, text="<--", width=20, command=backsp)
        mc.grid(column=0, row=1)
        mr = customtkinter.CTkButton(calc_window, text="CE", width=20)
        mr.grid(column=1, row=1)
        ms = customtkinter.CTkButton(calc_window, text="C", width=20, command=c)
        ms.grid(column=2, row=1)
        mpl = customtkinter.CTkButton(calc_window, text="(", width=20, command=parl)
        mpl.grid(column=3, row=1)
        mmin = customtkinter.CTkButton(calc_window, text=")", width=20, command=parr)
        mmin.grid(column=4, row=1)
        b7 = customtkinter.CTkButton(calc_window, text="7", width=30, command=p7)
        b7.grid(column=0, row=2)
        b8 = customtkinter.CTkButton(calc_window, text="8", width=30, command=p8)
        b8.grid(column=1, row=2)
        b9 = customtkinter.CTkButton(calc_window, text="9", width=30, command=p9)
        b9.grid(column=2, row=2)
        bdivis = customtkinter.CTkButton(calc_window, text="/", width=30, command=div)
        bdivis.grid(column=3, row=2)
        bproc = customtkinter.CTkButton(calc_window, text="%", width=30, command=percsym)
        bproc.grid(column=4, row=2)
        b4 = customtkinter.CTkButton(calc_window, text="4", width=30, command=p4)
        b4.grid(column=0, row=3)
        b5 = customtkinter.CTkButton(calc_window, text="5", width=30, command=p5)
        b5.grid(column=1, row=3)
        b6 = customtkinter.CTkButton(calc_window, text="6", width=30, command=p6)
        b6.grid(column=2, row=3)
        mult = customtkinter.CTkButton(calc_window, text="*", width=30, command=mult)
        mult.grid(column=3, row=3)
        dbo = customtkinter.CTkButton(calc_window, text="1/x", width=30)
        dbo.grid(column=4, row=3)
        b1 = customtkinter.CTkButton(calc_window, text="1", width=30, command=p1)
        b1.grid(column=0, row=4)
        b2 = customtkinter.CTkButton(calc_window, text="2", width=30, command=p2)
        b2.grid(column=1, row=4)
        b3 = customtkinter.CTkButton(calc_window, text="3", width=30, command=p3)
        b3.grid(column=2, row=4)
        minus = customtkinter.CTkButton(calc_window, text="-", width=30, command=minus)
        minus.grid(column=3, row=4)
        eqv = customtkinter.CTkButton(calc_window, text="=", width=30, height=70, command=eqv)
        eqv.grid(column=4, row=4, rowspan=2)
        b0 = customtkinter.CTkButton(calc_window, text="0", width=80, command=p0)
        b0.grid(column=0, row=5, columnspan=2)
        coma = customtkinter.CTkButton(calc_window, text=".", width=30, command=dot)
        coma.grid(column=2, row=5)
        plus = customtkinter.CTkButton(calc_window, text="+", width=30, command=plus)
        plus.grid(column=3, row=5)
        is_calc = False
        calc_window.protocol("WM_DELETE_WINDOW", on_calc_close)