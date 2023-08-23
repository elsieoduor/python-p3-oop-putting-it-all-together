#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand):
        self.brand = brand
        self._size = 0

    def get_shoe_size(self):
        return self._size
    
    def set_shoe_size(self, size):
        if type(size) == int:
            self._size = size
        else:
            print('size must be an integer')
    
    size = property(get_shoe_size, set_shoe_size)

    def cobble(self, condition = 'New'):
        self.condition = condition
        return ('Your shoe is as good as new!')
    
        
    