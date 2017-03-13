import numpy as np
from changeNode import ChangeNode
import minimax
import expectimax

"""
Modulo de inteligencia artificial, evaluacion de estados y expansion de nodos
"""

"""FUNCION PRINCIPAL, dado un tablero y un jugador, retorna la mejor jugada"""
def Agente_JuanDaniel_Alejandro(board, player):
  adversary = 0
  if player == 1:
    adversary = 2
  else:
    adversary = 1

  # Se juega por reflejo
  reflejo = reflexAgent(board, player)
  if reflejo is not None:
    return reflejo
  onSub = False
  numMoves = countMoves(board)
  if numMoves <= 50:
    delta = int(numMoves/10)
    if(delta<=3):
      delta = 3
    newBoard = playOnSubMatch(board, delta, player)
    onSub = True
    root = ChangeNode(None, newBoard, [], True)
  else:
    root = ChangeNode(None, board, [], True)
  expandChangeNode(root, player, False)
  for child in root.getSuccesors():
    expandChangeNode(child, adversary, True)
    for grandChildren in child.getSuccesors():
      expandChangeNode(grandChildren, player, False)
#  print(root.state)
  root.state = board
#  print(root.state)
  if numMoves < 100:
    res = expectimax.value(root)
  else:
    res = minimax.value(root)
  move = None
  max = 0

  for node in root.getSuccesors():
    if(node.value >= max):
#      print("Entre.")
      max = node.value
      move = node.changeset[-1][1]
#  print(max)
#  print(move)
  if(onSub):
    if(player == 1):
      return [move[0], move[1]+(5-delta)]
    else:
      return [move[0]+(5-delta),move[1]]
  else:
    return move
"""Agente que juega por reflejo"""
def reflexAgent(board, player):
  # moves = countMoves(board)
  mid = int(len(board)/2)
  if board[mid][mid] == 0:
    return [mid, mid]

  if player == 1:
    if board[3][4] == 0:
      return [3,4]
    elif board[5][3] == 0:
      return [5,3]
    elif board[6][4] == 0:
      return [6,4]
    elif  board[7][5] == 0:
      return [7,5]
  else:
    if board[4][3] == 0:
      return [4,3]
    elif board[3][5] == 0:
      return [3,5]
    elif board[4][6] == 0:
      return [4,6]
    elif  board[5][7] == 0:
      return [5,7]

"""Cuenta cuantas jugadas se han hecho en un tablero"""
def countMoves(board):
  count = 0
  for y in range(len(board)):
    for x in range(len(board)):
      if board[y][x] == 1 or board[y][x] == 2:
        count += 1

  return count

"""Retorna un subtablero de un tablero dada un jugador y un tamaño"""
def playOnSubMatch(board, size, player):
  center = int(len(board)/2)
  if player == 1:
    newBoard = []
    # board = board.tolist()
    for row in board:
      newBoard.append(row[center-size:center+size+1])
    # return np.array(newBoard)
    return newBoard
  else:
    return board[center-size:center+size+1]

"""Asigna los hijos con todos los posibles estados a un nodo dado"""
def expandChangeNode(node, player, isMax):
  state = node.state
  root = node.getRoot()
  moves = getPosibleMoves(root.state, node.changeset, player)
  for newMove in moves:
    newChangeset = node.changeset + [newMove]
    node.addSuccesor(None, newChangeset, not isMax)

# move[numeroJugador][y,x]
"""Retorna una lista de posibles jugadas que se pueden hacer dado un estado"""
def getPosibleMoves(state, moves, player):
  newBoard = np.copy(state)
  for move in moves:
    newBoard[move[1][0]][move[1][1]] = move[0]

  newMoves = []
  for col in range(len(state)):
    for row in range(len(state[col])):
      if newBoard[col][row] == 0:
        newMoves.append((player, [col,row]))
  return newMoves


"""Evalua si dado un estado, hay una conexion virtual"""
def hasVirtualConnection(board, player):
  # board = node.state
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

def isNotBlocked(board, move):
  size = len(board)
  y = move[1][0]
  x = move[1][1]
  player = move[0]
  adversary = 0
  if player == 1:
    adversary = 2
  else:
    adversary = 1

  if player == 1:
    if y < size-1 and x > 0 and board[y+1][x] == adversary and \
      board[y+1][x-1] == adversary:

      return True

  if player == 2:
    if x < size-1 and y > 0 and board[y][x+1] == adversary and \
      board[y-1][x+1] == adversary:

      return True

  return False

# con una jugada, que tan larga genero una linea
# Que tan cerca quedo de los bordes ((11-dIzq)/11)*((11-dDer)/11)
def countLenLine(board, move):
  # size = len(board)
  y = move[1][0]
  x = move[1][1]
  player = move[0]

  return countForwards(board, player, y, x, 0) + countBackwards(board, player, y, x, 0)


def countBackwards(board, player ,i, j, count):
  try:
    if player == 1:
      if i == 0:
        return 20, i

      if board[i-1][j] == 1:
        return countBackwards(board, player, i-1, j, count + 1)
      if board[i-1][j+1] == 1:
        return countBackwards(board, player, i-1, j+1, count + 1)
      return count, i

    if player == 2:
      if j == 0:
        return 20, j
      if board[i][j-1] == 2:
        return countBackwards(board, player, i, j-1, count+1)
      if board[i-1][j-1] == 2:
        return countBackwards(board, player, i-1, j-1, count+1)
      return count, j

  except Exception:
    return count, i

def countForwards(board, player, i, j, count):
  try:
    if player == 1:
      if i == 10:
        return 20, i
      if board[i+1][j] == 1:
        return countForwards(board, player, i+1, j, count+1)
      if board[i+1][j-1] == 1:
        return countForwards(board, player, i+1, j-1, count+1)
      return count, i

    if player == 2:
      if j == 10:
        return 20, j
      if board[i][j+1] == 2:
        return countForwards(board, player, i, j+1, count+1)
      if board[i-1][j+1] == 2:
        return countForwards(board, player, i-1, j+1, count+1)
      return count, j

  except Exception as e:
    return count, j