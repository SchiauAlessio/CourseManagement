class IterableDataStructureDictionary:
    def __init__(self):
        self.__dictionary={}

    def __setitem__(self,key,value):
        self.__dictionary[key]=value

    def __getitem__(self,key):
        return self.__dictionary[key]

    def __delitem__(self,index):
        del self.__dictionary[index]


    def __iter__(self):
        return self.__dictionary.__iter__()


    def __len__(self):
        return len(self.__dictionary)

    def values(self):
        return list(self.__dictionary.values())