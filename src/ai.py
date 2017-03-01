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

def expandChangeNode(node, player):
  state = node.state
  root = _getRoot(node)
  moves = getPosibleMoves(node.state, node.changset, player)
  node.addSuccesor(None, node.changset.extend(moves))

def _getRoot(node):
  root = node
  while root is not None:
    root = node.parent
  return root

def getPosibleMoves(state, moves, player):
  for move in moves:
    state[move[0]][move[1]] = player

  newMoves = []
  for col in range(len(state)):
    for row in range(len(state)):
      if state[col][row] == 0:
        newMoves.append((player, [col,row]))
  return newMoves


"""Evalua si dado un estado, hay una conexion virtual"""
def hasVirtualConnection(node, player):
  board = node.state
  size = len(board)

  if player == 1:
    for y in range(size):
      for x in range(size):
        if y < size-2 and 1 < x < size-2:
          if board[y][x] == player:
            if ((board[y+1][x+1] == player and board[y+1][x] == 0 and board[y][x+1] == 0) or
                (board[y+2][x-1] == player and board[y+1][x-1] == 0 and board[y+1][x] == 0) or
                (board[y+1][x-2] == player and board[y][x-1] == 0 and board[y+1][x+1] == 0)):
              return True


  if player == 2:
    for y in range(size):
      for x in range(size):
        if x < size-2:
          if board[y][x] == player:
            if ((board[y+1][x+1] == player and board[y][x+1] == 0 and board[y+1][x] == 0) or
                (board[y-1][x+2] == player and board[y][x+1] == 0 and board[y+1][x+1] == 0) or
                (board[y-2][x+1] == player and board[y+1][x] == 0 and board[y][x+1] == 0)):
               return True
  return False
