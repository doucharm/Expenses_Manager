import Get_Data
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tabulate
import sqlalchemy as sql
def Show_Expenses(main_menu,engine):
    "Show data collected in a table, from which user can delete entries accordande with indexes "
    data=Get_Data.All_Expenses(engine)
    total_rows = len(data)
    if total_rows==0:
        return 0
    total_columns = len(data[0])
    data_tab=Toplevel(main_menu)

    data_tab.title("All expenses")
    b_ex=Button(data_tab, text="Quit              ", command=data_tab.destroy)
    b_ex.grid(row=0,column=0)

    class Table: #TABLE structure for easy display
        def __init__(self,root):
            for i in range(total_rows):
                for j in range(total_columns):
                 
                    self.e = Entry(root, width=30, fg='black',
                                   font=('Times New Roman',14))
               
                    self.e.grid(row=i+3, column=j)
                    self.e.insert(END, data[i][j])
 
    t=Table(data_tab)

if __name__=="__main__":
    print("Module Show_Data ")
