from Get_Data import All_Expenses
from tkinter import *
from tkinter import ttk
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def Analize_Expenses(main_menu,options_list):
    "Analize expenses base on pre-set limit of each catagory and draw pie chart"
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

    

if __name__=="__main__":
    print("Module Show_Data ")

    

