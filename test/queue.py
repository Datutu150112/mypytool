from mypytool import *
q = Queue()
q.push(2)
print(q.front()) #输出：2
q.push(1)
print(q.front()) #输出：2
print(q.back()) #输出：1
print(q.size()) #输出：2
q.pop()
q.pop()
print(q.empty()) #输出：True
