# p. 437

name = "Jim"

def what_happens_here():
    print(name)  # can read variables from outer scopes
    name += " is great"  # ... but cannot assign to them
    # must use : global name
    print(name)
    
def test():
    testeql(what_happens_here(), None)
