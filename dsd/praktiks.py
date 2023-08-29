import six
import sys
sys.modules['sklearn.externals.six'] = six
import sklearn
from mlrose import TravellingSales, TSPOpt, genetic_alg

import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox
from PIL import Image
import operator
import customtkinter
import pandas as pd
from itertools import permutations


def read_from_file1(path):
    if path.split('\\')[-1].split('.')[-1] == 'xlsx':
        data = pd.read_excel(path, header=None)
    elif path.split('\\')[-1].split('.')[-1] == 'csv':
        data = pd.read_csv(path, header=None)
    return data


def solving_tsp1(D):
    if len(list(D.columns)) == len(list(D.index)):
        names = list(D.columns)
    else:
        names = ['City' + str(i) for i in D.shape[0]]

    dat = []

    for i in range(len(D.iloc[0])):
        for j in range(len(D.iloc[0])-1):
            if i != j:
                dat.append((i, j, D.iloc[i, j]))

    fitn_dist = TravellingSales(distances=dat)

    problem_fit = TSPOpt(length=len(D), fitness_fn=fitn_dist, maximize=opt_value.get() == 'Maximize income')

    bs, bf = genetic_alg(problem_fit, random_state=2)

    return names[bs[-1]] + ' '.join([names[i] for i in bs]), bf


def solving_tsp2(D, s):
    if len(list(D.columns)) == len(list(D.index)):
        names = list(D.columns)
    else:
        names = ['City' + str(i) for i in D.shape[0]]

    bul_func = operator.gt if opt_value.get() == "Maximize income" else operator.lt
    V = len(D)
    vertex = []
    for i in range(V):
        if i != s:
            vertex.append(i)
    min_cost = 0
    next_permutation = permutations(vertex)
    best_perm = next_permutation.__next__()
    k = s
    for j in best_perm:
        min_cost += D[D.columns[k]].iloc[j]
        k = j
    for i in next_permutation:
        current_cost = 0
        k = s
        for j in i:
            current_cost += D[D.columns[k]][j]
            k = j
        current_cost += D[D.columns[k]][s]
        if bul_func(current_cost, min_cost):
            min_cost = current_cost
            best_perm = i

    return names[s] + ' '.join([names[i] for i in best_perm]) + names[s], min_cost


def solving_tsp3(D, s):
    if len(list(D.columns)) == len(list(D.index)):
        names = list(D.columns)
    else:
        names = ['City' + str(i) for i in D.shape[0]]

    num_cities = D.shape[0]
    visited = [False] * num_cities
    route = []
    current_city = s
    total_distance = 0
    bul_func = operator.gt if opt_value.get() == "Maximize income" else operator.lt


    route.append(current_city)
    visited[current_city] = True

    for _ in range(num_cities - 1):
        nearest_city = None
        min_distance = sys.maxsize * 1 - 2*(bul_func == operator.gt)

        for next_city in range(num_cities):
            if not visited[next_city] and bul_func(D[D.columns[current_city]][next_city], min_distance):
                nearest_city = next_city
                min_distance = D[D.columns[current_city]][next_city]

        current_city = nearest_city
        route.append(current_city)
        visited[current_city] = True
        total_distance += min_distance

    route.append(s)
    total_distance += D[D.columns[current_city]][s]

    return ' '.join([names[i] for i in route]), total_distance


customtkinter.set_appearance_mode('system')
customtkinter.set_default_color_theme('blue')

root = customtkinter.CTk()
root.geometry('700x700')
root.title('Transport Salesman Problem')
root.resizable(False, False)
for i in range(4):
    root.columnconfigure(i, weight=(1 if i != 1 else 2))
for j in range(3):
    root.rowconfigure(j, weight=1)

dp = 0

is_calc_closed = True
def calc():
    global is_calc_closed
    if is_calc_closed:
        def on_calc_close():
            global is_calc_closed
            nonlocal calc_window
            is_calc_closed = True
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
        is_calc_closed = False
        calc_window.protocol("WM_DELETE_WINDOW", on_calc_close)


def select_file():
    try:
        global dp
        filetypes = (
            ('Excel files', '*.xlsx'),
            ('CSV files', '*.csv*')
        )

        filename = fd.askopenfilename(
            title='Open a file',
            initialdir='/',
            filetypes=filetypes)
        txtarea.delete("1.0","end")
        dp = read_from_file1(filename)
        if len(dp.columns) == len(dp.index):
            dp.columns = ['City'+str(i+1) for i in range(len(dp.columns))]
            dp.index = dp.columns
        else:
            new_cols = list(dp.iloc[0])
            dp.columns = new_cols
            dp = pd.DataFrame(dp.iloc[1:], columns=new_cols)
            dp.index = dp.columns
            for col in dp.columns:
                dp[col] = pd.to_numeric(dp[col])
        txtarea.insert(tk.END, dp.fillna('').to_string())
        l1.configure(text='Optimal amount:')
    except UnboundLocalError:
        pass


out = ''


def solve():
    global out
    try:
        if alg_value.get() == 'mlrose algorithm':
            res = solving_tsp1(dp)
            txtarea.insert(tk.END, '\n Results \n')
            txtarea.insert(tk.END, res[0])
            l1.configure(text=str(res[1]) + ' ' + curr_value.get())
            out = res[0]
        elif alg_value.get() == 'Simple approach':
            try:
                res = solving_tsp2(dp, int(s_area.get())-1)
                txtarea.insert(tk.END, '\n Results \n')
                txtarea.insert(tk.END, res[0])
                l1.configure(text=str(res[1]) + ' ' + curr_value.get())
                out = res[0]
            except (ValueError, IndexError):
                messagebox.showerror("Error", "Incorrect value of number of cities.Please input number in bounds of matrix length")
        elif alg_value.get() == 'Greedy algorithm':
            try:
                res = solving_tsp2(dp, int(s_area.get()) - 1)
                txtarea.insert(tk.END, '\n Results \n')
                txtarea.insert(tk.END, res[0])
                l1.configure(text=str(res[1]) + ' ' + curr_value.get())
                out = res[0]
            except (ValueError, IndexError):
                messagebox.showerror("Error", "Incorrect value of number of cities.Please input number in bounds of matrix length")
    except AttributeError:
        messagebox.showerror("Error", "Nothing to solve yet. Please input or import data and try again.")


def save():
    global out
    if out:
        files = [('All files', '*.*'),
                 ('Text files', '*.txt'), ]
        fl = fd.asksaveasfile(filetypes=files, defaultextension=files)
        try:
            fl.write(out)
            fl.close()
            messagebox.showinfo("Saving", "Successfully saved !")
        except AttributeError:
            pass
    else:
        messagebox.showwarning("Save warning", "You don't have proceeded output yet. Please try again after solving procedure")

is_closed = True
def create_table():
    global is_closed
    if is_closed:
        numofm = []
        numofs = []
        values = []
        def create_table2():
            nonlocal numofs, numofm, values
            try:
                if (numofs != []) or (numofs != []) or (values != []):
                    clear()
                if int(e1.get()) > 5:
                    messagebox.showwarning('Warning',
                                           'Please, change number of values or import files to proceed large data',
                                           parent=window)
                elif int(e1.get()) <= 0:
                    messagebox.showerror('Error',
                                           'Incorrect number of cities, please change and try again.',
                                           parent=window)
                else:
                    numofm = ['' for _ in range(int(e1.get()))]
                    numofs = ['' for _ in range(int(e1.get()))]
                    for i in range(int(e1.get())):
                        numofm[i] = customtkinter.CTkLabel(window, text='City' + str(i + 1))
                        numofm[i].grid(row=3, column=i + 1)
                    for j in range(int(e1.get())):
                        numofs[j] = customtkinter.CTkLabel(window, text='City' + str(j + 1))
                        numofs[j].grid(row=j + 4, column=0)
                    values = [['' for i in range(int(e1.get()))] for j in range(int(e1.get()))]
                    for i in range(int(e1.get())):
                        for j in range(int(e1.get())):
                            values[j][i] = customtkinter.CTkEntry(window)
                            values[j][i].grid(row=j + 4, column=i + 1)
            except:
                messagebox.showwarning('Warning', 'Incorrect input, please try again', parent=window)

        def clear():
            nonlocal numofm, numofs, values
            for i in numofm:
                i.destroy()
            for j in numofs:
                j.destroy()
            for i in values:
                for j in i:
                    j.destroy()
            numofs, numofm, values = [], [], []


        def done():
            global dp, is_closed
            nonlocal numofm, numofs, values
            try:
                res = [[] for _ in range(len(numofs))]
                for i in range(len(values)):
                    for j in values[i]:
                        res[i].append(int(j.get()))
                cl = ['City' + str(i+1) for i in range(len(numofm))]
                rws = ['City' + str(j+1) for j in range(len(numofs))]
                dp = pd.DataFrame(data=res, columns=cl, index=rws)
                if len(dp) != 0:
                    txtarea.delete("1.0","end")
                    txtarea.insert(tk.END, dp.to_string())
                    window.destroy()
                    is_closed = True
                else:
                    an = messagebox.askyesno("Exit", "You have not input any value. Do you want to quit ?")
                    if an:
                        window.destroy()
                        is_closed = True
            except ValueError:
                messagebox.showerror('Error', 'Incorrect input. Please, fill all of the cells and try again.', parent=window)


        def on_close():
            global is_closed
            nonlocal window
            is_closed = True
            window.destroy()


        window = customtkinter.CTkToplevel(root)
        window.geometry('800x400')
        window.title('Create table')
        window.attributes('-topmost', True)

        label3 = customtkinter.CTkLabel(window, text='Please enter numbers of cities (less or equal to 5)')
        label3.place(relx=0.1, rely=0.7)
        nofc = customtkinter.CTkLabel(window, text='Number of cities:')
        nofc.place(relx=0.1, rely=0.8)
        e1 = customtkinter.CTkEntry(window)
        e1.place(relx=0.25, rely=0.8)

        crt = customtkinter.CTkButton(window, text='Create table', command=create_table2)
        crt.place(relx=0.45, rely=0.9)

        clr = customtkinter.CTkButton(window, text='Clear', command=clear)
        clr.place(relx=0.1, rely=0.9)

        dnn = customtkinter.CTkButton(window, text='Done', command=done)
        dnn.place(relx=0.8, rely=0.9)
        is_closed = False
        window.protocol("WM_DELETE_WINDOW", on_close)




txtarea = customtkinter.CTkTextbox(root, width=500, height=200)
txtarea.grid(column=0, row=0, columnspan=4)
l1 = customtkinter.CTkLabel(root, text='Optimal amount:')
l1.grid(column=3, row=1)
l2 = customtkinter.CTkLabel(root, text='Currency:')
l2.grid(column=1, row=1)
l3 = customtkinter.CTkLabel(root, text='Which city or node is initial (number of city):')
l3.place(x=100, y=325)
s_area = customtkinter.CTkEntry(root, width=50, height=20)
s_area.place(x=350, y=325)
l4 = customtkinter.CTkLabel(root, text="(Doesn't work with mlrose algorithm)")
l4.place(x=450, y=325)
curr_list = ['UAH', 'USD', 'EUR']
curr_value = customtkinter.StringVar(root)
curr_value.set('UAH')

curr_menu = customtkinter.CTkOptionMenu(master=root, variable=curr_value, values=curr_list)
curr_menu.grid(column=2, row=1)

opt_list = ['Maximize income', 'Minimize expenses']
opt_value = customtkinter.StringVar(root)
opt_value.set('Maximize income')

alg_list = ['mlrose algorithm', 'Greedy algorithm', 'Simple approach']
alg_value = customtkinter.StringVar(root)
alg_value.set('mlrose algorithm')

alg_menu = customtkinter.CTkOptionMenu(master=root, variable=alg_value, values=alg_list)
alg_menu.place(x=500, y=0)

opt_menu = customtkinter.CTkOptionMenu(master=root, variable=opt_value, values=opt_list)
opt_menu.grid(column=0, row=1)
# open button
open_button = customtkinter.CTkButton(
    root,
    text='Open a File',
    command=select_file
)

solve_button = customtkinter.CTkButton(
    root,
    text='Solve',
    command=solve
)

ti_button = customtkinter.CTkButton(
    root,
    text='Create table',
    command=create_table
)

save_button = customtkinter.CTkButton(
    root,
    text='Save',
    command=save
)

imgcalc = customtkinter.CTkImage(light_image=Image.open("vector-calculator-icon.jpg"), size=(30, 30))
calc_button = customtkinter.CTkButton(root, image=imgcalc, text="Calculator", command=calc)

calc_button.place(x=0, y=0)
ti_button.grid(column=0, row=2)
open_button.grid(column=1, row=2)
solve_button.grid(column=2, row=2)
save_button.grid(column=3, row=2)

root.mainloop()
