class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.location = 0

    def append(self, item):
        # if capacity is full, start from the beginning
        # what is the beginning, if it's always changing? Need to have location within the array that matches up
        # If the array is empty, it's length is 0, and the location is 0
        # If we add an item, the length is 1, and the location has to be 1, however, the array index is 0
        # Let's think about this
        # if we're under capacity, we don't have to do any popping
        # if we're over capacity, we have to pop
        # First check if we've reached the end of what our location should be to insert, then reset to 0
        if self.location == self.capacity:
            self.location = 0
        if len(self.storage) == self.capacity:
            # This should be the normal state after were full, we'll constantly be doing this
            print(f"Capacity reached, Location: {self.location}")
            self.storage.pop(self.location)
            self.storage.insert(self.location, item)
        elif len(self.storage) == 0:
            # This is if we're empty
            self.storage.insert(0, item)
        else:
            # This is for a list that hasn't reached capacity
            print(f"Not at capacity, Location: {self.location}")
            self.storage.insert(self.location, item)
        self.location += 1
            
    def get(self):
        return self.storage

ring_buffer = RingBuffer(3)

ring_buffer.append(1)
print(ring_buffer.get())
ring_buffer.append(2)
print(ring_buffer.get())
ring_buffer.append(3)

print(ring_buffer.get())

ring_buffer.append(4)
print(ring_buffer.get())
ring_buffer.append(5)
print(ring_buffer.get())

# print(ring_buffer.get())
