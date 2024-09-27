from sys import argv

from helper import runTest
from breedingMethods import *

if len(argv) < 2:
  print("pick a breeding method: [easy|hard]")
  print("tries can also be specified: [method] <tries>")
  exit()

methodName = argv[1]

if not ["easy", "hard"].count(methodName):
  print("invalid breeding method: [easy|hard]")
  exit()

tries = int(argv[2]) if len(argv) == 3 and argv[2].isnumeric() else 1000

runTest(tries, breedEasy if methodName == "easy" else breedHard)
