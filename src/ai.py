import numpy as np
from changeNode import ChangeNode
from expectimax import value

"""
Modulo de inteligencia artificial, evaluacion de estados y expansion de nodos
"""

"""FUNCION PRINCIPAL, dado un tablero y un jugador, retorna la mejor jugada"""
def Agente_JuanDaniel_Alejandro(board, player):
  adversary = 0
  if player == 1:
    adversary == 2
  else:
    adversary == 1

  root = Node(None, board)
  expandNode(root, player)
  for child in root.getSuccesors():
    expandNode(root, adversary)
    for grandChildren in child.getSuccesors():
      expandNode(grandChildren, player)

  bestNode = None
  for child in root.getSuccesors():
    nodeValue = value(child)
    child.value = nodeValue

    if bestNode.value < nodeValue:
      bestNode = child

  return bestNode.changeset[1]

"""Agente que juega por reflejo"""
def reflexAgent(board, player):
  # moves = countMoves(board)
  if player == 1:
    if board[3][4] == 0:
      return (3,4)
    elif board[5][3] == 0:
      return (5,3)
    elif board[6][4] == 0:
      return (6,4)
    elif  board[7][5] == 0:
      return (7,5)
  else:
    if board[4][3] == 0:
      return (4,3)
    elif board[3][5] == 0:
      return (3,5)
    elif board[4][6] == 0:
      return (4,6)
    elif  board[5][7] == 0:
      return (5,7)

"""Cuenta cuantas jugadas se han hecho en un tablero"""
def countMoves(board):
  count = 0
  for y in len(board):
    for x in len(board):
      if board[y][x] == 1 or board[y][x] == 2:
        count += 1

  return count

"""Retorna un subtablero de un tablero dada un jugador y un tamaño"""
def playOnSubMatch(board, size, player):
  center = int(len(board)/2)
  if player == 1:
    newBoard = []
    board = board.tolist()
    for row in board:
      newBoard.append(row[center-size:center+size])
    return np.array(newBoard)
  else:
    return board[center-size:center+size]

"""Asigna los hijos con todos los posibles estados a un nodo dado"""
def expandChangeNode(node, player):
  state = node.state
  root = _getRoot(node)
  moves = getPosibleMoves(root.state, node.changeset, player)
  for newMove in moves:
    newChangeset = node.changeset + [newMove]
    node.addSuccesor(None, newChangeset)

"""retorna la raiz de un arbol"""
def _getRoot(node):
  root = node
  while root.parent is not None:
    root = root.parent
  return root

# move[numeroJugador][y,x]
"""Retorna una lista de posibles jugadas que se pueden hacer dado un estado"""
def getPosibleMoves(state, moves, player):
  newBoard = np.copy(state)
  for move in moves:
    newBoard[move[1][0]][move[1][1]] = move[0]

  newMoves = []
  for col in range(len(state)):
    for row in range(len(state)):
      if newBoard[col][row] == 0:
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
            if ((board[y+1][x+1] == player and board[y+1][x] == 0 and \
                  board[y][x+1] == 0) or
                (board[y+2][x-1] == player and board[y+1][x-1] == 0 and \
                  board[y+1][x] == 0) or
                (board[y+1][x-2] == player and board[y][x-1] == 0 and \
                  board[y+1][x+1] == 0)):

              return True


  if player == 2:
    for y in range(size):
      for x in range(size):
        if x < size-2:
          if board[y][x] == player:
            if ((board[y+1][x+1] == player and board[y][x+1] == 0 and \
                  board[y+1][x] == 0) or
                (board[y-1][x+2] == player and board[y][x+1] == 0 and \
                  board[y+1][x+1] == 0) or
                (board[y-2][x+1] == player and board[y+1][x] == 0 and \
                  board[y][x+1] == 0)):
               return True
  return False

"""Retorna el numero de conexiones que se hacen con una jugada"""
def countNewConnections(board, move):
  count = 0
  y = move[1][0]
  x = move[1][1]
  player = move[0]
  size = len(board)

  if y > 0 and board[y-1][x] == player:
    count += 1

  if y < size-1 and board[y+1][x] == player:
    count += 1

  if x > 0 and board[y][x-1] == player:
    count += 1

  if x < size-1 and board[y][x+1] == player:
    count += 1

  if x < size-1 and y > 0 and board[y-1][x+1] == player:
    count += 1

  if x > 0 and y < size-1 and board[y+1][x-1] == player:
    count += 1

  return count