#Miguel Alejandro Figuera Quintero
#C.I:V-23.558.789
#Seccion 8B
#Linked Lists - Hash Maps
from LinkedLists import Linked_List
from LinkedLists import Node



class HashTable:
    #hashes string
    def hashing_function(string):
        hashed=[ord(x) for x in string]

        return sum(hashed)%16

    #hash function with both name & surname.
    def hash(name,surname):
        return (hashing_function(name)+hashing_function(surname))%16


