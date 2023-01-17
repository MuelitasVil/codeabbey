import 'dart:io';

List<int> Games(List<int> Wins,int index){

  int winsPlayerOne = 0;
  int winsPlayerTwo = 0;

  if(Wins.last == 0){
    
    List<String> plays = stdin.readLineSync().toString().trim().split(" "); 
    List<String> winsPlayerOne = plays.where((play) => play == "RS" || play == "SP" || play == "PR").toList();
    List<String> winsPlayerTwo = plays.where((play) => play == "SR" || play == "PS" || play == "RP").toList();


    if(winsPlayerOne.length > winsPlayerTwo.length){
      Wins[index] = 1;
      print(1);
    }else{
      Wins[index] = 2;
      print(2);
    }

    Wins = Games(Wins, index+1); 

  }

  return Wins;

}

void main(){
  
  int index = 0;
  int numberOfpalys = int.parse(stdin.readLineSync().toString());
  List<int> wins = new List.filled(numberOfpalys, 0, growable: true);
  wins = Games(wins, index);
  String answer = wins.map((win) => win).toList().join(" ");
  print(answer.trim());
  
}