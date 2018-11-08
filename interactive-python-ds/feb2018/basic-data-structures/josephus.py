from mqueue import MQueue

def josephus(people, skip):
    q = MQueue()
    for i in range(1, people+1):
        q.enqueue(i)

    while q.size() > 1:
        print(q)

        for i in range(skip):
            head = q.dequeue()
            print("skip", head)
            q.enqueue(head)
        dead = q.dequeue()
        print(dead, "was killed")
    print(q.dequeue(), "survives")

def test():
    josephus(7, 3)
