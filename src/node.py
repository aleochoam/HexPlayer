class Node(object):
  """Clase nodo n-ario"""
  utility = NaN
  succesors = []

  def __init__(self, utility):
    self.utility = utility

  def addSuccesor(self, succesor):
    self.succesors.append(succesor)



def makeTree(state):
  root = Node(0)
  # ampliar el nodo, 5 niveles
  for i in range(5):
    ampliarNodo(root)
  return root

def ampliarNodo(root):
  # Agreagar los hijos
  return root