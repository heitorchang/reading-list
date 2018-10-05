class LogicGate:

    def __init__(self, n):

        self.label = n
        self.output = None

        print("init LogicGate", self.label)


    def getLabel(self):

        return self.label


    def getOutput(self):

        self.output = self.performGateLogic()  # not defined in this class
        return self.output



class BinaryGate(LogicGate):

    def __init__(self, n):

        LogicGate.__init__(self, n)
        
        # OR 
        # super().__init__(n)
        
        self.pinA = None
        self.pinB = None


    def getPinA(self):

        if self.pinA is None:
            return int(input("Enter Pin A input for gate " + self.getLabel() + ": "))
        else:
            return self.pinA.getFrom().getOutput()


    def getPinB(self):

        if self.pinB is None:
            return int(input("Enter Pin B input for gate " + self.getLabel() + ": "))
        else:
            return self.pinB.getFrom().getOutput()

        
    def setNextPin(self, source):

        if self.pinA is None:
            self.pinA = source

        else:
            if self.pinB is None:
                self.pinB = source
            else:
                raise RuntimeError("Error: No empty pins")
                
            
        
class UnaryGate(LogicGate):

    def __init__(self, n):

        LogicGate.__init__(self, n)

        self.pin = None


    def getPin(self):

        if self.pin is None:
            return int(input("Enter Pin input for gate " + self.getLabel() + ": "))
        else:
            return self.pin.getFrom().getOutput()


    def setNextPin(self, source):
        
        if self.pin is None:
            self.pin = source
        else:
            raise RuntimeError("Error: No empty pins")

                
                
class AndGate(BinaryGate):

    def __init__(self, n):
        
        super(AndGate, self).__init__(n)


    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        
        if a == 1 and b == 1:
            return 1
        else:
            return 0



class OrGate(BinaryGate):

    def __init__(self, n):

        super().__init__(n)


    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()

        if a == 1 or b == 1:
            return 1
        else:
            return 0



class NotGate(UnaryGate):

    def __init__(self, n):

        super().__init__(n)


    def performGateLogic(self):

        p = self.getPin()
        
        if p == 0:
            return 1
        else:
            return 0



class Connector:

    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate

        tgate.setNextPin(self)


    def getFrom(self):
        
        return self.fromgate


    def getTo(self):
        
        return self.togate


