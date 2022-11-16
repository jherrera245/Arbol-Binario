class Tree:

    def __init__(self, data):
        self.data = data
        self.derecha = None
        self.izquierda = None

    def add(self, data):
        if data < self.data:
            if self.izquierda is None:
                self.izquierda = Tree(data)
            else:
                self.izquierda.add(data)
        else:
            if self.derecha is None:
                self.derecha = Tree(data)
            else:
                self.derecha.add(data)

    def predecessor(self):
        if self.derecha is None:
            return self
        else:
            return self.derecha.predecessor()

    def successor(self):
        if self.izquierda is None:
            return self
        else:
            return self.izquierda.successor()

    def remove(self, data):
        nodo = self
        if data < self.data:
            self.izquierda = self.izquierda.remove(data)
        elif data > self.data:
            self.derecha = self.derecha.remove(data)
        else:
            if self.izquierda is not None and self.derecha is not None:
                nodoTemporal  = self
                nodoIzquierda = self.izquierda.predecessor()
                self.data = nodoIzquierda.data
                nodoTemporal.izquierda = nodoTemporal.remove(nodoIzquierda)
            elif self.izquierda is not None:
                nodo = self.izquierda
            elif self.derecha is not None:
                nodo = self.derecha
            else:
                nodo = None
        return nodo                

    #recolectar los datos desde la raiz desde la izquierda
    def preorder(self, lista = list()):
        lista.append(self.data)

        if self.izquierda is not None:
            self.izquierda.preorder(lista)

        if self.derecha is not None:
            self.derecha.preorder(lista)

        return lista

    def inorder(self, lista = list()):

        if self.izquierda is not None:
            self.izquierda.inorder(lista)

        lista.append(self.data)

        if self.derecha is not None:
            self.derecha.inorder(lista)

        return lista

    def postorder(self, lista = list()):

        if self.izquierda is not None:
            self.izquierda.postorder(lista)

        if self.derecha is not None:
            self.derecha.postorder(lista)

        lista.append(self.data)

        return lista

#importando libreria random
import random

arbol = Tree(30)

#cargamos los datos al rabol de forma aleatorio.
for i in range(0, 99):
    arbol.add(random.randrange(1, 1000, 1))

print("Barridos")
preorder = arbol.preorder()
inorder = arbol.inorder()
postorder = arbol.postorder()

print("Barrido preorder", preorder)
print("\nBarrido postorder", postorder)
print("\nBarrido inorder", inorder)


# idea para contar los numeros pares
pares = 0
for  valor in inorder:
    if valor%2 == 0:
        pares += 1

print("Pares ", pares)

# de nuestros datos escoger el valor a eliminar
remover = input("Que valor quieres remover: ")
remover = int(remover)

arbol.remove(remover)