import random
import matplotlib.pyplot as plt # type: ignore

alphabet = "abcdefghijklmnopqrstuvwxyz"

def randomGraph():
  return ''.join(random.sample(alphabet, len(alphabet)))

def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

def testMethod(tries, graphA, graphB, breedMethod):
  i = 0
  missingLetters = {}
  solutions = []

  while i < tries:
    graphC = breedMethod(graphA, graphB)

    mL = graphC.count("0")
    missingLetters[mL] = missingLetters.get(mL, 0) + 1

    if mL == 0:
      solutions.append(graphC)

    i += 1

  for key, value in missingLetters.items():
    missingLetters[key] = value/float(tries)

  return solutions, missingLetters

def summarizeSolutions(solutions, missingLetters, tries, graphA, graphB):
  print(f"Found a solution {int(missingLetters[0]*tries)} times.")

  print(f"A: {graphA}")
  print(f"B: {graphB}")
  print("----------------")

  for s in solutions[0:20]:
    print(s + (" - is parent" if s == graphA or s == graphB else ""))

def plotSolutions(missingLetters):
  plt.bar(list(missingLetters.keys()), list(missingLetters.values()))
  plt.title("Missing Letter Distribution")
  plt.get_current_fig_manager().set_window_title('Graph Breeding')
  plt.show()

def runFullTest(tries, breedMethod):
  graphA, graphB = randomGraph(), randomGraph()

  print(f"Graph A is: {graphA}")
  print(f"Graph B is: {graphB}")

  solutions, missingLetters = testMethod(tries, graphA, graphB, breedMethod)

  summarizeSolutions(solutions, missingLetters, tries, graphA, graphB)
  plotSolutions(missingLetters)

