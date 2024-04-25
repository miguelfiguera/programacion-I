#Miguel Alejandro Figuera Quintero
#C.I:V-23.558.789
#Seccion 8B
#Linked Lists - Hash Maps

#Linked list


class Node:
    #Define el constructor para los nodos y sus valores iniciales.
    def __init__(self,value,children=None):
        self.value=value
        self.children=children

    

class List:
#Define el constructor de la lista y sus valores iniciales
    def __init__(self):
        self.instances=[]
        self.head=self.instances[0]
        self.tail=self.instances[-1]
        self.node_count=0
    
    #Funcion para corregir en caso de que haya algun tipo
    #de desbalance dentro de la lista.
    def node_correction(self):
        length=len(self.instances)
        # Loop para corregir el desbalance
        for i,x in enumerate(self.instances):
            # Si el indice es menor a la longitud-1 de la lista
            #entonces el hijo del nodo actual, es el siguiente en la lista.
            if i < length-1:
                x.children=self.instances[i+1]
            #si el indice es igual al longitud-1 de la lista
            #el nodo actual es el final de la lista y no debe tener hijo.
            elif i==length-1:
                x.children=None
                #se puede convertir en un uroboros (linked list circular) de la siguiente manera
                #x.children=self.instances[0]
        #actualizar la cabeza y la cola
        self.head=self.instances[0]
        self.tail=self.instances[-1]
    
    def create_node(self,value,children=None):
        #crea el nodo y lo agrega a la lista
        self.instances.append(Node(value,children))
        self.node_count+=1

    def create_nodes_list(self,array):
        #list comprehension para crear todos los nodos a partir de un array
        # y colocarlos dentro de la lista de instances.
        the_list=[self.create_node(x,array[i+1]) if i<len(array)-1 else self.create_node(x,None) for i,x in enumerate(array)]
        self.instances=the_list
        self.node_count=len(array)

    def append_new_node(self,value,children=None):
        #agrega un nuevo nodo a la lista
        self.create_node(value,children)
        #corrige la lista para que todos los elementos
        #esten debidamente anclados al siguiente.
        self.node_correction()
    
    def size(self):
        print (f'La lista contiene:{self.node_count} nodos.')
    
    def head(self):
        print(self.head)
    def tail(self):
        print(self.tail)

    def __str__(self):
        for i,x in enumerate(self.instances):
            print(f'(key:{x.value} -> children: {x.children})')
        return f'La lista contiene {self.node_count} nodos'
    
    def pop_node(self):
        #elimina el ultimo nodo de la lista.
        self.instances.pop()
        self.node_count-=1

    def delete_node_at(self,index):
        #guard clause si el indice no existe
        if index>=len(self.instances)-1:
            print('Index does not exist')
            print(f'Top index is {len(self.instances)-1}')
            return
        #borra el nodo en el indice indicado
        self.instances.pop(index)
        #reduce el numero de nodos
        self.node_count-=1
        #corrige ruptura en la cadena
        self.node_correction()
    def insert_node(self,index,value):
        #inserta el nodo en el indice indicado
        self.instances.insert(index,self.create_node(value))
        #aumenta numero de nodos
        self.node_count+=1
        #corrige la cadena
        self.node_correction()

    def find(self,value):
        answer=[]
        #busca el valor en la lista
        for x in self.instances:
            if x.value==value:
                answer.append(x)
        #Si no hay un valor, avisa que no fue encontrado
        if answer==[]:
            return f'{value} not found'
        #retorna el nodo
        return answer[0]

    

    
array=[1,2,3,4,5,6,7,8,9,10,123,4,1235661,1233221,4368,4567,679,567,809]