//Declara la funcion y establece los tipos de data que recibe en cada variable
//Declara tambien que tipo de dato retornara la funcion.
function triangleInequality(a:number,b:number,c:number):boolean{
    //convierte los argumentos a un array de numberos
    const array:number[]=[a,b,c];

    //crea un segundo array con los argumentos ordenados de menor a mayor
    const sorted=array.sort((a,b)=>a-b);
    
    //retorna un valor booleano
    //si la suma de los dos primeros elementos es mayor al tercero, el triangulo puede construirse
    //por lo tanto retorna true
    //caso contrario retorna false porque el triangulo no puede construirse.
    return sorted[0]+sorted[1]>sorted[2];
}