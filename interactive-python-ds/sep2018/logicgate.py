class LogicGate:
    def __init__(self, n):
        self.label = n
        self.output = None

    def getLabel(self):
        return self.label

    def getOutput(self):
        self.output = self.logic()
        return self.output

    def __repr__(self):
        return self.label
        
        
class BinaryGate(LogicGate):
    def __init__(self, n):
        super().__init__(n)

        self.pinA = None
        self.pinB = None

    def getPinA(self):
        return int(input("Enter pin A input for " + self.getLabel()))

    def getPinB(self):
        return int(input("Enter pin B input for " + self.getLabel()))


class UnaryGate(LogicGate):
    def __init__(self, n):
        super().__init__(n)

        self.pin = None

    def getPin(self):
        return int(input("Enter pin input for " + self.getLabel))

        
class AndGate(BinaryGate):
    def __init__(self, n):
        super().__init__(n)

    def logic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a == 1 and b == 1:
            return 1
        else:
            return 0
            

# Connector has a fromgate and togate
