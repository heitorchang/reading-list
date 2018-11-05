def isValid(state, missionaries, cannibals):
    boat = state[2]
    if boat:
        if state[0] - missionaries < 0:
            print("not enough missionaries on bank A")
            return False
        if state[1] - cannibals < 0:
            print("not enough cannibals on bank A")
            return False
        if state[1] - cannibals > state[0] - missionaries:
            print("A to B: cannibals outnumber missionaries")
            return False
    else:
        if state[0] + missionaries > 3:
            print("not enough missionaries on bank B")
            return False
        if state[1] + cannibals > 3:
            print("not enough cannibals on bank B")
            return False
        if state[1] + cannibals > state[0] + missionaries:
            print("B to A: cannibals outnumber missionaries")
            return False
    return True


def isValidState(state):
    return 0 <= state[0] <= 3 and 0 <= state[1] <= 3

    
class World:
    def __init__(self, missionaries, cannibals, boatOnBankA):
        # river banks a and b
        # in bank a, (missionaries, cannibals, boatOnBankA)
        # self.state = [3, 3, True]
        self.state = [missionaries, cannibals, boatOnBankA]
        self.seen = set([tuple(self.state)])
        self.path = []

    def move(self, missionaries, cannibals):
        curstate = self.state[:]
        
        if self.state[2]:
            self.state[0] -= missionaries
            self.state[1] -= cannibals
            self.state[2] = False
        else:
            self.state[0] += missionaries
            self.state[1] += cannibals
            self.state[2] = True

        newstate = self.state
        
        if isValidState(newstate) and tuple(newstate) not in self.seen:
            self.state = newstate
            self.seen.add(tuple(self.state))
            self.path.append(self.state)
        else:
            self.state = curstate

        if self.state == [0, 0, 0]:
            return self.path
            
        print(self.seen, self.state)
        return self.state

    def __str__(self):
        return str(self.state)
        
    def __repr__(self):
        return self.__str__()


def solve():
    w = World(3, 3, True)
    options = [[2, 0], [0, 2], [1, 0], [0, 1], [1, 1]]

    counter = 1
    while counter < 150:
        for o in options:
            print(o)
            w = World(*w.move(*o))
            # infinite loop
            counter += 1
