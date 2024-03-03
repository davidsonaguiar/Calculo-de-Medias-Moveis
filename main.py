from deque import Deque

deque = Deque()

for i in range(8):
  deque.add_first(i)

print(deque.size()) # 8
print(deque.first()) # 7
print(deque.last()) # 0
print(deque.is_full()) # false
