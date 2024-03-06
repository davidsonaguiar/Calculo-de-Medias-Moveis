from deque import Deque

def moving_average(input_list, k):
  deque = Deque()
  for i in range(len(input_list)):
    if i == 0:
      deque.add_last(None)
      deque.add_last(input_list[i])
      continue

    if (i + 1) < k:
      last = deque.remove_last()
      deque.add_last(None)
      deque.add_last(last + input_list[i])
      continue

    last = deque.remove_last()
    sum_step = last + input_list[i]
    deque.add_last(sum_step / 3)

    if i < (len(input_list) - 1):
      del_element = input_list[i - (k - 1)]
      deque.add_last(sum_step - del_element)

  return deque.items()
  