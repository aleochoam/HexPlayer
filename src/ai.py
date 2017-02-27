from copy import deepcopy

def expandNode(node, player):
  state = node.state
  for col in range(0, len(state)):
    for row in range(0, len(state[col])):
      if state[col][row] == 0:
        child = deepcopy(state) #Se podrá cambiar por algo más eficiente?
        child[col][row] = player
        node.addSuccesor(child)

