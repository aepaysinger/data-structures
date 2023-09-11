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