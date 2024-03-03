from deque import Deque

deque = Deque()

deque.add_first(1)
deque.add_first(2)
deque.add_first(3)
deque.add_last(6)
deque.add_last(7)

deque.remove_last()
deque.remove_first()
deque.remove_last()
deque.remove_first()
deque.remove_first()

print("Is empty: ", deque.is_empty())
print("Is full: ", deque.is_full())
print("Size: ", deque.size())

try:
  print("First: ", deque.first())
  print("Last: ", deque.last())
except Exception as e:
  print(e)
