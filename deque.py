class Deque:

  def __init__(self):
    self._capacity = 5
    self._items = [None] * self._capacity
    self._size = 0
    self._index_first = None
    self._index_last = None

  
  def is_empty(self):
    return self._size == 0
  
  
  def size(self):
    return self._size
  

  def is_full(self):
    return self._size == self._capacity
  

  def first(self):
    if self.is_empty():
      raise Exception("Deque is empty")
    return self._items[self._index_first]
  
    
  def last(self):
    if self.is_empty():
      raise Exception("Deque is empty")

    return self._items[self._index_last]

      
  def add_first(self, item):
    if self.is_full():
      raise Exception("Deque is full")

    if self.is_empty():
      self._items[0] = item
      self._index_first = 0
      self._index_last = 0
      self._size += 1
      return

    if self._index_first == 0:
      self._index_first = self._capacity - 1
      self._items[self._index_first] = item
      self._index_last = 0
      self._size += 1
      return
    
    self._index_first -= 1
    self._items[self._index_first] = item
    self._size += 1
    return
    

  def remove_first(self):
    if self.is_empty():
      raise Exception("Deque is empty")
      
    item = self.first()
    self._items[self._index_first] = None
    
    if self._size == 1:
      print("Entrou aqui")
      self._index_first = None
      self._index_last = None
      self._size = 0
      return item
    
    if self._index_first == self._capacity - 1:
      self._index_first = 0
      self._size -= 1
      return item

    self._index_first += 1
    self._size -= 1
    return item

  
  def add_last(self, item):
    if self.is_full():
      raise Exception("Deque is full")

    if self.is_empty():
      self._items[0] = item
      self._index_first = 0
      self._index_last = 0
      self._size += 1
      return

    if self._index_last == self._capacity - 1:
      self._index_last = 0
      self._items[self._index_last] = item
      self._size += 1
      return
    
    self._index_last += 1
    self._items[self._index_last] = item
    self._size += 1
    return

  
  def remove_last(self):
    if self.is_empty():
      raise Exception("Deque is empty")
      
    item = self.last()
    self._items[self._index_last] = None
    
    if self._size == 1:
      self._index_first = None
      self._index_last = None
      self._size -= 0
      return item
    
    if self._index_last == 0:
      self._index_last = self._capacity - 1
      self._size -= 1
      return item

    self._index_last -= 1
    self._size -= 1
    return item