import 'dart:io';

int Double(int num){

  return num * 2;

}
void main() {

    int winsPlayerOne = 0;
    int winsPlayerTwo = 0;

    List<String> plays = stdin.readLineSync().toString().trim().split(" ");
    String answer = plays.map((play) => play).toList().join(" ");
    print("................");
    print(answer);

    plays.map((play) => play == "RS" || play == "SP" || play == "PR" 
    ? winsPlayerOne++ : winsPlayerTwo++).toList();

    print(winsPlayerOne);
    print(winsPlayerTwo);



  }