class Queue():
    def __init__(self,Front=0,End = 0):
        self.Front = Front
        self.End = End
        self.endcp = End
        self.queue = [0]
        if self.End != 0 or self.Front != 0:
            for i in range(self.End + self.Front):
                self.queue.append(0)
    def push(self,n):
        if self.End == self.endcp:
            self.queue[self.End] = n
        else:
            self.queue.append(n)
        self.End += 1
        return None
    def pop(self):
        self.queue[self.Front] = 0
        self.Front += 1
        if self.End - self.Front == 0:
            self.End = 0
            self.Front = 0
        return None
    def size(self):
        return self.End - self.Front
    def empty(self):
        if self.End - self.Front == 0:
            return True
        else:
            return False
    def front(self):
        return self.queue[self.Front]
    def back(self):
        return self.queue[self.End]