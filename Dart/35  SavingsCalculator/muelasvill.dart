import 'dart:io';

int CantOfMonth(double base, double goal, double interest, int cantOfmonth) {
  if (base < goal) {
    base = base + (base * (interest / 100));
    cantOfmonth = CantOfMonth(base, goal, interest, cantOfmonth + 1);
  }

  return cantOfmonth;
}

String SavingsCalculator(int NumsOfSaving, int number_saving) {
  String months = "";

  if (number_saving < NumsOfSaving) {
    List<String> Account = stdin.readLineSync().toString().split(" ");
    List<double> NumsAccount =
        Account.map((value) => double.parse(value + ".0")).toList();

    months = CantOfMonth(NumsAccount[0], NumsAccount[1], NumsAccount[2], 0)
        .toString();
    months = months + " " + SavingsCalculator(NumsOfSaving, number_saving + 1);
  }

  return months;
}

void main() {
  int NumsOfAccount = int.parse(stdin.readLineSync().toString());
  print(SavingsCalculator(NumsOfAccount, 0).trim());
}
