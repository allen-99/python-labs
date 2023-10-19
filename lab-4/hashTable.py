from functools import reduce


class Table:
    def __init__(self, length = 20) -> None:
        self.weidth = 0
        self.length = length
        self.hashTable = dict.fromkeys(range(0, length))  
    

    def __hash_func(self, value):
        return reduce(lambda x, y: x + y, [str(ord(v)) for i, v in enumerate(value)])

    def __get_hash(self, value):
        return int(self.__hash_func(value)) % self.length

    def __change_hash_table_size(self, newLenght):
        newHashTable = Table(newLenght)
        for key, array in self.hashTable.items():
            if array == None:
                continue
            for value in array:
                newHashTable.insert(value)
        self.hashTable = newHashTable.hashTable
        self.length = newLenght

    def insert(self, value):
        index = self.__get_hash(value)
        if self.hashTable[index]:
            self.hashTable[index].append(value) 
        else:
            self.hashTable[index] = [value]
            self.weidth += 1
        
        if self.length // 2 < self.weidth:
            self.__change_hash_table_size(self.length * 2)
    
    def remove(self, value):
        index = self.__get_hash(value)
        if not self.hashTable[index] or value not in self.hashTable[index]:
            print(f'value {value} isnt in hash table')
            return
        self.hashTable[index].remove(value)
        print(f'value {value} success remove')
    
    def search(self, value):
        index = self.__get_hash(value)
        if not self.hashTable[index] or value not in self.hashTable[index]:
            print(f'value {value} isnt in hash table')
            return
        print(f'value {value} is in table')
        print(f'hash index: {index}')
        print(f'hash value: {self.__hash_func(value)}')
        

    def print_table(self):
        for key, array in self.hashTable.items():
            if array == None or not array:
                print(key, ': Empty')
            else:
                print(key, ':', array)

table = Table()

if __name__ == '__main__': 
  
    while(True):
        data_raw = input("Please enter value (add, remove, search, print): ")

        if data_raw == "add":
            value = input("Please enter value for insert into table: ")
            table.insert(value)


        elif data_raw == "remove":
            value = input("Please enter value for delete from table: ")
            table.remove(value)


        elif data_raw == "search":
            value = input("Please enter value for search from table: ")
            table.search(value)


        elif data_raw == "print":
            table.print_table()

        elif data_raw == 'exit':
            break