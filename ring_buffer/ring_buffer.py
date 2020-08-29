class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.count = 0

    def append(self, item):
        if  self.capacity > len(self.storage):
            self.storage.append(item)
            self.count += 1
        
        elif self.count == self.capacity:
            self.count = 0
            self.storage[self.count] = item
            self.count +=1

        else:
            self.storage[self.count] = item
            self.count += 1

            
        return item


    def get(self):
        return (self.storage)