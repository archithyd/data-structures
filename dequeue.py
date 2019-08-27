import collections

DoubleEnded=collections.deque(["mon","tue","wed"])
print(DoubleEnded)
DoubleEnded.append("thur")
print(DoubleEnded)
DoubleEnded.appendleft("sun")
print(DoubleEnded)
DoubleEnded.pop()
print(DoubleEnded)
DoubleEnded.popleft()
print(DoubleEnded)
