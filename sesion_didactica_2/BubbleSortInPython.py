# Miguel Figuera Quintero V-23.558.789 Seccion 8B

def bubble_sort(array:list):
    print(array)
    #Numero de iteraciones posibles.
    num=len(array)-1
    #Loop de primer nivel para la cantidad de iteraciones
    while True:
        #variable para determinar break-case
        swapped=False
        #loop de segundo nivel (nested loop) para cada elemento del array
        for index,element in enumerate(array):
            #comparar elementos y ver si el actual es menor que el anterior
            #Eliminando la posibilidad de que el array se muerda la cola puesto
            #que en python array[-1] es igual al ultimo dato del array
            if element < array[index-1] and index != 0:
                #intercambiar elementos con ayuda de un auixiliar(helper)
                #para no perder la informacion
                helper=array[index-1]
                #el anterior obtiene al actual
                array[index-1]=element
                #el actual obtiene al helper
                array[index]=helper
                #determinar que no se cumple el break-case
                swapped=True
                #print('array:',array)
        #break-case
        if not swapped:
            break
    #retornar el array ordenado
    return array
# Fin del proceso marcado por indentacion.


print(bubble_sort([9,8,7,6,5,4,3,2,1]))