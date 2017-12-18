"""
Script for the Python Workshop - Final Application
Dec 2017
"""

# #################################
# Lab animals manager 
# #################################

import numpy as np 
from pylab import *

allAnimals = []

myFile = open("scoresAllAnimals.txt", "r")
temp = myFile.read()
myFile.close()
# print(temp)

values = temp.split("\n")
# print(values)
for i in range(len(values)):
	values[i] = values[i].split("\t")
	allAnimals.append(values[i])

# print(allAnimals[0][1])

print("------ Weigths per animal ----------")

for i in range(1, len(allAnimals)): # Start at 1 because of the header
	# print(allAnimals[i])
	animal = allAnimals[i][0]
	idNb = allAnimals[i][1]
	sex = allAnimals[i][3]
	age = int(allAnimals[i][2])
	print("The %s with the ID %s (%s) weights %dg" %(animal, idNb, sex, age))

print("------ Mean scores per animal ----------")

meanScores = []
for i in range(len(allAnimals)):
	if (i!= 0): # Other way to avoid the header
		scoresPerAnimal = []
		animal = allAnimals[i][0]
		idNb = allAnimals[i][1]
		sex = allAnimals[i][3]
		age = int(allAnimals[i][2])
		for j in range (4, len(allAnimals[i])):
			score = int(allAnimals[i][j])
			scoresPerAnimal.append(score)
		# print("Scores:", scoresPerAnimal)
		meanPerAnimal = np.mean(scoresPerAnimal)
		# print("Mean:", meanPerAnimal)
		meanScores.append(meanPerAnimal)
		print("The %s with the ID %s (%s) has a mean score of %f" %(animal, idNb, sex, meanScores[i-1]))

print("------ Plotting the scores evolution per animal ----------")

figure(figsize=(9,7), dpi=80)
suptitle("Evolution of the scores per animal")

for i in range(len(allAnimals)):
	if (i!= 0): # Other way to avoid the header
		scoresPerAnimal = []
		animal = allAnimals[i][0]
		idNb = allAnimals[i][1]
		aniID = allAnimals[i][0] + "_" + allAnimals[i][1]
		# print(aniID)
		for j in range (4, len(allAnimals[i])):
			score = int(allAnimals[i][j])
			scoresPerAnimal.append(score)
		if (animal == 'mouse'):
			subplot(311)
			plot(range(len(scoresPerAnimal)), scoresPerAnimal, label=aniID)
			legend()
			xlabel("Days")
			ylabel("Score")
			xlim(0, 30)
		elif (animal == 'monkey'):
			subplot(312)
			plot(range(len(scoresPerAnimal)), scoresPerAnimal, label=aniID)
			legend()
			xlabel("Days")
			ylabel("Score")
			xlim(0, 30)
		elif (animal == 'bird'):
			subplot(313)
			plot(range(len(scoresPerAnimal)), scoresPerAnimal, label=aniID)
			legend()
			xlabel("Days")
			ylabel("Score")
			xlim(0, 30)

subplots_adjust(hspace=0.35)
show()		

print("------ Plotting mean scores per animal ----------")

meanScores = []
sdScores = []
animalsIDs = []
for i in range(len(allAnimals)):
	if (i!= 0): # Other way to avoid the header
		scoresPerAnimal = []
		animal = allAnimals[i][0]
		idNb = allAnimals[i][1]
		aniID = str(allAnimals[i][0] + "_" + allAnimals[i][1])
		animalsIDs.append(aniID)
		for j in range (4, len(allAnimals[i])):
			score = int(allAnimals[i][j])
			scoresPerAnimal.append(score)
		# print("Scores:", scoresPerAnimal)
		meanPerAnimal = np.mean(scoresPerAnimal)
		sdPerAnimal = np.std(scoresPerAnimal)
		# print("Mean:", meanPerAnimal)
		meanScores.append(meanPerAnimal)
		sdScores.append(sdPerAnimal)

figure(figsize=(9,7), dpi=80)

bar(range(len(meanScores)), meanScores, edgecolor='darkblue', yerr=sdScores)
title("Mean scores per animal")
xlabel("Animals")
ylabel("Mean scores")
xticks(range(len(meanScores)), animalsIDs, rotation=45)

show()

