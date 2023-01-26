def SacarExtension(self):
    tam = len(self) - 1
    extension = ""

    while(self[tam] != "." and self[tam] != "/"):
      extension = self[tam] + extension
      tam = tam - 1
      
    extension = self[tam] + extension

    if(extension[0] == "."):
        return extension[1::].lower()
    else:
        return "zzzzzzzzz"


print(SacarExtension("https://raw.githubusercontent.com/djs1193/codeabbey/master/q97pya"))