import Get_Data
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tabulate
def Show_Expenses(main_menu):
    "Show data collected in a table, from which user can delete entries accordande with indexes "
    data=Get_Data.All_Expenses()
    total_rows = len(data)
    if total_rows==0:
        return 0
    total_columns = len(data[0])
    data_tab=Toplevel(main_menu)

    def Delete_Entry():
        file_handler1=open("expenses_data.txt")
        data1=file_handler1.readlines()
        file_handler1.close()
        index=int(i_dx.get("1.0", "end-1c"))
        if index<=len(data1):
                data1.pop(index)
                file_handler2=open("expenses_data.txt",mode='w')
                file_handler2.writelines(data1)

        data_tab.destroy()
    

    data_tab.title("All expenses")
    b_ex=Button(data_tab, text="Quit              ", command=data_tab.destroy)
    b_del=Button(data_tab,text="Delete index",command=Delete_Entry)
    i_dx=Text(data_tab, height = 1,width = 6,bg = "light yellow")
    b_ex.grid(row=0,column=0)
    b_del.grid(row=1,column=0)
    i_dx.grid(row=1,column=1)
    
   
    class Table:
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
