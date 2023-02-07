def All_Expenses():
    "read datas saved from file pro analize or display. Data base unavaiable"
    file_handler=open("expenses_data.txt",mode='r')
    data_table=list()
    dat=file_handler.readlines()
    for x in dat:
        data_table.append(x.split(';'))
    return data_table
