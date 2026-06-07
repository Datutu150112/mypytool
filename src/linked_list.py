class Linked_node:
    def __init__(self,list,point=None,id=0):
        self.n = list
        self.points = point
        self.id = id
class General_Linked_list:
    def __init__(self,n=None):
        self.head = Linked_node(n)
        self.element = 1
    def append(self,n):
        new_Linkednode = Linked_node(n,None,self.element)
        temp = self.head
        for i in range(self.element - 1):
            temp = self.head.points
        temp.points = new_Linkednode
        self.element += 1
    def display(self):
        temp = self.head
        for i in range(self.element):
            print(temp.n,end=" -> ")
            temp = temp.points
    def delet(self):
        self.element -= 1
        temp = self.head
        for i in range(self.element - 1):
            temp = self.head.points
        temp.points = None
    def is_empty(self):
        return self.head is None
    def length(self):
        return self.element
    def items(self):
        temp = self.head
        while temp is not None:
            yield temp.n
            temp = temp.points
    def add(self,n,place=1):
        temp = self.head
        temp2 = Linked_node(n,temp.points,place)
        if self.is_empty():
            self.head.points = temp2
        elif place > (self.length() - 1):
            self.append(n)
        else:
            for i in range(place - 1):
                temp = temp.points
            temp2.points = temp.points
            temp.points = temp2
            temp2.points.id += 1
        self.element += 1
    def insert(self,n,place=1):
        temp = self.head
        temp2 = Linked_node(n,temp.points,place)
        if self.is_empty():
            self.head.points = temp2
        elif place > (self.length() - 1):
            self.append(n)
        else:
            for i in range(place - 1):
                temp = temp.points
            temp2.points = temp.points
            temp.points = temp2
            temp2.points.id += 1
        self.element += 1
    def remove(self,place=1):
        temp = self.head
        if not self.is_empty:
            if place > (self.length() - 1):
                self.delet()
            else:
                for i in range(place - 1):
                    temp = temp.points
                temp2 = temp.points
                temp2.point.id -= 1
                temp.points = temp2.points
        self.element -= 1
    def find(self,n):
        return n in self.items()
class Cycle_Linked_list:
    def __init__(self,n=None):
        self.head = Linked_node(n)
        self.element = 1
    def append(self,n):
        temp = Linked_node(n,id=self.element)
        temp.points = temp
        if self.element == 1:
            self.head.points = temp
        else:
            temp2 = self.head
            for i in range(self.element - 1):
                temp2 = temp2.points
            temp.points = self.head.points
            temp2.points = temp
        self.element += 1
    def delet(self):
        temp = self.head
        self.element -= 1
        for i in range(self.element - 1):
            temp = temp.points
        if self.element == 1:
            self.head.points = None
        else:
             temp.points = self.head.points
    def items(self):
        temp = self.head
        for i in range(self.element):
            yield temp.n
            temp = temp.points
    def display(self):
        temp = self.head
        for i in range(self.element):
            print(temp.n,end=" -> ")
            temp = temp.points
    def is_empty(self):
        return self.head.points is None
    def length(self):
        return self.element
    def add(self,n,place=1):
        temp = self.head
        temp2 = Linked_node(n,id=place)
        temp2.points = temp2
        if self.is_empty():
            self.head.points = temp2
        elif place == 1:
            temp2.points = temp.points
            self.head.points = temp2
            temp3 = self.head
            for i in range(self.element - 1):
                temp3 = temp3.points
            temp3.points = temp2
        elif place > (self.length() - 1):
            self.append(n)
        else:
            for i in range(place - 1):
                temp = temp.points
            temp2.points = temp.points
            temp.points = temp2
        self.element += 1
    def insert(self,n,place=1):
        temp = self.head
        temp2 = Linked_node(n,id=place)
        temp2.points = temp2
        if self.is_empty():
            self.head.points = temp2
        elif place == 1:
            temp2.points = temp.points
            self.head.points = temp2
            temp3 = self.head
            for i in range(self.element):
                temp3 = temp3.points
            temp3.points = temp2
        elif place > (self.length() - 1):
            self.append(n)
        else:
            for i in range(place - 1):
                temp = temp.points
            temp2.points = temp.points
            temp.points = temp2
        self.element += 1
    def remove(self,place = 1):
        temp = self.head
        temp2 = self.head
        if not self.is_empty():
            if not self.length == 2:
                if place > (self.length() - 1):
                    self.delet()
                elif place == 1:
                    temp.points = temp.points.points
                    for i in range(self.element - 1):
                        temp2 = temp2.points
                    temp2.points = self.head.points
                    
                else:
                    for i in range(place - 2):
                        temp = temp.points
                    temp.points = temp.points.points
            else:
                self.head.points = None
        self.element -= 1
    def find(self,n):
        return n in self.items()        