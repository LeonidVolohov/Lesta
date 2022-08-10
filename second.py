from collections import deque

class CircularBuffer():
    def __init__(self, length: int) -> None:
        self._data = []
        self._index = 0
        self._length = length

    # TODO: fix wrong adding
    def append_element(self, item) -> None:
        if len(self._data) == self._length:
            self._data[self._index] = item
        else:
            self._data.append(item)
        self._index = (self._index + 1) % self._length

    def get_element(self, index: int):
        if index >= len(self._data):
            raise IndexError("Wrong Index. It should be less than len(data)")
        return self._data[index]
    
    def get_data(self) -> list:
        return self._data


class CircularDequeBuffer(deque):
    def __init__(self, size=0):
        super(CircularDequeBuffer, self).__init__(maxlen=size)


def main():
    circular_buffer = CircularBuffer(5)
    for i in range(7):
        circular_buffer.append_element(i)
        print(circular_buffer.get_data())
    print(circular_buffer.get_element(-1))

    print("--------------")

    deq = CircularDequeBuffer(size=5)
    for i in range(7):
        deq.append(i)
        print(list(deq))

if __name__ == "__main__":
    main()