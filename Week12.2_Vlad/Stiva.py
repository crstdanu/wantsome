# stiva (Last In First Out)
# coada (First In First Out)
# lista liniara simplu/dublu inlantuita
# graf
# arbore

class Stiva:
    def __init__(self):
        self.elemente = []

    def push(self, nr):
        self.elemente.append(nr)

    def pop(self):
        return self.elemente.pop()

    def __str__(self):
        return str(self.elemente)


class Coada:
    def __init__(self):
        self.elemente = []

    def enqueue(self, nr):
        self.elemente.append(nr)

    def deque(self):
        return self.elemente.pop(0)

    def __str__(self):
        return str(self.elemente)


class Node:
    def __init__(self, nr):
        self.left = None
        self.right = None
        self.data = nr

    def insert(self, nr):
        if self.data is None:
            self.data = nr
        else:
            if nr == self.data:
                pass
            elif nr < self.data:
                if self.left is None:
                    self.left = Node(nr)
                else:
                    self.left.insert(nr)
            else:
                if self.right is None:
                    self.right = Node(nr)
                else:
                    self.right.insert(nr)

    def traversare_inordine(self):
        if self.left:
            self.left.traversare_inordine()
        print(self.data)
        if self.right:
            self.right.traversare_inordine()


n = Node(100)
n.insert(50)
n.insert(75)
n.insert(25)
n.insert(10)
n.insert(30)
n.insert(1)
n.insert(2)
n.insert(85)
n.insert(80)
n.insert(95)
n.traversare_inordine()


# st = Stiva()
# st.push(10)
# st.push(100)
# st.push(21)
# st.push(5)
# print(st)
# a = st.pop()
# b = st.pop()
# print(a,b)
# print(st)
# print(' ')
# co = Coada()
# co.enqueue(11)
# co.enqueue(5)
# co.enqueue(8)
# co.enqueue(44)
# co.enqueue(32)
# print(co)
# a = co.deque()
# b = co.deque()
# print(a,b)
# print(co)
