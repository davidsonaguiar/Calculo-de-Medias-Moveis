from deque import Deque
from moving_average import moving_average

deque = Deque(10)

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


list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [120, 130, 150, 140, 160, 170, 180, 200, 190, 210]
result = moving_average(list, 3)
result2 = moving_average(list2, 3)
print(result)
print(result2)