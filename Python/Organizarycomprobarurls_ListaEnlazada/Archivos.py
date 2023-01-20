import urllib.request
from os import remove

class Link:
  def __init__(self, link, linkComparar):
    self.link = link
    self.linkComparar = linkComparar

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
    
    newNode = Node(newElement)
    if(self.head == None):
      self.head = newNode
      return

    if(self.head.data.linkComparar > newElement.linkComparar):
        newNode.next = self.head
        self.head = newNode
        return

    else:
      temp = self.head
      insertMedium = False
      while(temp.next != None):
        if(newElement.linkComparar > temp.data.linkComparar and newElement.linkComparar < temp.next.data.linkComparar):
            insertMedium = True
            break
        temp = temp.next
      
      if(insertMedium):
        newNode.next = temp.next
        temp.next = newNode
      else:
         temp.next = newNode 

  def PrintList(self):
    temp = self.head
    if(temp != None):
      print("The list contains:", end=" ")
      while (temp != None):
        print(temp.data.link, end=" ")
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
            
            ListaUrl = LinkedList()
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
                    link = Link(linea, linea.lower())
                    ListaUrl.push_back(link)
            
            print("Se han eliminado {} url's del archivo Other.lst {} ".format(contador, numeroArchivo))
                
            archivo.close()
            remove(Direccion)
            
            archivo = open(Direccion,"w")

            # Se borra el archvio orignal y se reescribe con las url organizadas y funcionales
            # Finalmente se comprueba cuando falte solo un url para evitar el salto de linea final

            while(ListaUrl.IsEmpty() == False):
              if(ListaUrl.IsCasiEmpty() == False):
                url = ListaUrl.pop_front().link
                archivo.write("{}".format(url))
              else:
                url = ListaUrl.pop_front().link
                archivo.write("{}".format(url).strip())
            
            print("Se organizo con exito el archivo {} Others.lst ".format(numeroArchivo))


        except:
            print("El archivo {}\others.lst no existe".format(numeroArchivo))


def EliminarLink(numero, link):
        print(numero)
        numeroArchivo = StringArchivo(numero)

        try:
            
            ListaUrl = LinkedList()
            contador = 0
            Direccion = "C:\\Users\\mmart\\OneDrive\\Escritorio\\AutonomicJump\\challenges\\code\\codeabbey\\{}\\OTHERS.lst".format(numeroArchivo)

            archivo = open(Direccion)
            linea=archivo.readline()
            print("Se abrio el archivo {} Others.lst ".format(numeroArchivo))

            while linea != '':
                UrlEliminadas = False
                linea=archivo.readline()
                try:
                    datos = urllib.request.urlopen(linea)
                except:
                    print("Error {} ".format(linea))
                    UrlEliminadas = True
                    contador = contador + 1 
                
                if(UrlEliminadas == False and linea != link):
                    link = Link(linea, linea.lower())
                    ListaUrl.push_back(link)
            
            print("Se han eliminado {} url's del archivo Other.lst {} ".format(contador, numeroArchivo))
                
            archivo.close()
            remove(Direccion)
            
            archivo = open(Direccion,"w")

            while(ListaUrl.IsEmpty() == False):
              if(ListaUrl.IsCasiEmpty() == False):
                url = ListaUrl.pop_front().link
                archivo.write("{}".format(url))
              else:
                url = ListaUrl.pop_front().link
                archivo.write("{}".format(url).strip())

            print("Se organizo con exito el archivo {} Others.lst ".format(numeroArchivo))


        except:
            print("El archivo {}\others.lst no existe".format(numeroArchivo))

def InsertarLink(numero, link):
        print(numero)
        numeroArchivo = StringArchivo(numero)

        try:
            
            newlink = Link(link, link.lower())
            ListaUrl = LinkedList()
            ListaUrl.push_back(newlink)

            contador = 0
            Direccion = "C:\\Users\\mmart\\OneDrive\\Escritorio\\AutonomicJump\\challenges\\code\\codeabbey\\{}\\OTHERS.lst".format(numeroArchivo)

            archivo = open(Direccion)
            linea=archivo.readline()
            print("Se abrio el archivo {} Others.lst ".format(numeroArchivo))

            while linea != '':
                UrlEliminadas = False
                linea=archivo.readline()
                try:
                    datos = urllib.request.urlopen(linea)
                except:
                    print("Error {} ".format(linea))
                    UrlEliminadas = True
                    contador = contador + 1 
                
                if(UrlEliminadas == False):
                    link = Link(linea, linea.lower())
                    ListaUrl.push_back(link)
            
            print("Se han eliminado {} url's del archivo Other.lst {} ".format(contador, numeroArchivo))
                
            archivo.close()
            remove(Direccion)
            
            archivo = open(Direccion,"w")

            while(ListaUrl.IsEmpty() == False):
              if(ListaUrl.IsCasiEmpty() == False):
                url = ListaUrl.pop_front().link
                archivo.write("{}".format(url))
              else:
                url = ListaUrl.pop_front().link
                archivo.write("{}".format(url).strip())

            print("Se organizo con exito el archivo {} Others.lst ".format(numeroArchivo))


        except:
            print("El archivo {}\others.lst no existe".format(numeroArchivo))


palabra1 = "holaa"
palabra2 = "buenas"

# Insertar Links 
#1
InsertarLink(97, "https://raw.githubusercontent.com/djs1193/codeabbey/master/q97.py\n")
#2
InsertarLink(105, "https://raw.githubusercontent.com/djs1193/codeabbey/master/q105.py\n")
#3
InsertarLink(2,"https://raw.githubusercontent.com/Curio5813/CodeAbbey/master/problem002.py\n")
#4
InsertarLink(5,"https://raw.githubusercontent.com/bijeshkawan/codeabbySolutions/master/pro5.html\n")
#5
InsertarLink(5,"https://raw.githubusercontent.com/bijeshkawan/codeabbySolutions/master/addition_array.html\n")
#6
InsertarLink(2,"https://raw.githubusercontent.com/bijeshkawan/codeabbySolutions/master/sum_in_loop.html\n")
#7
InsertarLink(2,"https://raw.githubusercontent.com/bijeshkawan/codeabbySolutions/master/sum_loop.html\n")
#8
InsertarLink(2,"https://raw.githubusercontent.com/oleksaT/codeabby/main/SumInLoop.java\n")
#9
InsertarLink(16,"https://raw.githubusercontent.com/oleksaT/codeabby/main/AverageOfAnArray.java\n")
#10 MY CODE
InsertarLink(13,"https://raw.githubusercontent.com/MuelitasVil/codeabbey/main/Dart/13%20%20Weighted%20sum%20of%20digits/muelasvill.dart\n")