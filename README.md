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
    * pop(): Removes and returns the "top" value in the heap, while maintaining the heap property.
## Graph:
    * nodes(): Returns a list of all the nodes in the graph.
    * edges(): Returns a list of all the edges in the graph.
    * add_node(value): Adds a new node(value) to the graph.
    * add_edge(value1, value2): Adds a new edge to the graph connecting the node containing 'value1' and the node containing 'value2'. If either value1 or value2 are not already present in the graph, they should be added. If an edge already exisits overwrite it.
    * del_node(value): deletes the node containing 'value' from the graph; raises an error if no such node exists.
    * del_edge(value1, value2): Deletes the edge connecting 'value1' and 'value2' from the graph; raises an error if no such edge exsits.
    * has_node(value): Returns True if node containing 'value' is contained in the graph, False if not.
    * neighbors(value): Returns the list of all nodes connected to the node containing 'value' by edges; raises an error if 'value' is nto in graph.
    * adjacent(value1, value2): Returns True if there is an edge connecting 'value1' and 'value2', False if not; raises an error if either of the supplied values are not in graph.
    * depth_first_traversal(start_val): Performs a full depth-first traversal of the graph beginning at 'start_val'. Returns the full cisited path when traversal is complete.
    * breadth_first_traversal(start_val): Performs a full breadth-first traversal of the graph beginning at the 'start_val'. Returns the full visited path when the traversal is complete.
## Priority Queue:
    * insert(value): Inserts the value into the queue. Takes an optional argument for that value's priority, set by default to 0.
    * pop(): Removes the most important item from the queue and returns its value.
    * peek(): Returns the most important item without removing it from the queue.
