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

    if(self.head.data == newElement):
        Norepetido = False        
        return Norepetido

    if(self.head.data > newElement):
        newNode.next = self.head
        self.head = newNode
        return Norepetido

    else:
      
      temp = self.head
      insertMedium = False

      while(temp.next != None):

        if(newElement == temp.next.data):
          Norepetido = False

        if(newElement > temp.data and newElement < temp.next.data):
            insertMedium = True
            break
        temp = temp.next
      
      if(insertMedium and Norepetido):
        newNode.next = temp.next
        temp.next = newNode
      elif(Norepetido):
         temp.next = newNode 


      return Norepetido

  def PrintList(self):
    temp = self.head
    if(temp != None):
      print("The list contains:", end=" ")
      while (temp != None):
        print(temp.data, end=" ")
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


lista = LinkedList()


print(lista.push_back(1))
print(lista.push_back(10))
print(lista.push_back(1))
print(lista.push_back(1))
print(lista.push_back(1))
print(lista.push_back(2))

lista.PrintList()