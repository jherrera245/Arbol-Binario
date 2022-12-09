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
                nodoTemporal.izquierda = nodoTemporal.izquierda.remove(nodoIzquierda.data)
            elif self.izquierda is not None:
                nodo = self.izquierda
            elif self.derecha is not None:
                nodo = self.derecha
            else:
                nodo = None
        return nodo 

    #buscar un elemento del arbol
    def search(self, data):
        return self.findInNode(self, data)

    def findInNode(self, node, data):
        if node is None:
            return False
        elif isinstance(node.data, Tree):
            if isinstance(node.data.izquierda, Tree):
                return self.findInNode(node.data.izquierda, data)
            elif isinstance(node.data.derecha, Tree):
                return self.findInNode(node.data.derecha, data)
        elif data < node.data:
            return self.findInNode(node.izquierda, data)
        elif data > node.data:
            return self.findInNode(node.derecha, data)
        elif data == node.data:
            return True
        else:
            return False

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
