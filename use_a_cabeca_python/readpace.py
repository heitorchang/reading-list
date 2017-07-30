# p. 407

row_data = {}

with open("PaceData.csv") as paces:
    column_headings = paces.readline().strip().split(',')
    column_headings.pop(0)
    for each_line in paces:
        row = each_line.strip().split(',')
        row_label = row.pop(0)
        inner_dict = {}
        for i in range(len(column_headings)):
            inner_dict[row[i]] = column_headings[i]
        row_data[row_label] = inner_dict

    # creates a reverse lookup table. Given a distance
    # and time, return the matching VO2 value

def getVO2(row_data, race, time):
    try:
        return row_data[race][time]
    except KeyError:
        return "Exact time not found"
    
def test():
    testeql(row_data['2mi']['8:00'], '84.8')
    testeql(row_data['Marathon']['2:14:15'], '79.3')
    testeql(getVO2(row_data, '2mi', '0:00'), "Exact time not found")
