//Miguel Figuera Quintero V-23.558.789 Seccion 8B

//Define la funcion bubbleSort, tipos de variables y tipo de retorno
function bubbleSort(array: number[]): number[] {
    //longitud del array para el ciclo for de primer nivel
  const num = array.length;
  //ciclo for de primer nivel
  for (let i: number = 0; i < num; i++) {
    //variable swapped inicializada en false para controlar si hubo intercambios
    let swapped: boolean = false;
    //ciclo for de segundo nivel a traves del metodo Array.prototype.forEach()
    array.forEach((value, index) => {
        //compara elemento actual con el siguiente y si el actual es mayor, lo intercambia
      if (index < num - 1 && value > array[index + 1]) {
        //helper para guardar valor actual
        let helper = value;
        //valor actual sustituido por el siguiente
        array[index] = array[index + 1];
        //proximo valor sustituido por valor actual
        array[index + 1] = helper;
        //manifiesta que si hubo un intercambio para evitar el break-case
        swapped = true;
      }
    });
    //si no hubo intercambios, termina el for de primer nivel
    if (!swapped) {
      break;
    }
  }
  //Retorna el array organizado
  return array;
}


let answer = bubbleSort([1,2,7,8,5,3,124,6,54321,3])
console.log(answer)

//Puede probar el codigo en typescriptlang.org/play