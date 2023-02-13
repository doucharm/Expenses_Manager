from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import Calendar
import sqlalchemy as sql
import class1

def add_expenses(main_menu,options_list,engine):
    "Adding a new entry to data base, entry have 4 attribute name,catagory,date and money, of which only money are strictly required"
    def save_payment():
        i1 = input_payment.get("1.0","end-1c")
        i2 = value_inside.get()
        i3=  input_date.get("1.0","end-1c")
        i4 = input_money.get("1.0", "end-1c")
        if input_money.get("1.0", END)=="\n" or not i4.isdigit():
            messagebox.showerror(title="Invalid expense", message="Need to specific an amount of money")
            add_expense.destroy()
        else:
            pay=class1.Payment(i1,i2,i3,i4)
            with engine.connect() as conn:
                conn.execute(sql.text("INSERT INTO some_table (name,cata,date_num,money_num) VALUES (:name,:cata,:date_num,:money_num)"),[{"name": i1, "cata": i2, "date_num": i3, "money_num": i4}],)
                conn.commit() #insert data into base and close window.
            add_expense.destroy()

    add_expense=Toplevel(main_menu)
    add_expense.geometry('500x150')
    add_expense.title('Enter payment')
    Label(add_expense,text="Fill the bracket", width=20).grid(row=0, column=0)
    Label(add_expense,text="Payment: ", width=15).grid(row=1, column=0)
    input_payment = Text(add_expense, height = 1,width = 30,bg = "light yellow")
    input_payment.grid(row=1,column=2)
    # attribute name is a textbox for string, where user can input whatever detail needed to clarify the entry
    def callback(selection):
        i2=value_inside.get()
    Label(add_expense,text="Category: ", width=15).grid(row=2, column=0)
    
    value_inside = StringVar(add_expense)
    value_inside.set("Miscellaneous")
    question_menu = OptionMenu(add_expense, value_inside, *options_list,command=callback)
    question_menu.grid(row=2,column=2)
    # attribute catagory(default miscellaneous)

    Label(add_expense,text="Date:", width=15).grid(row=3, column=0)
    input_date=Text(add_expense,height=1,width=20,bg='light green')
    input_date.grid(row=3,column=2)
    def Get_Date():
        def print_sel():
             input_date.insert(END,cal.selection_get())
             top.destroy()
        top = Toplevel(add_expense)
        cal = Calendar(top,font="Arial 14", selectmode='day',cursor="hand1", year=2023, month=2, day=1)
        cal.pack(fill="both", expand=True)
        ttk.Button(top, text="Select_date", command=print_sel).pack()
    Button(add_expense, text = "Get Date",command = Get_Date).grid(row=3, column=3)
    #date sellection screen, open a seperate calendar for easy visualization
    Label(add_expense,text="Money: ", width=15).grid(row=4, column=0)
    input_money = Text(add_expense, height = 1,width = 10,bg = "light blue")
    input_money.grid(row=4,column=2)
    Button(add_expense,text="Save this payment", command=save_payment).grid(row=6,column=2) # save entry to database

if __name__=="__main__":
    print("Module Show_Data ")

