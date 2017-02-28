import numpy as np

"""
Modulo de inteligencia artificial, evaluacion de estados y expansion de nodos
"""

"""Asigna los hijos con todos los posibles estados a un nodo dado"""
def Agente_JuanDaniel_Alejandro(board, player):
  root = Node(None, board)
  expandNode(root, player)
  return root

def expandNode(node, player):
  state = node.state
  for col in range(0, len(state)):
    for row in range(0, len(state[col])):
      if state[col][row] == 0:
        child = np.copy(state) #Se podrá cambiar por algo más eficiente?
        child[col][row] = player
        node.addSuccesor(child)

"""Evalua si dado un estado, hay una conexion virtual"""
def hasVirtualConnection(node, player):
  board = node.state
  size = len(board)

  if player == 1:
    for y in range(size):
      for x in range(size):
        if y < size-2 and 1 < x < size-2:
          if board[y][x] == player:
            if (board[y+1][x-1] == player or
                board[y+2][x+1] == player or
                board[y+1][x+2] == player):
              return True


  if player == 2:
    for y in range(size):
      for x in range(size):
        if x < size-2:
          if board[y][x] == player:
            if (board[y-1][x+1] == player or
                board[y+1][x+2] == player or
                board[y+2][x+1] == player):
               return True
  return False
