class Node(object):
  """Clase nodo para realizar arboles n-arios, con un estado de juego"""

  def __init__(self, parent, state):
    self.succesors = []
    self.parent = parent
    self.state = state

  def addSuccesor(parent, state):
    node = Node(parent, state)
    parent.succesors.append(node)

  def getParent(self):
    return self.parent

  def getChild(self, index):
    if self._isIndexValid(index):
      return self.succesors[index]

  def _isIndexValid(self, index):
    if 0 <= index < len(self.succesors):
      return True
    else:
      return False

  def printNode(self):
    print("Tengo " + str(len(self.succesors)))
    for col in self.state:
      for cell in col:
        print(cell, end=" ")
      print("")
