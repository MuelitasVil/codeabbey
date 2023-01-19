import 'dart:io';


String SumOfDigits(List<int> num, int indice){
  //Se ingresa la lista de enteros, la recucion va hasta que ses vacie la lista
  int? Sumatoria = num[0] * indice;

  num.removeAt(0);

  if(!num.isEmpty){

    Sumatoria = Sumatoria + int.parse(SumOfDigits(num, indice + 1));
    
  }
  
  return Sumatoria.toString();

}

String WalkNumbers(List<String> lista){

    String answer = "";

    if(!lista.isEmpty){
      
      //Se convierte el numero en una lsita de enteros
      List<int> Numbers = lista[0].split("").map
      ((num) => int.parse(num)).toList();
      lista.removeAt(0);
      answer = SumOfDigits(Numbers, 1);
      answer = answer + " " + WalkNumbers(lista);  
    
    }

    return answer;

}

void main(){


  stdin.readLineSync().toString();
  List<String> numbers = stdin.readLineSync().toString().trim().split(" ");
  print(WalkNumbers(numbers).trim());

}