import statistics
 
f = open("diabetes.txt", "r")
f2 = open("diabetes-type.txt", "r")
 
dictionary = {}
dictionary2 = {}
 
 
def unique(attribute, _list):
    _uniqueList = []
    for element in _list:
        if element not in _uniqueList:
            _uniqueList.append(element)
 
    print("Liczba unikalnych wartości atrubutu {}: {}".format(attribute, len(_uniqueList)))
    print("Unikalne wartości atrybutu {}".format(attribute))
    # for element in _uniqueList:
    print(_uniqueList)
 
 
for x in f2:
    line = x
    line = line.strip()
    line = line.split(" ")
    dictionary2[line[0]] = line[1]
 
indexesOfNumbers = []
i = 0
for key in dictionary2:
    if dictionary2[key] == "n":
        indexesOfNumbers.append(i)
    i += 1
 
for x in f:
    line = x
    line = line.strip()
    line = line.split(" ")
 
    lineCopy = []
    n = 0
    for item in line:
        if n in indexesOfNumbers:
            lineCopy.append(float(item))
        else:
            lineCopy.append(item)
        n += 1
    line = lineCopy
 
    if line[-1] in dictionary:
        dictionary[line[-1]] = dictionary.get(line[-1]) + [line]
    else:
        dictionary[line[-1]] = [line]
 
print("-------------------------")
print("Istniejące klasy decycyzyjne + liczba elementów w klasie: ")
print("-------------------------")
 
for key in dictionary:
    print("{}, liczba elementów: {}".format(key, len(dictionary[key])))
 
print("-------------------------")
print("Max i min:")
print("-------------------------")
 
for indexesOfNumber in indexesOfNumbers:
    listOfAttributes = []
    listOfAttributesByKey = {}
 
    for key in dictionary:
        listByKeys = []
        for value in dictionary[key]:
            listOfAttributes.append(value[indexesOfNumber])
            listByKeys.append(value[indexesOfNumber])
        listOfAttributesByKey[key] = listByKeys
 
    print("------------------------------------------------------------------")
    print("------------------------------------------------------------------")
    print("{} Max: {}; Min {}".format("a{}".format(str(indexesOfNumber + 1)), max(listOfAttributes),
                                      min(listOfAttributes)))
    unique("a{}".format(indexesOfNumber+1), listOfAttributes)
    print("Odchylenie standardowe atrybutu {}, wynosi: {}".format(indexesOfNumber+1, statistics.stdev(listOfAttributes)))
    print("-------------------------")
    for key in listOfAttributesByKey:
        print("Odchylenie standardowe atrybutu {} w klasie decyzyjnej {}, wynosi: {}".format(indexesOfNumber+1, key, statistics.stdev(listOfAttributesByKey[key])))
 
 
print("-------------------------")
