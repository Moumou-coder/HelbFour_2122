# Import
import re

# Ouverture du fichier
filePath = "./resource/transact_log.txt"
readModeFile = 'r'
f = open(filePath, readModeFile)
numberOfClients = 0
# initialisation d'un dictionnaire (jours)
daysDict = {
    "Monday": numberOfClients,
    "Tuesday": numberOfClients,
    "Wednesday": numberOfClients,
    "Thursday": numberOfClients,
    "Friday": numberOfClients,
    "Saturday": numberOfClients,
}

# les jours les plus lucratifs entre 2014 - 2020
keyDay = ""
countLine = 0
valueCountProduct = 0
charBegins = 0
charEnd = 0
for line in f:
    countLine += 1
    if countLine <= 2:
        continue
    # Définir le jour où il y a eu le plus de ventes entre 2014 - 2020
    if re.match("^[Day : ]", line):
        charBegins = line.index(":") + 1
        charEnd = line.index("-")
        keyDay = line[charBegins:charEnd]
    else:
        valueCountProduct = line.count('p')
        daysDict[keyDay] = daysDict.get(keyDay) + valueCountProduct

print(daysDict)

# 
