
class Lifo:

    maxSize = 0
    buffer = []

    def __init__(self, s = 255):
        assert(isinstance(s, int) and s > 0)
        self.maxSize = s
        self.buffer = []

    def __str__(self):
        ret = self.__class__.__name__ + "\n"
        for k,v in self.__dict__.items():
            ret = ret + k + ": " + str(v) + "\n"
        return ret

    def push(self, obj):
        assert(obj is not None)
        if len(self.buffer) < self.maxSize:
            self.buffer.append(obj)
            return True
        else:
            return False

    def pop(self):
        assert(len(self.buffer) > 0)
        return self.buffer.pop()


class Fifo(Lifo):

    def __init__(self, s = 255):
        Lifo.__init__(self, s)

    def pop(self):
        assert(len(self.buffer) > 0)
        ret = self.buffer[0]
        del(self.buffer[0])
        return ret


def main():
    myLifo = Lifo(8)
    myFifo = Fifo(8)

    for i in range(10):
        myLifo.push(i)
    print(myLifo)
    for i in range(3):
        myLifo.pop()
    print(myLifo)

    for i in range(10):
        myFifo.push(i)
    print(myFifo)
    for i in range(3):
        myFifo.pop()
    print(myFifo)

if __name__ == "__main__":
    main()