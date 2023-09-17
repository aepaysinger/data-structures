# data-structures-new
## LinkedList:
    * push(val): Inserts the value at the head of the list
    * pop(): Pops the first value off the head of the list and returns it. Raises an exception if there are no values to return.
    * size(): Returns the length of the list.
    * search(val): Returns the node containing the val in the list if it is present. If it is not present it will return None.
    * remove(node): Removes the given node from the list. If the node is not in the list is will raise an exception.
    * display(): Returns a unicode string representing the list as if it were a Pthon tuple literal. Ex: "(5, 'Bravo', 9)"
    * len(the_list): Returns the size of the list
    * print(the_list): Returns what the display method returns.
## Doubly LinkedList:
    * push(val): Inserts the value val at the head of the list.
    * append(val): Appends the value val to the tail of the list.
    * pop(): Pops the fitst value off the head of the list and return it. Raises an exception with an appropriate message if there are no values to return.
    * shift(): Removes the last value from the tail of the list and returnds it. Raises an exception with an appropriate messafe if there are no values to return.
    * remove(val): Removes the first instance of val found in the list, starting from the head. If val is not present, it will raise and appropriate Python exception.
    * len(): Returns the size of the list.
## Stack:
    * push(val): Adds a value to the stack. The parameter is the value to be added to the stack.
    * pop(): Removes a value from the stack and returns the value. If the stack is empty, attempts to call pop should raise an appropriate Python exception message.
    * len(): Returns the size of the stack
## Queue:
    * enqueue(value): Adds value to the queue.
    * dequeue(): Removes the correct item from the queue and returns its value. If the queue is empty it should raise an error.
    * peek(): Returns the next value in the queue without dequeueing it. If the queue is empty it returns None.
    * size(): Returns the size of the queue. Should return 0 if the queue is empty.
    * len(): Returns the suze of the queue. 
## Deque:
    * append(value): Adds value to the tail of the deque.
    * appendleft(value): Adds value to the front of the deque.
    * pop(): Removes a value from the tail of the deque and returns it. Raises an exception if the Dequw is empty.
    * popleft(): Removes a value from the front of the Deque and returns it. Raises an exception of the Deque is empty.
    * peek(): Returns the next value that would be returned by pop but leaves the value in the Deque. Returns None if the Deque is empty.
    * peekleft(): Returns the next value that would be returned by popleft but leaves the value in the Deque. Returns None if the Deque is empty.
    * size(): Returns the count of items in the Deque. Returns 0 if the Deque is empty.
## Binary Tree:
    * takes a bin_type: max heap (largest number is at the top of the tree) or min heap(smallest number is at the top of the tree).
    * push(val): Puts a new value into the heap, while maintaining the heap property.
    * pop(): Removes the "top" value in the heap, while maintaining the heap property.
    * parent_index(index): Returns the index of the parent index to the give index.
    * left_child_index(index): Returns the left child index of the given index.
    * right_child_index(index): Returns the right child index of the give index.
    * has_parent(index): Returns True or False. Checks if the given index has a parent.
    * has_left_child(index): Returns True or False. Checks if the given index has a left child.
    * has_right_child(index): Returns True or False. Checks if the given index has a right child.
    * heap_up(): Is used to organize the storage. Keeps the smalles element at the top of the tree.
    * heap_down(): Is used to organixe the storage. Keeps the largest element at the top of the tree.
    * swap(index1, index2): Swaps two elements in storage.