from Data_1 import nested_list

class FlatIterator():

    def __init__(self, some_list):
        self.some_list = some_list

    def __iter__(self):
        self.cursor_1 = -1
        self.cursor_2 = 0
        return self

    def __next__(self):
        self.cursor_1 += 1
        if self.cursor_1 == len(self.some_list[self.cursor_2]):
            self.cursor_1 = 0
            self.cursor_2 += 1
            if self.cursor_2 == len(self.some_list):
                raise StopIteration
        return self.some_list[self.cursor_2][self.cursor_1]


if __name__ == '__main__':
    for item in FlatIterator(nested_list):
        print(item)
    flat_list = [item for item in FlatIterator(nested_list)]
    print(flat_list)


