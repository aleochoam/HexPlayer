from random import randint
# Cambiar por funcion de evaluación

def value(node):
  if len(node.succesors) == 0:
    return getUtility(node)

  if node.isMax:
    return maxValue(node)
  else:
    return expValue(node)

def maxValue(node):
  value = -inf

  if len(node.getSuccesors()) == 0:
    value = getUtility(node)
  else:
    for child in node.succesors:
      value = max(v, value(child))
  return value

def expValue(node):
  value = 0

  if len(node.getSuccesors()) == 0:
    value = getUtility(node)

  else:
    for child in node.succesors:
      p = 1/len(node.succesors)
      value = value + p*value(child)
  return values

def getUtility(node):
  # Hacer algo magico
  return int(random()*1000)