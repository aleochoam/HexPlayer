MAXDEPTH = 10
# Cambiar por funcion de evaluación

def value(state, depth=0):
  if len(state.succesors) == 0:
    return state.utility

  if depth >= MAXDEPTH:
    return evaluate(state)

  if state.isMax:
    return maxValue(state, depth++)
  else:
    return expValue(state, depth++)

def maxValue(state, depth):
  if depth >= MAXDEPTH:
    return evaluate(state)

  value = -inf
  for child in state.succesors:
    value = max(v, value(child, depth++))
  return value

def expValue(state, depth):
  if depth >= MAXDEPTH:
    return evaluate(state)

  value = 0
  for child in state.succesors:
    p = 1/len(state.succesors)
    value = value + p*value(child, depth++)
  return values

def evaluate(state):
  # Funcion magica de evaluacion