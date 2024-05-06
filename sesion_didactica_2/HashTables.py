#Miguel Alejandro Figuera Quintero
#C.I:V-23.558.789
#Seccion 8B
#Hash Table with linked list and Nodes.
from LinkedLists import Linked_List
from LinkedLists import Node


# poblacion de muestra para trabajar
nombres_apellidos_venezolanos = [
    "José Pérez",
    "María Rodríguez",
    "Luis González",
    "Carmen Martínez",
    "Carlos Hernández",
    "Ana López",
    "Juan García",
    "Jesús Sánchez",
    "Pedro Fernández",
    "Rosa Ramírez",
    "Rafael Torres",
    "Ángel Díaz"
]
names2=[
  "Adelynn Nixon",
  "Cory Cabrera",
  "Daleyza Ponce",
  "Langston Vincent",
  "Allyson Cobb",
  "Raphael Murphy",
  "Bella Maddox",
  "Lyric Garrison",
  "Cadence Brooks",
  "Jordan Mueller",
  "Imani Benitez",
  "Justice Medina",
  "Elliana Dillon",
  "Alvin Wolfe",
  "Hallie Christian",
  "Ledger Dawson",
  "Veronica Reed",
  "Easton Mack",
  "Nadia Roy",
  "Marcelo Miranda",
  "Amina Moss",
  "Porter Jackson",
  "Avery Leach",
  "Westin Kerr",
  "Baylee Andrade",
  "Abdiel Tanner",
  "Harmoni Gibson",
  "Tyler Jefferson",
  "Julieta Baldwin",
  "Jaiden Rich"
]

class HashTable:

    def __init__(self) -> None:
        self.load_factor=0.75
        self.capacity=16
        self.instances=[]
        self.nodes=0
    
    def create_linked_lists(self):
        for i in range(self.capacity-1):
            self.instances.append(Linked_List())

    def create_node(self,value):
        capacity=self.capacity
        # crea un nuevo nodo
        new_node=Node(value)
        new_node.hash(capacity)
        self.instances[new_node.hash].append_new_node_hash(new_node)
        self.nodes += 1
        return 'new node created'
    
    def create_all_nodes(self,array):
        for i in array:
            self.create_node(i)
        self.evaluate_load()
    
    # si cambia la capacidad, los nodos deben ser reubicados.
    def reubicate_nodes(self):
        #queue para listar todos los nodos
        queue=[]
        #recorrer todos los "buckets" en el hash Table
        for i in self.instances:
            #recorrer todos los nodos en cada linked list
            for x in i.instances:
                #agregar el nodo a la queue
                queue.append(x)
        
        # emitir nuevo hash para los nodos y reubicar en una nueva linked list
        for i in queue:
            i.hash(self.capacity)
            self.instances[i.hash].append_new_node_hash(i)
    
    def evaluate_load(self):
        # calcula el factor de carga
        time_to_extend_load:bool=self.capacity*self.load_factor>=self.nodes
        if time_to_extend_load == True:
            # si el factor de carga fue alcanzado, aumenta la capacidad y reubica los nodos
            self.capacity*2
            self.reubicate_nodes()
        else:
            print('load is quite fine...currently I mean...')


