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


# Graphique des jours les plus rentables au niveau de la vente des produits
print(daysDict)
percentDays = 0
totalProduct = daysDict["Monday"] + daysDict["Tuesday"] + daysDict["Wednesday"] + daysDict["Thursday"] + daysDict[
    "Friday"] + daysDict["Saturday"]

daysPercentDict = {
    "Monday": percentDays,
    "Tuesday": percentDays,
    "Wednesday": percentDays,
    "Thursday": percentDays,
    "Friday": percentDays,
    "Saturday": percentDays,
}

i = 0
while i < 6:
    for x in daysPercentDict.keys():
        i += 1
        daysPercentDict[x] = ((daysDict[x] / totalProduct) * 1000) % 100

for d in daysPercentDict.items():
    for i in range(int(d[1])):
        print('🟥', end="")
    print(" :" + d[0], end="")
    print(" ")

print()
# Graphique représentant l'évolution de l'entreprise au niveau entre 2014-2020
print(yearsDict)

################################################# Réponse Q 2 #############################################
from itertools import combinations

# Ouverture du fichier
filePath = "./resource/Tester.txt"
readModeFile = 'r'
f = open(filePath, readModeFile)

productsCombVal = 1
productsCombDict = {
}

for lineOfProduct in f:
    if lineOfProduct.startswith("["):
        listProduct = eval(lineOfProduct)
        listComb = combinations(listProduct, 2)
        for i in list(listComb):
            sortedTupleKey = tuple(sorted(i))
            if sortedTupleKey not in productsCombDict:
                productsCombDict.update({sortedTupleKey: productsCombVal})
            else:
                productsCombDict[sortedTupleKey] = productsCombDict.get(sortedTupleKey) + 1

# todo: regarder le cours - support - confidence - lift
# print(productsCombDict)
