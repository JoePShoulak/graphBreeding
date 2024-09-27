from sys import argv

from helper import runTest
from breedingMethods import *

if len(argv) < 2: # no method
  print("pick a breeding method: [easy|hard]")
  print("tries can also be specified: [method] <tries>")
  exit()

methodName = argv[1]

if not ["easy", "hard"].count(methodName): # wrong method
  print("invalid breeding method: [easy|hard]")
  exit()

tries = int(argv[2]) if len(argv) == 3 and argv[2].isnumeric() else 1000 # you can pass a number of tries, defaults to 1000 (not validated)

runTest(tries, breedEasy if methodName == "easy" else breedHard) # actually run the test and analysis
