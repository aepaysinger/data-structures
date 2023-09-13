class BinaryHeap:
    def __init__(self, values=None):
        self.heap = [values]
        self.size = 0
        if values:
            for value in values:
                heap_up(value)
                

        def find_parent(self, index):
            return (index - 1) // 2
        
        def heap_up(self, value):
            index = self.size
            self.heap[index] = value
            parent = find_parent(index)
            while self.heap[parent] < value:
                swap(self.heap[parent], index)
            self.size += 1

        def swap(self, index1, index2):
            self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    
            
