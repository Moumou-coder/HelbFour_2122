import re

# Ouverture du fichier
filePath = "./resource/transact_log.txt"
readModeFile = 'r'
f = open(filePath, readModeFile)

# init variables réutilisables
countLine = 0
charBegins = 0
charEnd = 0

# les jours les plus lucratifs entre 2014 - 2020
keyYear = ""
numberOfProduct = 0
yearsDict = {
    "2014": numberOfProduct,
    "2015": numberOfProduct,
    "2016": numberOfProduct,
    "2017": numberOfProduct,
    "2018": numberOfProduct,
    "2019": numberOfProduct,
    "2020": numberOfProduct,
}

keyDay = ""
valueCountProduct = 0
daysDict = {
    "Monday": valueCountProduct,
    "Tuesday": valueCountProduct,
    "Wednesday": valueCountProduct,
    "Thursday": valueCountProduct,
    "Friday": valueCountProduct,
    "Saturday": valueCountProduct,
}

for line in f:
    # Définir les années où il y a eu le plus de ventes entre 2014 - 2020
    if re.match("[Year:]", line):
        charBegins = line.index(":") + 1
        charEnd = line.index("*")
        keyYear = line[charBegins:charEnd]

    # Définir le jour où il y a eu le plus de ventes entre 2014 - 2020
    if re.match("[Day:]", line):
        charBegins = line.index(":") + 1
        charEnd = line.index("-")
        keyDay = line[charBegins:charEnd]

    # Rajouter dans les hashMap
    if line.startswith("["):
        numberOfProduct = line.count('p')
        yearsDict[keyYear] = yearsDict.get(keyYear) + numberOfProduct

        valueCountProduct = line.count('p')
        daysDict[keyDay] = daysDict.get(keyDay) + valueCountProduct

# gaph en nuage de points - évolution durant les années
print(yearsDict)
# graph Histogram
print(daysDict)

################################################# Réponse Q 2 #############################################
from itertools import combinations

# Ouverture du fichier
filePath = "./resource/test.txt"
readModeFile = 'r'
f = open(filePath, readModeFile)

for lineOfProduct in f:
    if lineOfProduct.startswith("["):
        listProduct = eval(lineOfProduct)
        listComb = combinations(listProduct, 2)
        print(list(listComb))


# refaire l'exo du cours




