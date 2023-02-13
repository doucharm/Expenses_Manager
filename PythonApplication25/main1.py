from tkinter import *
from tkinter import ttk
import sqlalchemy as sql

import class1
from Add_Expense import add_expenses
from Show_Data import Show_Expenses
import Analize_Data

def main():
    engine = sql.create_engine("sqlite+pysqlite:///expenses_datas.dbf", echo=True) #shared engine to access expenses_datas.db
    main_menu = Tk()
    main_menu.title("Expenses manager")
    options_list = ["Groceries", "Housing and Utilities", "Transpotation", "Entertainment",'Health care','Miscellaneous']
    # catagories can be modified to fit personal details
    main_menu.geometry("250x200")
    bg = PhotoImage(file = "bg_im.ppm") 
    canvas1 = Canvas( main_menu, width = 250,height = 200) #placed all widgets on canvas
    canvas1.pack(fill = "both", expand = True)
    canvas1.create_image( 0, 0, image = bg,anchor = "nw")
    canvas1.create_text( 200, 250, text = "Welcome")
    button1 = Button( main_menu, text = "Add expense",command=lambda:add_expenses(main_menu,options_list,engine))
    button2 = Button( main_menu, text = "Show expenses",command=lambda:Show_Expenses(main_menu,engine))
    button3 = Button( main_menu, text = "Analyze",command=lambda:Analize_Data.Analize_Expenses(main_menu,options_list,engine))
    button4 = Button( main_menu, text = "Quit",command=main_menu.destroy)
    button1_canvas = canvas1.create_window( 150, 50,anchor = "nw",window = button1)
    button2_canvas = canvas1.create_window( 150, 80,anchor = "nw",window = button2)
    button3_canvas = canvas1.create_window( 150, 110, anchor = "nw",window = button3)
    button4_canvas = canvas1.create_window( 150, 140, anchor = "nw",window = button4)
    main_menu.mainloop()
if __name__ == "__main__":
    main()
    
    
    
