from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # if self.current is None or self.current is self.capacity:
        #     self.current = 1
        # else:
        #     self.current += 1
        if self.current is None:
            self.storage.add_to_head(item)
            self.current = self.storage.head
        elif self.current.next is None and self.storage.length <= self.capacity:
            self.current.insert_after(item)
            self.current = self.current.next

        if self.current is self.storage.tail:
            self.storage.tail.delete()
            self.storage.add_to_tail(item)
            self.current = self.storage.tail

        else:
            self.storage.delete(self.current.next)
            self.current.insert_after(item)
            self.current = self.current.next
            

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        spot = self.storage.head
        while spot is not None:
            list_buffer_contents += spot.value
            spot = spot.next

        # TODO: Your code here

        return list_buffer_contents

RBT = RingBuffer(3)
RBT.append('a')
RBT.append('b')
RBT.append('c')
RBT.append('D')

print(RBT.storage)
print(RBT.get())











# ----------------Stretch Goal-------------------

class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
