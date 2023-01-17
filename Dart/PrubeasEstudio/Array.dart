void main(){

  List<String> lista  = ["hola", "juan", "roberto"];
  List NuevaLista = lista.where((alumno) => alumno.startsWith("h")).toList();

  print(lista);
  print(NuevaLista);

  print("-----------------");
  lista.removeAt(0);
  print(lista);

  // Remove where 

  
    List<int> numeros2 = [1, 2, 3];
    List<int> NuevaLista2 = numeros2.map((num) => num == 2 ? num : 0).toList();
    NuevaLista2.removeWhere((element) => element == 0);

    List<int> numeros = [1, 2, 3, 4];
    numeros.removeWhere((element) => element == 2);

    List<String> numbers = ['one', 'two', 'three', 'four'];
    numbers.removeWhere((item) => item.length == 3);
    print(numbers.join(', ')); // 'three, four'
    

}