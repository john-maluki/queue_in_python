class Node:
  def __init__(self, value):
    self.value = value
    self.next = None


class Queue:
  def __init__(self):
    self.first = None
    self.last = None
    self.length = 0

  def enqueue(self, value):
    new_node = Node(value)
    if self.is_empty:
      self.first = new_node
      self.last = new_node
      self.length += 1
    else:
      self.last.next = new_node
      self.last = new_node
      self.length += 1

  def dequeue(self):
    if self.is_empty:
      return None

    leader = self.first
    self.first = leader.next
    del leader
    self.length -= 1

  def peek(self):
    if self.is_empty:
      return None
    return self.first.value

  @property
  def items(self):
    values = []
    if self.is_empty:
      return []
    current_node = self.first
    while(current_node != None):
      values.append(current_node.value)
      current_node = current_node.next
    return values

  @property
  def is_empty(self):
    return self.length == 0


queue = Queue()
print(queue.items)
queue.enqueue(100)
print(queue.items)
queue.enqueue(105)
print(queue.items)
queue.enqueue(110)
print(queue.items)
p = queue.peek()
print(p)
queue.dequeue()
print(queue.items)
queue.enqueue(115)
print(queue.items)