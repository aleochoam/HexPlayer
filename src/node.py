class Node(object):
  """Clase nodo n-ario"""
  utility = 0
  succesors = []

  def __init__(self, utility):
    self.utility = utility

  def addSuccesor(self, succesor):
    self.succesors.append(succesor)