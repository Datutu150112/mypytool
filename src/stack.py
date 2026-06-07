class Stack():
    def __init__(self,Top = 0):
        self.Top = Top
        self.Bottom = Top
        self.stack = [0]

    def top(self):
        return self.stack[self.Top - 1]
    def push(self,n):
        if self.Top == 0:
            self.stack[self.Top] = n
        else:
            self.stack.append(n)
        self.Top+=1
        return None
    def pop(self):
        self.Top -= 1
        self.stack[self.Top] = 0
        if self.Top - self.Bottom == 0:
            self.Top = self.Bottom
        return None
    def empty(self):
        if self.Top - self.Bottom == 0:
            return True
        else:
            return False
    def size(self):
        return self.Top - self.Bottom