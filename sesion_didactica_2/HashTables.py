#Miguel Alejandro Figuera Quintero
#C.I:V-23.558.789
#Seccion 8B
#Hash Table with linked list and Nodes.
from LinkedLists import Linked_List
from LinkedLists import Node


# poblacion de muestra para trabajar
nombres_apellidos_venezolanos = [
    "José Pérez",
    "séJo réPez",
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
        self.nodes=0
        self.instances=[]

    
    def create_linked_lists(self):
        for i in range(self.capacity):
            self.instances.append(Linked_List())

    def create_node(self,value):
        capacity=self.capacity
        # crea un nuevo nodo
        new_node=Node(value)
        new_node.hashing(capacity)
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
        

        self.instances=[]
        #crea nuevas linked lists mientras la data esta segura en el queue
        self.create_linked_lists()  
    
    
        # emitir nuevo hash para los nodos y reubicar en una nueva linked list
        for i in queue:
            i.hashing(self.capacity)
            self.instances[i.hash].append_new_node_hash(i)
    
    def evaluate_load(self):
        # calcula el factor de carga
        time_to_extend_load:bool=self.nodes>=int(self.capacity*self.load_factor)
        if time_to_extend_load:
            print('Load to big'.center(30,'~'))
            print('Reubicating Nodes'.center(30,'~'))
            # si el factor de carga fue alcanzado, aumenta la capacidad y reubica los nodos
            self.capacity=self.capacity*2
            self.reubicate_nodes()
        else:
            print('\n load is quite fine...currently I mean...')

    def __str__(self) -> str:
        message='''
        Hash Table with linked lists and Nodes.
        Load_factor: {load}
        Capacity: {capacity}
        Nodes: {nodes}
'''
        return message.format(load=self.load_factor,capacity=self.capacity,nodes=self.nodes)

    def print_all_nodes(self):
        #recorre cada instancia de cada bucket
        for i,x in enumerate(self.instances):
            if len(x.instances)==0:
                print('bucket:'.center(30,'*'),i,f'\n{x}\n',)
            else:
                print('bucket:'.center(30,'*'),i)
            for y in x.instances:
                print(f'{y} \n')

    def hash_value_for_find(self,value):
        #separa el nombre y apellido
        name,surname=value.split(' ')

        #convierte cada letra en un valor numerico

        hashed1=[ord(x)for x in name]
        hashed2=[ord(x)for x in surname]


        #suma todos los valores numericos en el list y lo lleva a un numero entre 0 y 15

        return ((sum(hashed1)%self.capacity) + (sum(hashed2)%self.capacity))%self.capacity
    
    def find_node(self,value):
        print(f'searching for {value}'.center(30,'.'))
        #identifica el bucket al replicar el hash del valor del nodo
        index=self.hash_value_for_find(value)
        #imprime el valor del bucket
        print(f'At bucket {index}:'.center(30,'*'))
        #imprime el resultado
        result= self.instances[index].find(value)
        if result:
            return result
        else:
            return f'{value} not found \n'


    def has(self,value):
        result=self.find_node(value)
        if result:
            return True
        else:
            return False
    
    def length(self):
        return self.nodes
    
    def delete(self,value):
        helper=self.hash_value_for_find(value)
        if helper is None:
            return 'value not found'
        self.instances[helper].delete_after_find(value)
        self.nodes -= 1
        print(f'{value} was deleted')


    def clear_map(self):
        print('HashMap has been cleared'.center(30,'~'))
        self.instances=[]
        self.capacity=16
        self.load_factor=0.75
        self.nodes=0
        self.create_linked_lists()

my_table=HashTable()
my_table.create_linked_lists()
print(my_table)
my_table.create_all_nodes(nombres_apellidos_venezolanos)
#my_table.print_all_nodes()
print(my_table)
#print(my_table.nodes<=int(my_table.capacity*my_table.load_factor))
my_table.find_node('José Pérez')
my_table.find_node('Nadia Roy')
my_table.create_all_nodes(names2)
print(my_table)
my_table.print_all_nodes()
my_table.find_node('Nadia Roy')
my_table.find_node('José Pérez')
print(my_table)
my_table.delete('Nadia Roy')
my_table.find_node('Nadia Roy')
print(my_table)
my_table.clear_map()
print(my_table)