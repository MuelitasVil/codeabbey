import urllib.request
from os import remove

def SacarExtension(self):
    tam = len(self) - 1
    extension = ""

    while(self[tam] != "." and self[tam] != "/"):
      extension = self[tam] + extension
      tam = tam - 1
      
    extension = self[tam] + extension

    return extension

class Link:

  def __init__(self, link, extension):

    self.link = link
    self.extension = extension

# node structure
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

#class Linked List
class LinkedList:
  def __init__(self):
    self.head = None

  #Add new element at the end of the list
  def push_back(self, newElement):
    
    Norepetido = True

    newNode = Node(newElement)
    if(self.head == None):
      self.head = newNode
      return Norepetido

    if(self.head.data.extension == newElement.extension):
        Norepetido = False        
        return Norepetido

    if(self.head.data.extension.lower() > newElement.extension.lower()):

        newNode.next = self.head
        self.head = newNode
        return Norepetido

    else:
      
      temp = self.head
      insertMedium = False

      while(temp.next != None):

        if(newElement.extension == temp.next.data.extension):
          Norepetido = False
          return Norepetido
          
        if(newElement.extension.lower() > temp.data.extension.lower() and newElement.extension.lower() < temp.next.data.extension.lower()):
            insertMedium = True
            break
        temp = temp.next
      
      if(insertMedium and Norepetido):
        newNode.next = temp.next
        temp.next = newNode
      elif(Norepetido or newElement.extension):
         temp.next = newNode 


      return Norepetido

  def PrintList(self):
    temp = self.head
    if(temp != None):
      print("The list contains:", end=" ")
      while (temp != None):
        print(temp.data.extension, end=" ")
        temp = temp.next
      print()
    else:
      print("The list is empty.")

  def pop_front(self):
    
    if(self.head != None):
      temp = self.head
      data = temp.data
      self.head = self.head.next
      temp = None 
  
    return data

  def IsEmpty(self):
    Empty = False
    if(self.head == None):
        Empty = True
    return Empty

  def IsCasiEmpty(self):
    Empty = False
    if(self.head.next == None):
        Empty = True
    return Empty


def StringArchivo(number):
        
        numeroArchivo = ""

        if(number< 10):
            numeroArchivo = "00"+str(number)
        elif(number < 100):
            numeroArchivo = "0"+str(number)
        else:
            numeroArchivo = str(number)

        return numeroArchivo
    

def OrganizarYEliminarLinksDañados():
    numeroArchivo = ""
    for x in range(1, 302):
        OrganizarArchivoOthers(x)
       
 

def OrganizarArchivoOthers(numero):
        print(numero)
        numeroArchivo = StringArchivo(numero)

        try:
            # Se crea la lsita enlazada para insertar en orden alfabetico 
            # Se intenta acceder al orchivo other
            
            ListaUrlExtencion = LinkedList()
            ListaUrlNoExtencion = LinkedList()

            contador = 0
            Direccion = "C:\\Users\\mmart\\OneDrive\\Escritorio\\AutonomicJump\\challenges\\code\\codeabbey\\{}\\OTHERS.lst".format(numeroArchivo)

            archivo = open(Direccion)
            linea=archivo.readline()
            print("Se abrio el archivo {} Others.lst ".format(numeroArchivo))

            while linea != '':
                
                # Se recorren los url y se comprueba si este sigue funcionando
                # Si el url existe se inserta en una lista, sino se ignora

                UrlEliminadas = False
                linea=archivo.readline()

                try:
                    datos = urllib.request.urlopen(linea)
                except:
                    print("Error {} ".format(linea))
                    UrlEliminadas = True
                    contador = contador + 1 
                
                if(UrlEliminadas == False):

                    extension = SacarExtension(linea)
                    print(extension)
                    if(extension[0] == "."):
                      extension = extension[1::]
                      link = Link(linea, extension)
                      if(ListaUrlExtencion.push_back(link) == False):
                        print("Error : Extension repetida: "+link.link+"\n"+"Extencion :"+link.extension)
                    else:
                      extension = extension[1::]
                      print("Link sin extencion "+linea)
                      link = Link(linea, extension)
                      if(ListaUrlNoExtencion.push_back(link) == False):
                        print("Error : Extension repetida: "+link.link+"\n"+"Extencion :"+link.extension)                   


            print("Se han eliminado {} url's del archivo Other.lst {} ".format(contador, numeroArchivo))
                
            #print("--------------------------")
            #ListaUrlNoExtencion.PrintList()
            
            archivo.close()
            remove(Direccion)
            
            archivo = open(Direccion,"w")

            while(ListaUrlExtencion.IsEmpty() == False):
              if(ListaUrlExtencion.IsCasiEmpty() == False or ListaUrlNoExtencion.IsEmpty() == False):
                url = ListaUrlExtencion.pop_front().link
                archivo.write("{}".format(url))
              else:
                url = ListaUrlExtencion.pop_front().link
                archivo.write("{}".format(url).strip())
              
            while(ListaUrlNoExtencion.IsEmpty() == False):
              url = ListaUrlNoExtencion.pop_front().link
              archivo.write("{}".format(url))

            print("Se organizo con exito el archivo {} Others.lst ".format(numeroArchivo))


        except:
            print("El archivo {}\others.lst no existe".format(numeroArchivo))


def OrganizarArchivoOthersDireccion(Direccion):

        try:
            # Se crea la lsita enlazada para insertar en orden alfabetico 
            # Se intenta acceder al orchivo other
            
            ListaUrlExtencion = LinkedList()
            ListaUrlNoExtencion = LinkedList()

            contador = 0

            archivo = open(Direccion)
            linea=archivo.readline()
            print("Se abrio el archivo {}".format(Direccion))

            while linea != '':
                
                # Se recorren los url y se comprueba si este sigue funcionando
                # Si el url existe se inserta en una lista, sino se ignora

                UrlEliminadas = False
                linea=archivo.readline()

                try:
                    datos = urllib.request.urlopen(linea)
                except:
                    print("Error {} ".format(linea))
                    UrlEliminadas = True
                    contador = contador + 1 
                
                if(UrlEliminadas == False):

                    extension = SacarExtension(linea)
                    print(extension)
                    if(extension[0] == "."):
                      extension = extension[1::]
                      link = Link(linea, extension)
                      if(ListaUrlExtencion.push_back(link) == False):
                        print("Error : Extension repetida: "+link.link+"\n"+"Extencion :"+link.extension)
                    else:
                      extension = extension[1::]
                      print("Link sin extencion "+linea)
                      link = Link(linea, extension)
                      if(ListaUrlNoExtencion.push_back(link) == False):
                        print("Error : Extension repetida: "+link.link+"\n"+"Extencion :"+link.extension)                   


            print("Se han eliminado {} url's del archivo {} ".format(contador, Direccion))
                
            #print("--------------------------")
            #ListaUrlNoExtencion.PrintList()
            
            archivo.close()
            remove(Direccion)
            
            archivo = open(Direccion,"w")

            while(ListaUrlExtencion.IsEmpty() == False):
              if(ListaUrlExtencion.IsCasiEmpty() == False or ListaUrlNoExtencion.IsEmpty() == False):
                url = ListaUrlExtencion.pop_front().link
                archivo.write("{}".format(url))
              else:
                url = ListaUrlExtencion.pop_front().link
                archivo.write("{}".format(url).strip())
              
            while(ListaUrlNoExtencion.IsEmpty() == False):
              url = ListaUrlNoExtencion.pop_front().link
              archivo.write("{}".format(url))

            print("Se organizo con exito el archivo {} Others.lst ".format(Direccion))


        except:
            print("El archivo {}\others.lst no existe".format(Direccion))

def InsertarLink(numero, nlink):
        
        print(numero)
        numeroArchivo = StringArchivo(numero)

        try:

            ListaUrlExtencion = LinkedList()
            ListaUrlNoExtencion = LinkedList()

            contador = 0
            Direccion = "C:\\Users\\mmart\\OneDrive\\Escritorio\\AutonomicJump\\challenges\\code\\codeabbey\\{}\\OTHERS.lst".format(numeroArchivo)

            archivo = open(Direccion)
            linea=archivo.readline()
            print("Se abrio el archivo {} Others.lst ".format(numeroArchivo))

            while linea != '':

                UrlEliminadas = False
                linea = archivo.readline()

                try:
                    datos = urllib.request.urlopen(linea)
                except:
                    print("Error {} ".format(linea))
                    UrlEliminadas = True
                    contador = contador + 1 
                
                if(UrlEliminadas == False):

                    extension = SacarExtension(linea)

                    if(extension[0] == "."):
                      extension = extension[1::]
                      link = Link(linea, extension)
                      if(ListaUrlExtencion.push_back(link) == False):
                        print("Error : Extension repetida: "+link.link+"\n"+"Extencion :"+link.extension)
                    else:
                      extension = extension[1::]
                      link = Link(linea, extension)
                      if(ListaUrlNoExtencion.push_back(link) == False):
                        print("Error : Extension repetida: "+link.link+"\n"+"Extencion :"+link.extension)                   


            print("Se han eliminado {} url's del archivo Other.lst {} ".format(contador, numeroArchivo))
                
            archivo.close()
            remove(Direccion)
            
            archivo = open(Direccion,"w")
            extension = SacarExtension(nlink)

            if(extension == "."):
              extension = extension[1::]
              link = Link(nlink, extension)
              if(ListaUrlExtencion.push_back(link) == False):
                print("Error : Extension insertada repetida: "+link.link+"\n"+"Extencion :"+link.extension)
              else:
                print("Se ha insertado con exito el link")
            else:
                extension = extension[1::]
                link = Link(nlink, extension)
                if(ListaUrlNoExtencion.push_back(link) == False):
                  print("Error : Extension insertada  repetida: "+link.link+"\n"+"Extencion :"+link.extension)  
                else:
                  print("Se ha insertado con exito el link")
              

            while(ListaUrlExtencion.IsEmpty() == False):
              if(ListaUrlExtencion.IsCasiEmpty() == False or ListaUrlNoExtencion.IsEmpty() == False):
                url = ListaUrlExtencion.pop_front().link
                archivo.write("{}".format(url))
              else:
                url = ListaUrlExtencion.pop_front().link
                archivo.write("{}".format(url).strip())
              
            while(ListaUrlNoExtencion.IsEmpty() == False):
              url = ListaUrlNoExtencion.pop_front().link
              archivo.write("{}".format(url))

            print("Se organizo con exito el archivo {} Others.lst ".format(numeroArchivo))


        except:
            print("El archivo {}\others.lst no existe".format(numeroArchivo))

OrganizarArchivoOthers(35)

#InsertarLink(13,"https://raw.githubusercontent.com/MuelitasVil/codeabbey/main/Dart/13%20%20Weighted%20sum%20of%20digits/muelasvill.dart\n")
#InsertarLink(14,"https://raw.githubusercontent.com/MuelitasVil/codeabbey/Ejercicio14/Dart/14%20Moduar%20calculator/muelasvill.dart\n")
#InsertarLink(49,"https://raw.githubusercontent.com/MuelitasVil/codeabbey/Ej49RSP/Dart/49%20RSP/muelasvill.dart\n")