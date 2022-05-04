class GnomeSort:
    def __init__(self, object_list, key, reverse):
        self.__object_list = object_list
        self.__key = key
        self.__reverse = reverse

    @property
    def object_list(self):
        return self.__object_list

    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, key):
        self.__key = key

    @property
    def reverse(self):
        return self.__reverse

    def sort(self):
        self.object_list[:] = self.__gnome_sort(self.object_list)

    def __gnome_sort(self, list):
        index = 0
        while index < len(list):
            if index == 0:
                index += 1
            if self._in_order(list[index - 1], list[index]):
                index += 1
            else:
                list[index], list[index - 1] = list[index - 1], list[index]
                index -= 1
        return list

    def _in_order(self, element1, element2, equal=True):
        if self.key is None:
            self.key = lambda argument: argument
        if self.key(element1) == self.key(element2):
            return equal
        if not self.reverse:
            return self.key(element1) < self.key(element2)
        return self.key(element1) > self.key(element2)


class Sorting(object):
    @staticmethod
    def sort(collection, key=None, reverse=False):
        GnomeSort(collection, key, reverse).sort()
