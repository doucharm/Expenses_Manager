from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import Calendar
import tabulate
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
class Payment:
    def __init__(self,name_of_payment:str,type_of_payment:str,money:int,date:str):
        self.type_of_payment=type_of_payment 
        self.name_of_payment=name_of_payment
        self.money=money 
        self.date= date 
def add_expenses():
    def save_payment():
        i1 = input_payment.get("1.0","end-1c")
        i2 = value_inside.get()
        i3=  input_date.get("1.0","end-1c")
        i4 = input_money.get("1.0", "end-1c")
        if input_money.get("1.0", END)=="\n" or not i4.isdigit():
            messagebox.showerror(title="Invalid expense", message="Need to specific an amount of money")
            add_expense.destroy()
        else:
            pay=Payment(i1,i2,i3,i4)
            file_handler=open("expenses_data.txt",mode='a')
            to_file=i1+';'+i2+';'+i3+';'+i4
            file_handler.write(to_file)
            file_handler.write('\n')
            add_expense.destroy()
    add_expense=Toplevel(main_menu)
    add_expense.geometry('500x150')
    add_expense.title('Enter payment')
    Label(add_expense,text="Fill the bracket", width=20).grid(row=0, column=0)
    Label(add_expense,text="Payment: ", width=15).grid(row=1, column=0)
    input_payment = Text(add_expense, height = 1,width = 30,bg = "light yellow")
    input_payment.grid(row=1,column=2)

    def callback(selection):
        i2=value_inside.get()
    Label(add_expense,text="Categrory: ", width=15).grid(row=2, column=0)
    
    value_inside = StringVar(add_expense)
    value_inside.set("Miscellaneous")
    question_menu = OptionMenu(add_expense, value_inside, *options_list,command=callback)
    question_menu.grid(row=2,column=2)


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

    Label(add_expense,text="Money: ", width=15).grid(row=4, column=0)
    input_money = Text(add_expense, height = 1,width = 10,bg = "light blue")
    input_money.grid(row=4,column=2)


    Button(add_expense,text="Save this payment", command=save_payment).grid(row=6,column=2)
def All_Expenses():
    file_handler=open("expenses_data.txt",mode='r')
    data_table=list()
    dat=file_handler.readlines()
    for x in dat:
        data_table.append(x.split(';'))
    return data_table
def Show_Expenses():
    data=All_Expenses()
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
def Analize_Expenses():
    data=All_Expenses()
    catag=[0,0,0,0,0,0]
    over_spend=[0,0,0,0,0,0,0]
    for x in data:
        if int(x[3])>1000:
            over_spend[0]+=1
        for y in options_list:
            if x[1]==y:
                catag[options_list.index(y)]+=int(x[3])
    analize_window=Toplevel(main_menu)
    frame_pie_chart = Frame(analize_window)
    frame_pie_chart.pack()
    fig = plt.Figure()
    ax = fig.add_subplot(111)
    s_catag=list()
    s_option=list()
    for i in range(0,len(catag)):
        if catag[i]!=0:
            s_catag.append(catag[i])
            s_option.append(options_list[i])
    ax.pie(s_catag, radius=1, labels=s_option)
    chart1 = FigureCanvasTkAgg(fig,frame_pie_chart)
    chart1.get_tk_widget().pack()
    over_spend[1]=round(sum(catag)/150,2)
    over_spend[2]=round(catag[0]/40,2)
    over_spend[3]=round(catag[1]/80,2)
    over_spend[4]=round(catag[2]/40,2)
    over_spend[5]=round(catag[3]/30,2)
    over_spend[6]=round(catag[5]/30,2)
    o1=Label(analize_window, text="Control expenses")
    o1.pack()
    o2=Label(analize_window, text="There are "+ str(over_spend[0])+" purchases over the limit")
    o_all=Label(analize_window, text="Reached "+ str(over_spend[1])+"% spending limit for all purchases ("+str(sum(catag))+" kc )")
    o3=Label(analize_window, text="Reached "+ str(over_spend[2])+"% spending limit for groceries ("+str(catag[0])+" kc )")
    o4=Label(analize_window, text="Reached "+ str(over_spend[3])+"% spending limit for housing and utilities ("+str(catag[1])+" kc )")
    o5=Label(analize_window, text="Reached "+ str(over_spend[4])+"% spending limit for transportation ("+str(catag[2])+" kc )")
    o6=Label(analize_window, text="Reached "+ str(over_spend[5])+"% spending limit for entertainment ("+str(catag[3])+" kc )")
    o7=Label(analize_window, text="Reached "+ str(over_spend[6])+"% spending limit for miscellaneous ("+str(catag[5])+" kc )")
    o2.pack()
    o_all.pack()
    o3.pack()
    o4.pack()
    o5.pack()
    o6.pack()
    o7.pack()
main_menu = Tk()
main_menu.title("Expenses manager")
options_list = ["Groceries", "Housing and Utilities", "Transpotation", "Entertainment",'Health care','Miscellaneous']
main_menu.geometry("250x200")
bg = PhotoImage(file = "bg_im.ppm")
canvas1 = Canvas( main_menu, width = 250,height = 200) 
canvas1.pack(fill = "both", expand = True)
canvas1.create_image( 0, 0, image = bg,anchor = "nw")
canvas1.create_text( 200, 250, text = "Welcome")
button1 = Button( main_menu, text = "Add expense",command=add_expenses)
button2 = Button( main_menu, text = "Show expenses",command=Show_Expenses)
button3 = Button( main_menu, text = "Analyze",command=Analize_Expenses)
button4 = Button( main_menu, text = "Quit",command=main_menu.destroy)
button1_canvas = canvas1.create_window( 150, 50,anchor = "nw",window = button1)
button2_canvas = canvas1.create_window( 150, 80,anchor = "nw",window = button2)
button3_canvas = canvas1.create_window( 150, 110, anchor = "nw",window = button3)
button4_canvas = canvas1.create_window( 150, 140, anchor = "nw",window = button4)
main_menu.mainloop()

