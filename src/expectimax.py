# Cambiar por funcion de evaluación

def value(state):
  if len(state.succesors) == 0:
    return state.utility

  if state.isMax:
    return maxValue(state)
  else:
    return expValue(state)

def maxValue(state):
  value = -inf
  for child in state.succesors:
    value = max(v, value(child))
  return value

def expValue(state):
  value = 0
  for child in state.succesors:
    p = 1/len(state.succesors)
    value = value + p*value(child)
  return values