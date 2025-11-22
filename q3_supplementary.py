#!/usr/bin/env python
# coding: utf-8

class HashTable():
    """Implements a simple hash table of size k, with all 
    empty entries denoted as '-' at initialisation.

    You must not modify this code.

    Set up your hashtable as follows, with some sensible integer value for k:
        h = HashTable(k)
    
    For a HashTable h:
        h.lookup(pos) returns the data in position pos.
        h.add(pos, data) adds data in position pos. 
        h.check(table) checks that the current entries are equal to 
            table, which is represented as a list. This is only used for 
            testing that the hash table contains what we expect.
        h.print_table prints h (for debugging only).
    """
    def __init__(self, k):
        self.__table = ["-"] * k  
    def lookup(self, pos):
        return self.__table[pos]
    def add(self, pos, data):
        self.__table[pos] = data
    def check(self, table_of_data):
        return self.__table == table_of_data
    def print_table(self):
        print(self.__table)




#### WRITE YOUR SOLUTION BELOW; DO NOT MODIFY CODE ABOVE THIS LINE####
#### COPY YOUR CODE FROM BELOW INTO A FILE q3.py FOR SUBMISSION ####
#### DO NOT INCLUDE CODE ABOVE THIS LINE IN q3.py ####

def hash_quadratic(d):
    """Inserts keys from the list d into a hash table and
    returns the HashTable which contains the state of the 
    hash table after these insertions.

    Use just one HashTable instance inside this function.
    
    Uses quadratic probing (see question for details) to resolve 
    collisions.
    """
    raise NotImplementedError("Implement this function")

def hash_double(d):
    """Inserts keys from the list d into a hash table and
    returns the HashTable which contains the state of the 
    hash table after these insertions.

    Use just one HashTable instance inside this function.
    
    Uses secondary hashing (see question for details) to resolve
    collisions.
    """
    raise NotImplementedError("Implement this function")


#### WRITE YOUR SOLUTION ABOVE; DO NOT MODIFY CODE BELOW THIS LINE ####
#### DO NOT INCLUDE CODE BELOW THIS LINE IN q2.py ####

def q3_simple_tests():
    assert(hash_quadratic([1, 2, 3, 4, 5]).check(['-', '-', '-', '-', 4, '-', '-', '-', '-', 
        5, '-', '-', 1, '-', '-', '-', '-', 2, '-', '-', '-', '-', 3]))
    assert(hash_quadratic([5]).check(['-', '-', '-', '-', '-', '-', '-', '-', '-', 5, '-', 
        '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']))
    assert(hash_quadratic([28,5]).check(['-', '-', '-', '-', '-', '-', '-', '-', '-', 28, 5,
        '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']))


    assert(hash_double([1, 2, 3, 4, 5]).check(['-', '-', '-', '-', 4, '-', '-', '-', '-',
        5, '-', '-', 1, '-', '-', '-', '-', 2, '-', '-', '-', '-', 3]))
    assert(hash_double([5]).check(['-', '-', '-', '-', '-', '-', '-', '-', '-',
        5, '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']))
    assert(hash_double([28, 5]).check(['-', '-', '-', '-', '-', '-', '-', '-', '-',
        28, '-', '-', '-', '-', '-', 5, '-', '-', '-', '-', '-', '-', '-']))

