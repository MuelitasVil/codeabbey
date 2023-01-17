import 'dart:io';


List<int> Games(List<int> Wins,int index){

  int winsPlayerOne = 0;
  int winsPlayerTwo = 0;

  if(Wins.last == 0){
    
    List<String> plays = stdin.readLineSync().toString().trim().split(" ");
    plays.map((play) => play == "RS" || play == "SR" || play == "PR" 
    ? winsPlayerOne++ : winsPlayerTwo++);

    if(winsPlayerOne > winsPlayerTwo){
      Wins[index] = 1;
    }else{
      Wins[index] = 2;
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
  wins.map((win) => print(win));
  
}