class Stack:
    """Структура данных стек"""
    def __init__(self):
        self._elements = []

    def push(self, value):
        self._elements.append(value)

    def pop(self):
        value = self.back()
        del self._elements[-1]
        return value

    def back(self):
        if len(self._elements) == 0:
            raise IndexError('trying delete element from empty stack')
        value = self._elements[-1]
        return value

    def size(self):
        return len(self._elements)

    def clear(self):
        self._elements.clear()


def read_from_file(file_path: str):
    stack = Stack()
    with open(file_path) as file:
        for line in file:
            line = line.rstrip()
            record = line.split(' ')
            func = record[0]
            if func == "push":
                stack.push(record[1])
                print('ok')

            elif func == "pop":
                try:
                    v = stack.pop()
                    print(v)
                except IndexError as e:
                    print('error')

            elif func == "back":
                try:
                    v = stack.back()
                    print(v)
                except IndexError as e:
                    print('error')

            elif func == "clear":
                stack.clear()
                print("ok")

            elif func == "size":
                s = stack.size()
                print(s)

            elif func == "exit":
                print("bye")
                exit(0)

            else:
                continue

            # print("\n")


if __name__ == "__main__":
    read_from_file("input.txt")
    # stack = Stack()
    # stack.clear()
    # stack.push(2)
    # value = stack.back()
    # print("Last value = %s" % value)
    # stack.push(3)
    # value = stack.back()
    # print("Last value = %s" % value)
    # value = stack.pop()
    # print("Last value = %s" % value)
    # count = stack.size()
    # print("Size = %s" % count)
    #
    # command = stack.pop
    # import sys
    # read_from_file(sys.argv[1])
