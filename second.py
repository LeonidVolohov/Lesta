class RingBuffer():
    def __init__(self, length: int) -> None:
        self.data = []
        self.index = 0
        self.length = length

    def append_element(self, item):
        if len(self.data) == self.length:
            self.data[self.index] = item
        else:
            self.data.append(item)
        self.index = (self.index + 1) % self.length

    def get_element(self, index):
        return self.data[index]


def main():
    rb = RingBuffer(5)
    rb.append_element(1)
    print(rb.data)
    rb.append_element(2)
    print(rb.data)
    rb.append_element(3)
    print(rb.data)
    rb.append_element(4)
    print(rb.data)
    rb.append_element(5)
    print(rb.data)
    rb.append_element(6)
    print(rb.data)
    print(rb.get_element(1))

if __name__ == "__main__":
    main()