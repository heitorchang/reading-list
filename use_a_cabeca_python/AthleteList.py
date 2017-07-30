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

    a1 = AthleteList("A", "", ["1.0", "2.0", "3.0"])
    a2 = AthleteList("B", "", ["2.0", "3.0", "4.0"])

    all_ath = {}
    all_ath[a1.name] = a1
    all_ath[a2.name] = a2

    ath_name = "A"
    print(all_ath[ath_name].top3())
