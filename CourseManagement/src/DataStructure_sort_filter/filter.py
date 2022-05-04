class Filter:
    def __init__(self, object_list, key):
        self.__object_list = object_list
        self.__key = key

    @property
    def object_list(self):
        return self.__object_list

    @property
    def key(self):
        return self.__key

    def filter(self):
        self.object_list[:] = self.__filter_object_list(self.object_list)

    def __filter_object_list(self, object_list):
        filtered_list = []
        for object in object_list:
            if self._keep_element(object):
                filtered_list.append(object)
        return filtered_list

    def _keep_element(self, object):
        if self.key is None:
            return True
        return self.key(object)


class Filtering(object):
    @staticmethod
    def filter(collection, key=None):
        Filter(collection, key).filter()
