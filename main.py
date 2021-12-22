# Ouverture du fichier
filePath = "./resource/testing.txt"
readModeFile = 'r'
f = open(filePath, readModeFile)
numberOfClients = 0
# initialisation d'un dictionnaire (jours)
daysDict= {
    "Monday": numberOfClients,
    "Tuesday": numberOfClients,
    "Wednesday": numberOfClients,
    "Thursday": numberOfClients,
    "Friday": numberOfClients,
    "Saturday": numberOfClients,
}

# les jours les plus lucratifs entre 2014 - 2020
theDay = ""
countMonday = 0
countLine = 0
for l in f:
    countLine += 1
    if countLine <= 2:
        continue
    print(l)




