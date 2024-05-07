### Pseudo Codigo para bubble sort:

Miguel Alejandro Figuera Quintero
C.I:V-23.558.789
Seccion 8B

```
iniciar proceso bubble_sort (array):

lee array (debe ser de un solo tipo de dato)

lee longitud_de_array

Loop While True:

    cambio_alguno? = false

        for element,index in array (iterar sobre el array, incluyendo indices):


            revisar cual es mayor entre el actual y el anterior

            if element mayor que array[index-1] & index != 0:


            Si el actual es menor cambiar uno por otro y notificar que algo cambio



            cambiar de lugar element actual con el anterior.
            cambio_alguno? = True

            fin if
    
        fin for

*** si no hay ningun cambio de posicion en la iteracion actual (while Loop), rompe el loop***

    if cambio_alguno? == false:

    break loop while

   fin if

fin while (fin codigo interno, realmente ese loop es infinito)

print(array)

retornar array

fin proceso bubble_sort.
    
    

``` 

Basicamente es un loop "infinito" con un break case specifico, que dentro de si tiene otro loop que itera sobre todos los elementos de un array, si el array ha mutado algun elemento de su posicion en la iteracion actual, el loop del primer nivel procedera a una nueva iteracion.

Si no hay ninguna mutacion en el array, el loop del primer nivel cumplira su break case y saldra de las iteraciones.