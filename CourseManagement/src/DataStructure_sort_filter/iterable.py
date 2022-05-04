class IterableDataStructure:
    def __init__(self):
        self._index = 0
        self.__elements = []

    @property
    def elements(self):
        return self.__elements[:]

    def append(self, value):
        self.__elements.append(value)

    def __setitem__(self, key, value):
        self.__elements[key] = value

    def __getitem__(self, key):
        return self.__elements[key]

    def __delitem__(self, key):
        del self.__elements[key]

    def __next__(self):
        if self._index < len(self.__elements):
            result = self.__elements[self._index]
            self._index += 1
            return result
        else:
            raise StopIteration

    def __iter__(self):
        self._index = 0
        return self

    def __len__(self):
        return len(self.__elements)
