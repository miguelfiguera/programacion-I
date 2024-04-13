algoritmo para confirmar que es posible un triangulo con las medidas indicadas.
```
inicio inecualidad_triangulo(a,b,c):
        *agregar todos los valores a un array*
        array=[a,b,c]
        *organizar el array de menor a mayor*
        array.sort()
        *llevar la respuesta a un valor boolean*
        respuesta= (array[0] + array[1])>array[2]
        *regresar respuesta*
        return response
fin de inecualidad_triangulo
```