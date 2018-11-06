# river banks a and b
# [missionariesBankA, cannibalsBankA, boatsBankA, missionariesBankB, cannibalsBankB, boatsBankB]
# 
# initial state = [3, 3, 1, 0, 0, 0]

from collections import deque

class Vertex:
    def __init__(self, ma, ca, ba, mb, cb, bb):
        self.ma = ma
        self.ca = ca
        self.ba = ba
        self.mb = mb
        self.cb = cb
        self.bb = bb
        self.state = [ma, ca, ba, mb, cb, bb]
        self.pred = ""

    def __str__(self):
        return str(self.ma) + str(self.ca) + str(self.ba) + str(self.mb) + str(self.cb) + str(self.bb)

    def __repr__(self):
        return str(self.state)

    def isValid(self):
        return self.ma >= 0 and self.ca >= 0 and self.mb >= 0 and self.cb >= 0 and (self.ma >= self.ca or self.ma == 0) and (self.mb >= self.cb or self.mb == 0)

    def move(self, m, c):
        if self.ba == 1:
            return Vertex(self.ma - m, self.ca - c, 0, self.mb + m, self.cb + c, 1)
        else:
            return Vertex(self.ma + m, self.ca + c, 1, self.mb - m, self.cb - c, 0)
            
            
class Graph:
    def __init__(self):
        self.seen = set()
        self.vertices = {}

        # initialize vertices, exclude invalid states
        for m in range(4):
            for c in range(4):
                for b in range(2):
                    v = Vertex(m, c, b, 3-m, 3-c, 1-b)
                    if v.isValid():
                        self.vertices[str(v)] = v
                        
        self.start = self.vertices['331000']

        # BFS
        d = deque()

        d.append(self.start)

        self.seen.add(str(self.start))
        
        while d:
            curv = d.popleft()
            if str(curv) == '000331':
                # Found solution
                stack = [str(curv)]
                last = curv

                while True:
                    if last.pred == "":
                        break
                    stack.append(last.pred[:3] + " " + last.pred[3:])
                    last = self.vertices[last.pred]
                for mv in stack[::-1]:
                    print(mv)
                break

            # edges
            for m in range(3):
                for c in range(3):
                    if 1 <= m + c <= 2:
                        # print('from', curv, 'move', m, c)
                        dest = curv.move(m, c)
                        if dest.isValid() and str(dest) not in self.seen:

                            # print('setting pred of', str(dest), 'to', str(curv))
                            self.vertices[str(dest)].pred = str(curv)
                            
                            self.seen.add(str(dest))
                            d.append(self.vertices[str(dest)])
                            
                
