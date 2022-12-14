# data-structures
## LinkedList
  * push(val): will insert the value ‘val’ at the head of the list
  * pop(): will pop the first value off the head of the list and return it. Raises an exception with an appropriate message if there are no values to return.
  * size(): will return the length of the list
  * search(val): will return the node containing ‘val’ in the list, if present, else None
  * remove(node): will remove the given node from the list, wherever it might be (node must be an item in the list). If the node is not in the list, it should raise an exception with an appropriate message.
  * display() will return a unicode string representing the list as if it were a Python tuple literal: “(12, ‘sam’, 37, ‘tango’)”
  * len(the_list): returns the size of the list
  * print(the_list): returns what the display() method returns
  ## Stack
  * push(value) - Adds a value to the stack. The parameter is the value to be added to the stack.
  * pop() - Removes a value from the stack and returns that value. If the stack is empty, attempts to call pop should raise an appropriate Python exception with message.
  ## Doubly-Linked List
  * push(val) will insert the value val at the head of the list
  * append(val) will append the value val at the tail of the list
  * pop() will pop the first value off the head of the list and return it. Raises an exception with an appropriate message if there are no values to return.
  * shift() will remove the last value from the tail of the list and return it. Raises an exception with an appropriate message if there are no values to return.
  * remove(val) will remove the first instance of val found in the list, starting from the head. If val is not present, it will raise an appropriate Python exception.
  * len() will return the size of the list.
### Que_
  * enqueue(val): adds value to the queue
  * dequeue(): removes the correct item from the queue and returns its value (should raise an error if the queue is empty)
  * peek(): returns the next value in the queue without dequeueing it. If the queue is empty, returns None
  * size(): return the size of the queue. Should return 0 if the queue is empty.
