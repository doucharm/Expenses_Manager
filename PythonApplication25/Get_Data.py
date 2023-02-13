import sqlalchemy as sql
def All_Expenses(engine):
    "read datas saved from file pro analize or display."
    data_table=list()
    with engine.connect() as conn:
        result = conn.execute(sql.text("SELECT name, cata, date_num,money_num FROM some_table"))
    for row in result:
        data_table.append(row)
    return data_table #returned list for display/analize
