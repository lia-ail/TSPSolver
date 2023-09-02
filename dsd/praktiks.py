import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox
from PIL import Image
import customtkinter
import pandas as pd
from dynamic_example import dynamic_solution
from nearest_neighbor import nearestn_solution
from calculator import calc


def read_from_file1(path):
    """
    Helper function to get user data from files of .xlsx or .csv types at given path.
    :param path: Path, which is used to open a file.
    :return: Returns pd.DataFrame from an opened file.
    """
    if path.split('\\')[-1].split('.')[-1] == 'xlsx':
        data = pd.read_excel(path, header=None)
    elif path.split('\\')[-1].split('.')[-1] == 'csv':
        data = pd.read_csv(path, header=None)
    return data


def select_file():
    """
    A function that is linked to "Select file" button. Cleans display area. Using previously defined helper function
    writes to the global variable "dp" a matrix. If there are any user-defined names,
    refactor matrix to correctly display them, else defines default names in format "City X".
    Inserts matrix into display area.
    """
    try:
        global dp

        """
        Opening file procedure:
        """
        filetypes = (
            ('Excel files', '*.xlsx'),
            ('CSV files', '*.csv*')
        )

        filename = fd.askopenfilename(
            title='Open a file',
            initialdir='/',
            filetypes=filetypes)
        txtarea.delete("1.0", "end")
        dp = read_from_file1(filename)

        """
        If the first value of our matrix is not a number or a string with a single whitespace 
        (dependent on from which file is matrix imported) then, it has named columns and rows,
        and we need to edit our matrix to work correctly. If statement above is not True, then we check if
        number of columns is greater than number of rows. In case previous condition is True,
        we edit matrix accordingly, else name matrix with default names:
        """
        if pd.isna(dp.iloc[0][0]) or dp.iloc[0][0] == ' ':
            """
            Saving names:
            """
            new_cols = list(dp.iloc[0][1:])

            """
            Recreating table without names in fields:
            """
            dp = pd.DataFrame(dp[dp.columns[1:]].iloc[1:])

            """
            Define names for columns and rows:
            """
            dp.columns = new_cols
            dp.index = dp.columns

            """
            Change type of columns to numeric type:
            """
            for col in dp.columns:
                dp[col] = pd.to_numeric(dp[col])
        elif len(dp.columns) > len(dp.index):
            """
            Saving names:
            """
            new_cols = list(dp.iloc[0])

            """
            Recreating table without names in fields:
            """
            dp.columns = new_cols
            dp = pd.DataFrame(dp.iloc[1:], columns=new_cols)

            """
            Define names for columns and rows:
            """
            dp.index = dp.columns

            """
            Change type of columns to numeric type:
            """
            for col in dp.columns:
                dp[col] = pd.to_numeric(dp[col])
        else:
            """
            Set default names:
            """
            dp.columns = ['City'+str(i+1) for i in range(len(dp.columns))]
            dp.index = dp.columns

        """
        Inserting edited matrix into display area:
        """
        txtarea.insert(tk.END, dp.fillna('').to_string())
        l1.configure(text='Optimal amount:')
    except UnboundLocalError:
        pass


def solve():
    """
    A function that is linked to the "Solve" button.
    Calls imported "Dynamic programming algorithm" or "Nearest neighbor algorithm",
    according to user-defined value in "opt_value" menu. Displays result in display area,
    writes to global variable "out" calculated result.
    """
    global out
    try:
        """
        Calling imported function:
        """
        if alg_value.get() == "Dynamic programming algorithm":
            res = dynamic_solution(dp, opt_value.get() == "Minimize expenses")
        else:
            res = nearestn_solution(dp, opt_value.get() == "Minimize expenses")

        """
        Inserting result route in display area:
        """
        txtarea.insert(tk.END, '\n Results \n')
        txtarea.insert(tk.END, res[0])

        """
        Inserting optimal value to the according "l1" label:
        """
        l1.configure(text=str(res[1]) + ' ' + curr_value.get())

        """
        Putting result route to the "out" global value:
        """
        out = res[0]
    except AttributeError:
        messagebox.showerror("Error", "Nothing to solve yet. Please input or import data and try again.")


def save():
    """
    A function that is linked to the "Save" button. Saves calculated result,
    which is stored in global variable "out", to user-defined text file.
    """
    global out
    if out:  # if result exists
        """
        List of supported file extensions:
        """
        files = [('All files', '*.*'),
                 ('Text files', '*.txt'), ]

        """
        Put a file, in which the result will be saved, into a variable:
        """
        fl = fd.asksaveasfile(filetypes=files, defaultextension=files)

        """
        Saving procedure:
        """
        try:
            fl.write(out)
            fl.close()
            messagebox.showinfo("Saving", "Successfully saved !")
        except AttributeError:
            pass
    else:
        messagebox.showwarning("Save warning", "You don't have proceeded output yet."
                                               " Please try again after solving procedure")


def create_table():
    """
    A function that is linked to the "Create table" button. Creates a new window at the top of the parent window.
    Newly created window has three buttons and one field for getting user input.
    """
    global is_closed
    if is_closed:  # if window doesn't exist.
        numofm = []
        numofs = []
        values = []

        def create_table2():
            """
            A function that is linked to the "Create table" button of the child "Create table" window.
            Takes number of cities from "e1" field of child window,
            creates a table with user-defined number of cities, but no larger than 5x5, for user manual input.
            """
            nonlocal numofs, numofm, values
            try:
                if (numofs != []) or (numofs != []) or (values != []):
                    clear()

                """
                If number of cities in field "e1" is greater than 5, then sends a warning message.
                If number of cities in field "e1" is less than or equal to 0, sends an error message.
                """
                if int(e1.get()) > 5:
                    messagebox.showwarning("Warning",
                                           "Please, change number of values or import files to proceed large data",
                                           parent=window)
                elif int(e1.get()) <= 0:
                    messagebox.showerror("Error", "Incorrect number of cities, please change and try again.",
                                         parent=window)
                else:
                    """
                    Lists for rows and columns names:
                    """
                    numofm = ['' for _ in range(int(e1.get()))]
                    numofs = ['' for _ in range(int(e1.get()))]

                    """
                    Names placement:
                    """
                    for i in range(int(e1.get())):
                        numofm[i] = customtkinter.CTkLabel(window, text='City' + str(i + 1))
                        numofm[i].grid(row=3, column=i + 1)
                    for j in range(int(e1.get())):
                        numofs[j] = customtkinter.CTkLabel(window, text='City' + str(j + 1))
                        numofs[j].grid(row=j + 4, column=0)

                    """
                    List for the fields:
                    """
                    values = [['' for _ in range(int(e1.get()))] for __ in range(int(e1.get()))]

                    """
                    Fields placement:
                    """
                    for i in range(int(e1.get())):
                        for j in range(int(e1.get())):
                            values[j][i] = customtkinter.CTkEntry(window)
                            values[j][i].grid(row=j + 4, column=i + 1)
            except:
                messagebox.showwarning('Warning', 'Incorrect input, please try again', parent=window)

        def clear():
            """
            A function that is linked to the "Clear" button. Clears child window.
            """
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
            """
            A function that is linked to the "Done" button. Reads user input from earlier created table.
            Transforms it to the pd.DataFrame and writes it to the "dp" global value. If table is not created,
            then asks if user wants to close the window.
            """
            global dp, is_closed
            nonlocal numofm, numofs, values
            try:
                """
                Creating normal 2-D list and inserting values from table in it:
                """
                res = [[] for _ in range(len(numofs))]
                for i in range(len(values)):
                    for j in values[i]:
                        res[i].append(int(j.get()))

                """
                Creating names for rows and columns:
                """
                cl = ['City' + str(i+1) for i in range(len(numofm))]
                rws = ['City' + str(j+1) for j in range(len(numofs))]

                """
                Creating a pd.DataFrame matrix from simple 2-D "res" list:
                """
                dp = pd.DataFrame(data=res, columns=cl, index=rws)

                """
                If matrix is empty, asking if user wants to close the "Create window" table,
                else inserts matrix into display area.
                """
                if len(dp) != 0:
                    txtarea.delete("1.0", "end")
                    txtarea.insert(tk.END, dp.to_string())
                    window.destroy()
                    is_closed = True
                else:
                    an = messagebox.askyesno("Exit", "You have not input any value. Do you want to quit ?")
                    if an:
                        window.destroy()
                        is_closed = True
            except ValueError:
                messagebox.showerror('Error',
                                     'Incorrect input. Please, fill all of the cells and try again.', parent=window)

        def on_close():
            """
            A helper function, used in closing protocol, helps to prevent bug with ability of creating multiple
            instances of a window by multiple clicks at "Create table" button in root window.
            """
            global is_closed
            nonlocal window
            is_closed = True
            window.destroy()

        """
        Child window itself:
        """
        window = customtkinter.CTkToplevel(root)
        window.geometry('800x400')
        window.title('Create table')
        window.attributes('-topmost', True)

        label3 = customtkinter.CTkLabel(window, text='Please enter numbers of cities (less or equal to 5)')
        label3.place(relx=0.025, rely=0.7)
        nofc = customtkinter.CTkLabel(window, text='Number of cities:')
        nofc.place(relx=0.025, rely=0.8)
        e1 = customtkinter.CTkEntry(window)
        e1.place(relx=0.175, rely=0.8)

        crt = customtkinter.CTkButton(window, text='Create table', command=create_table2)
        crt.place(relx=0.415, rely=0.9)

        clr = customtkinter.CTkButton(window, text='Clear', command=clear)
        clr.place(relx=0.025, rely=0.9)

        dnn = customtkinter.CTkButton(window, text='Done', command=done)
        dnn.place(relx=0.8, rely=0.9)
        is_closed = False
        window.protocol("WM_DELETE_WINDOW", on_close)


dp = 0  # Global variable to keep input matrices.
out = ''  # Global variable to keep results of calculations.
is_closed = True  # Global variable to monitor if child window "Create table" is closed.

"""
UI of the main window:
"""

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

txtarea = customtkinter.CTkTextbox(root, width=500, height=200)
txtarea.grid(column=0, row=0, columnspan=4)
l1 = customtkinter.CTkLabel(root, text='Optimal amount:')
l1.grid(column=3, row=1)
l2 = customtkinter.CTkLabel(root, text='Currency:')
l2.grid(column=1, row=1)
l3 = customtkinter.CTkLabel(root, text='For not so big data samples "Dynamic programming algorithm"'
                                       'is OK, it also provide precise results.', font=("Arial", 14))
l3.place(x=0, y=300)
l4 = customtkinter.CTkLabel(root, text='For big data samples you can use "Nearest Neighbor Algorithm". '
                                       'It is not so precise, but much more efficient.', font=("Arial", 14))
l4.place(x=0, y=325)
curr_list = ['UAH', 'USD', 'EUR']
curr_value = customtkinter.StringVar(root)
curr_value.set('UAH')

curr_menu = customtkinter.CTkOptionMenu(master=root, variable=curr_value, values=curr_list)
curr_menu.grid(column=2, row=1)

opt_list = ["Maximize income", "Minimize expenses"]
opt_value = customtkinter.StringVar(root)
opt_value.set('Minimize expenses')

alg_list = ["Dynamic programming algorithm", "Nearest neighbor algorithm"]
alg_value = customtkinter.StringVar(root)
alg_value.set('Dynamic programming algorithm')

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
calc_button = customtkinter.CTkButton(root, image=imgcalc, text="Calculator", command=lambda: calc(root))

calc_button.place(x=0, y=0)
ti_button.grid(column=0, row=2)
open_button.grid(column=1, row=2)
solve_button.grid(column=2, row=2)
save_button.grid(column=3, row=2)

root.mainloop()
