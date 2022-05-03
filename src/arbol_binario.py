import time

class Nodo:
  def __init__(self,dato):
    self.izq = None
    self.dato = dato
    self.der = None

class Binario:
  def __init__(self):
    self.raiz = None

  def inserta(self,padre,dato):
    print("entro a inserta con ", dato," padre=",padre.dato)
    if padre.dato == dato:
      print("salgo con un valor repetido ",dato)
      return
    if dato > padre.dato:
      if padre.der == None:
        padre.der = Nodo(dato)
      else:
        self.inserta(padre.der, dato)
    else:
      if padre.izq == None:
        padre.izq = Nodo(dato)
      else:
        self.inserta(padre.izq, dato)
    print("salgo de inserta con ",dato)

  def add(self, dato):
    inicio = time.time_ns()
    print("INSERTO",dato)
    if self.raiz == None:
      self.raiz = Nodo(dato)
      print("coloqué la raíz con ", dato)
    else:
      self.inserta(self.raiz, dato)
    final = time.time_ns()
    total_time = ((final - inicio)/1e8)
    print("Duración: ", total_time)

  def enorden(self, padre):
      if padre.izq != None:
        self.enorden(padre.izq)
      print(padre.dato)
      if padre.der != None:
        self.enorden(padre.der)
        
  def inorder(self):
    if self.raiz != None:
      self.enorden(self.raiz)
    else:
      print("El árbol está vacío")

  def preorden(self,padre):
    if padre != None:
      print(padre.dato)
      self.preorden(padre.izq)
      self.preorden(padre.der)
    
  def preorder(self):
    if self.raiz != None:
      self.preorden(self.raiz)
    else:
      print("El árbol está vacío")
      
  def postorden(self,padre):
    if padre.izq != None:
      self.postorden(padre.izq)
    if padre.der != None:
      self.postorden(padre.der)
    print(padre.dato)
      
  def postorder(self):
    if self.raiz != None:
      self.postorden(self.raiz)
    else:
      print("El árbol está vacío")
      
    
    
arbol = Binario()

arbol.add(5)
arbol.add(5)
arbol.add(8)
arbol.add(4)
arbol.add(10)
arbol.add(12)
arbol.add(9)
arbol.add(30)
arbol.add(40)
arbol.add(25)


print("EN ORDEN")
arbol.inorder()
print("PRE-ORDEN")
arbol.preorder()
print("POST ORDEN")
arbol.postorder()

#arbol.delete(3)

#arbol.search(14)
#arbol.search(10)

print("terminé")


'''
  def porDer(padre ,hijo):
    sustituto = None
    while hijo.izq != None:
      padre = hijo.izq
      hijo = padre.izq
    sustituto = hijo
    padre.der = hijo.der
    return sustituto

  def porIzq(padre ,hijo):
    sustituto = None
    while hijo.der != None:
      padre = hijo.der
      hijo = padre.der
    sustituto = _hijo
    padre.izq = _hijo.izq
    return sustituto

  def elimina(padre ,dato):
    sustituto = None
    if dato == padre:
     	sustituto = porIzq(padre ,padre.izq)
     	if sustituto == None:
        sustituto = porDer(padre ,padre.der)
      if sustituto == null:
   		 	  # BORRAR AL PADRE
          return null;
        else:
          padre.dato = sustituto.dato
      else:
        # BUSCAR POR LA IZQUIERDA O LA DERECHA AL NODO A ELIMINAR
        return null

  def delete(self, dato):
    if self.raiz != None:
      self.borrar(self.raiz, dato)
      
'''
