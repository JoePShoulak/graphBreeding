from helper import *

def breedEasy(graphA, graphB):
  graphC = " "*26 # null values we know have to be replaced

  while graphC.count(" "): # while he have values to be replaced...
    foundOption = False

    for i in range(len(graphC)):
      optA, optB = graphA[i], graphB[i]

      if graphC.count(optA) * graphC.count(optB) > 0:
        continue # if both options are already in the graph, skip

      foundOption = True

      graphC = list(graphC)

      if graphC.count(optA) * graphC.count(optB) == 0:
        graphC[i] = optA if random.randint(0,1) else optB
      else:
        graphC[i] = optA if graphC.count(optA) == 0 else optB

      graphC = "".join(graphC)

    if not foundOption:
      # Here we would fill in blanks if any are remaining,
      # but they have yet to be found
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
    selection = graphA[index] if random.randint(0,1) else graphB[index]
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
        # we could maybe take all the leftover options, shuffle them,
        # and create a cycle out of them.
        # then we at least end up with a valid graph at the end,
        # as close as we can to being from the parents
        missingLetters = []
        for ch in alphabet:
          if graphC.count(ch) == 0:
            missingLetters.append(ch)

        print(f"No options left with valid choices. Missing letters {missingLetters}.")
        print(f"Graph C is: {graphC}")
        return graphC
  
  return graphC
