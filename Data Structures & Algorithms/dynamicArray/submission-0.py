class DynamicArray:
    
    def __init__(self, capacity: int):
        self.vector = list()
        self.capacity = capacity


    def get(self, i: int) -> int:
        return self.vector[i]

    def set(self, i: int, n: int) -> None:
        self.vector[i] = n

    def pushback(self, n: int) -> None:
        if len(self.vector) >= self.capacity:
            self.resize()
        self.vector.append(n)

    def popback(self) -> int:
        val = self.vector[-1]
        self.vector.pop()
        return val

    def resize(self) -> None:
        self.capacity *= 2

    def getSize(self) -> int:
        return len(self.vector)
    
    def getCapacity(self) -> int:
        return self.capacity
