class Deque:

  def __init__(self,  capacity):
    if capacity < 2:
      raise Exception("Capacity must be at least 2")
    self._capacity_init = capacity
    self._capacity = capacity
    self._items = [None] * capacity
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


  def items(self):
    return self._items
  

  def add_first(self, item):

    if self.is_full():
      self._resize(2 * self._capacity)

    
    if self.is_empty():
      self._items[0] = item
      self._index_first = 0
      self._index_last = 0
      self._size += 1
      return

      
    if self._index_first == 0:
      self._index_first = self._capacity - 1
      self._items[self._index_first] = item
      self._size += 1
      return
    
    self._index_first -= 1
    self._items[self._index_first] = item
    self._size += 1
    return
    

  def remove_first(self):
    if self.is_empty():
      raise Exception("Deque is empty")
        
    if (self._size - 1 == self._capacity // 4) and (self._capacity // 2 >= self._capacity_init):
      self._resize(self._capacity // 2)
      
    item = self.first()
    self._items[self._index_first] = None
    
    if self._size == 1:
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
      self._resize(2 * self._capacity)

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
    
    if (self._size - 1) == (self._capacity // 4) and( self._capacity // 2) >= self._capacity_init:
      self._resize(self._capacity // 2)	
      
    item = self.last()
    self._items[self._index_last] = None
    
    if self._size == 1:
      self._index_first = None
      self._index_last = None
      self._size -= 1
      return item
    
    if self._index_last == 0:
      self._index_last = self._capacity - 1
      self._size -= 1
      return item

    self._index_last -= 1
    self._size -= 1
    return item

  def _resize(self, new_capacity):

    new_items = [None] * new_capacity
    self._capacity = new_capacity
    index = 0
  
    while self._size > 0:
      first = self.remove_first()
      new_items[index] = first
      index += 1
    
    self._items = new_items
    self._capacity = new_capacity
    self._size = index
    self._index_first = 0
    self._index_last = self._size - 1


  def print(self):
    print(self._items)
 