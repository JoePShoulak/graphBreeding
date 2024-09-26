import random
import matplotlib.pyplot as plt # type: ignore

alphabet = "abcdefghijklmnopqrstuvwxyz"

def randomGraph():
  return ''.join(random.sample(alphabet, len(alphabet)))

def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

def runTest(tries, breedMethod):
  # setup test
  graphA, graphB = randomGraph(), randomGraph()

  print(f"Graph A is: {graphA}")
  print(f"Graph B is: {graphB}")

  # begin test
  i = 0
  missingLetters = {}
  solutions = []

  while i < tries:
    graphC = breedMethod(graphA, graphB)

    mL = graphC.count(" ")
    missingLetters[mL] = missingLetters.get(mL, 0) + 1

    if mL == 0:
      solutions.append(graphC)

    i += 1

  for key, value in missingLetters.items():
    missingLetters[key] = value/float(tries)

  # summarize
  print(f"Found a solution {int(missingLetters[0]*tries)} times.")

  print(f"A: {graphA}")
  print(f"B: {graphB}")
  print("----------------")

  for s in solutions[0:20]:
    print(s + (" - is parent" if s == graphA or s == graphB else ""))
  
  # plot
  plt.bar(list(missingLetters.keys()), list(missingLetters.values()))
  plt.title("Missing Letter Distribution")
  plt.get_current_fig_manager().set_window_title('Graph Breeding')
  plt.show()
