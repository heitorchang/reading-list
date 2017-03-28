import datetime

def install_ccdiary():
    quick_create("my_ccdiary", "amount int, ord int, type text, who text, day date")

def add_cc(amount, order, typ, who, day=None):
    """
    add_cc(3, 1, 'vid', 'name', '2017-03-27')  # first time
    add_cc(3, 2, 'pic', 'another name')  # second time
    """
    
    if day == None:
        day = datetime.datetime.now().strftime("%Y-%m-%d")
    quick_insert("my_ccdiary", (amount, order, typ, who, day))

def all_cc(typ=None, first_only=False):
    """
    all_cc('pic' OR 'vid', True OR False)
    """
    
    if typ == None:
        where_clause = "WHERE 1"
    else:
        where_clause = "WHERE type = '{}'".format(typ)

    if first_only:
        first_clause = " AND ord <= 1 "
    else:
        first_clause = " AND ord > 0 "
        
    sql = """
    SELECT day, amount, ord, type, who FROM my_ccdiary
    """ + where_clause + first_clause + """
    ORDER BY day desc"""

    # print(sql)
    
    weekdays = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    cursor = cnx.cursor(named_tuple=True)
    cursor.execute(sql)

    for row in cursor:
        if row.ord == 1:
            order = ""
        elif row.ord == 2:
            order = "2nd"
        elif row.ord == 3:
            order = "3rd"
        else:
            order = row.ord + "th"
        print("{} {} {:3s} {:10s} {} {}".format(
            weekdays[row.day.weekday()], row.day.strftime("%d/%m/%y"), order,
            "*" * row.amount, row.type, row.who))
    cursor.close()
