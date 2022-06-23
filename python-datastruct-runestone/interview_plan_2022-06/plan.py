
"""
DO NOT USE,
Use /learn-code/interview-topics/practice_2022-06/plan.py
"""


"""
topics off the top of my head that are important
"""

# calculate pi
# check code/learn-code/common-lisp/find-pi.lisp
# returns index 136120

# rationale for not using "while": avoid an infinite loop, be defensive
# if the range limit chosen was too small, increase it

def find_pi(desired_estimate):
    desired_estimate = str(desired_estimate)
    current_estimate = 0
    for i in range(300000):
        if i % 2 == 0:
            fraction = 4 / (2 * i + 1)
        else:
            fraction = -4 / (2 * i + 1)
        current_estimate += fraction

        # compare estimates
        if str(current_estimate)[:len(desired_estimate)] == desired_estimate:
            print(current_estimate, i)
            break
    else:
        # reached end, did not converge
        print(current_estimate, 'did not converge')



# linked list
# mention collections.deque

class LinkedListNode:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next_node


class HeitorNode:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def __str__(self):
        return str(self.value)

    def print_next_nodes(self):
        print(self.value, end='')
        if self.next_node:
            print(', ', end='')
            self.next_node.print_next_nodes()
        else:
            print()


def testLinkedList():
    hend = HeitorNode(3)
    hmid = HeitorNode(2, hend)
    hstart = HeitorNode(1, hmid)
    hstart.print_next_nodes()
    hmid.print_next_nodes()


### TODO add, remove methods


# binary search


# merge sort


# quicksort


# adjacency list


# BFS


# DFS


# Priority Queue
