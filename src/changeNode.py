import numpy as np
import ai

class ChangeNode(object):
  """docstring for ChangeNode"""
  def __init__(self, parent, state, changeset, isMax):
    self.succesors = []
    self.parent = parent
    self.state = np.array(state)
    self.changeset = changeset
    self.value = 0
    self.isMax = isMax

  def addSuccesor(self, state, changeset, isMax):
    # print(changeset)
    node = ChangeNode(self, state, changeset, isMax)
    self.succesors.append(node)

  def printNode(self):
    print("Estado: " + str(self.state))
    print("ChangeSet: " + str(self.changeset))

  def getParent(self):
    return self.parent

  def getChild(self, index):
    if self._isIndexValid(index):
      return self.succesors[index]

  def getSuccesors(self):
    return self.succesors

  def _isIndexValid(self, index):
    if 0 <= index < len(self.succesors):
      return True
    else:
      return False

  """retorna la raiz de un arbol"""
  def getRoot(self):
    root = self
    while root.parent is not None:
      root = root.parent
    return root

  def getState(self):
    board = np.copy(self.getRoot().state)
    for move in self.changeset:
      board[move[1][0]][move[1][1]] = move[0]
    return board

  def getValue(self):
    pesoCV = 2
    pesoNConexiones = 1
    pesoNoBloqueado = 2

    player = self.changeset[-1][0]
    lastMove = self.changeset[-1]
    Mboard = self.getState()

    vc = pesoCV * ai.hasVirtualConnection(Mboard, lastMove)
    nc = pesoNConexiones * ai.countNewConnections(Mboard, lastMove)
    nb = pesoNoBloqueado * ai.isNotBlocked(Mboard, lastMove)
    ll = ai.countLenLine(Mboard, lastMove)
    mo = ((11-ll[1])/11)*ll[0]

    self.value = vc + nc + nb + mo
    # print(self.value)
    # print(vc,nc,nb,ll, " = ", value)
    return self.value