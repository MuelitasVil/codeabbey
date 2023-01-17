import 'dart:ffi';
import 'dart:io';

int Double(int num){

  return num * 2;

}
void main() {

    int winsPlayerOne = 0;
    int winsPlayerTwo = 0;

    List<String> plays = stdin.readLineSync().toString().trim().split(" ");
    plays.map((play) => print(play));
    print(plays.iterator);

    plays.map((play) => play == "RS" || play == "SR" || play == "PR" 
    ? winsPlayerOne++ : winsPlayerTwo++);

    print(winsPlayerOne);
    print(winsPlayerTwo);


  }