from random import randint
from helper import find, alphabet

def breedEasy(graphA, graphB):
  graphC = " "*26 # null values we know have to be replaced

  while graphC.count(" "): # while he have values to be replaced...
    foundOption = False

    for i in range(len(graphC)):
      pathA, pathB = graphA[i], graphB[i]

      if graphC.count(pathA) * graphC.count(pathB): # if the count of both paths are non-zero
        continue # skip and hope we find another before giving up

      foundOption = True

      graphC = list(graphC)

      if not graphC.count(pathA) + graphC.count(pathB): # if the count of both are zero
        graphC[i] = pathA if randint(0,1) else pathB
      else:
        graphC[i] = pathB if graphC.count(pathA) else pathB

      graphC = "".join(graphC)

    if not foundOption:
      # Here we would fill in missing parts of the graph, if we want to
      return graphC
  
  return graphC

def breedHard(graphA, graphB):
  graphC = " "*26 # null values we know have to be replaced
  index, selection = 0, "a"

  while graphC.count(" "): # while he have values to be replaced...
    print(f"Letter {selection} (index {index}):")
    print(f"  Option A: {graphA[index]}")
    print(f"  Option B: {graphB[index]}")

    # get a random path forward from one of the parents
    selection = graphA[index] if randint(0,1) else graphB[index]
    print(f"  Selection: {selection}")

    # if that letter hasn't been in our graph yet, add it and update our index
    if graphC.count(selection) == 0:  
      lGraph = list(graphC)
      lGraph[index] = selection
      graphC = "".join(lGraph)

      index = ord(selection) - 97
    else: # if we can't follow that choice, iterate over all replaceable slots
      foundOption = False
      options = find(graphC, " ")
      letters = list(map(lambda i: alphabet[i], options))
      print(f"Selection already in graph, trying new positions from {options} ({letters})")

      for i in options: # for all our replaceable slots...
        # if neither choice can work, skip it (it helps us fill in as much as we can)
        if (graphC.count(graphA[i]) * graphC.count(graphB[i])) == 0:
          foundOption = True
          index = i
          selection = alphabet[index]
          break

      if not foundOption:
        # if none of the remaining options have valid choices, quit
        missingLetters = []
        for ch in alphabet:
          if graphC.count(ch) == 0:
            missingLetters.append(ch)

        print(f"No options left with valid choices. Missing letters {missingLetters}.")
        print(f"Graph C is: {graphC}")

        # Here we would fill in missing parts of the graph, if we want to

        return graphC
  
  return graphC
