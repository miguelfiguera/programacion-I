### Pseudo Codigo para bubble sort:

Miguel Alejandro Figuera Quintero
C.I:V-23.558.789
Seccion 8B

```
Inicio bubble_sort(array):
leer array
longitud= longitud del array

loop:
swapped=False
    for e,idx in array (iterar sobre el array, incluyendo indices):

        **revisar cual es mayor entre el actual y el anterior**
        check_mayor=e>array[i-1]

        **Si el actual es mayor cambiar uno por otro y recordar que algo cambio**

        if check_mayor: 
            swap(array[idx], array[idx-1])
            swapped=True
        fin if
    fin for
    *** si no hay ningun cambio de posicion en la iteracion actual, romple el loop***
    break if swapped==False
fin loop

print('sorted array',array)

return array

Fin bubble_sort
``` 

Basicamente es un loop "infinito" con un break case specifico, que dentro de si tiene otro loop que itera sobre todos los elementos de un array, si el array ha mutado algun elemento de su posicion en la iteracion actual, el loop del primer nivel procedera a una nueva iteracion.

Si no hay ninguna mutacion en el array, el loop del primer nivel cumplira su break case y saldra de las iteraciones.