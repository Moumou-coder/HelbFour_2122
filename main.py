# importations de packages
import re
from itertools import combinations
import operator

# Ouverture du fichier
filePath = "./resource/transact_log.txt"
readModeFile = 'r'
f = open(filePath, readModeFile)

# Les jours les plus lucratifs entre 2014 - 2020
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

charBegins = 0
charEnd = 0

for line in f:
    # Récupérer dynamiquement les années pour les utiliser comme key dans le dictionnaire
    if re.match("[Year:]", line):
        charBegins = line.index(":") + 1
        charEnd = line.index("*")
        keyYear = line[charBegins:charEnd]

    # Récupérer dynamiquement les jours pour les utiliser comme key dans le dictionnaire
    if re.match("[Day:]", line):
        charBegins = line.index(":") + 1
        charEnd = line.index("-")
        keyDay = line[charBegins:charEnd]

    # Rajouter dans le dictionnaire
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
percentYears = 0
yearsPercentDict = {
    "2014": percentYears,
    "2015": percentYears,
    "2016": percentYears,
    "2017": percentYears,
    "2018": percentYears,
    "2019": percentYears,
    "2020": percentYears,
}

j = 0
while j < 7:
    for x in yearsPercentDict.keys():
        j += 1
        yearsPercentDict[x] = ((yearsDict[x] / totalProduct) * 1000) % 100

for y in yearsPercentDict.items():
    for j in range(int(y[1])):
        print('🟥', end="")
    print(" :" + y[0], end="")
    print(" ")

print()
# Question N°2

filePath = "./resource/transact_log.txt"
readModeFile = 'r'
f = open(filePath, readModeFile)

productsCombVal = 1
productsCombDict = {}

# Création de combinaisons
for lineOfProduct in f:
    if lineOfProduct.startswith("["):
        listProduct = eval(lineOfProduct)
        listComb = combinations(listProduct, 2)
        # Ajouter le nombre d'occurrences des combinaisons
        for i in list(listComb):
            sortedTupleKey = tuple(sorted(i))
            if sortedTupleKey not in productsCombDict:
                productsCombDict.update({sortedTupleKey: productsCombVal})
            else:
                productsCombDict[sortedTupleKey] = productsCombDict.get(sortedTupleKey) + 1

# Demander à l'utiliser le classement des combinaisons achetées
topProducts = 0
while True:
    try:
        topProducts = int(input("Veuillez donner un nombre pour le Top ? des combinaisons plus courants : "))
        break
    except ValueError:
        print("\nCeci n'est pas un nombre! Veuillez donner un nombre svp...")

# trier de manière décroissant et afficher le top des combinaisons
sortedDescDict = sorted(productsCombDict.items(), key=lambda item: item[1], reverse=True)
k = 0
while k < topProducts:
    print((k+1), " ---> ", sortedDescDict[k])
    k += 1

# Récupération de la clé et de la valeur de la combinaison de produit ayant le plus d'occurrence
max_key = max(productsCombDict.items(), key=operator.itemgetter(1))[0]
max_value = max(productsCombDict.items(), key=operator.itemgetter(1))[1]
print("voici le groupe de produit le plus vendu: ", max_key, ":", max_value)
