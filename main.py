from deque import Deque

deque = Deque()

print("Test 1 - Add first")

for i in range(10):
  deque.add_first(i)

print(deque.size()) # 10
print(deque.is_full()) # True
print(deque.first()) # 9
print(deque.last()) # 0


print("Test 2 - remove first")

for i in range(10):
  deque.remove_first()

print(deque.size()) # 0
print(deque.is_empty()) # True
print(deque.is_full()) # False


print("Test 3 - Add last")

for i in range(10):
  deque.add_last(i)

print(deque.size()) # 10
print(deque.is_full()) # True
print(deque.first()) # 0
print(deque.last()) # 9


print("Test 4 - remove last")

for i in range(10):
  deque.remove_last()

print(deque.size()) # 0
print(deque.is_empty()) # True
