class AthleteList(list):
    def __init__(self, a_name, a_dob=None, a_times=[]):
        # list.__init__([])  # appears to be optional
        self.name = a_name
        self.dob = a_dob
        self.extend(a_times)
    def top3(self):
        return sorted(set(self))[:3]

def test():
    k = AthleteList("Kelly", "1997-11-15")
    testeql(k.top3(), [])

    j = AthleteList("John", "2002-01-29", ["2:01", "3:15", "2:02", "5:22"])
    testeql(j.top3(), ["2:01", "2:02", "3:15"])
