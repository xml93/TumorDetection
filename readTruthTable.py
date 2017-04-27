import csv

# This file reads the provided CSV file and evaluates the
# most probable cancer location by comparing all radiologists 
# opinions (taking the average) and returning it as a dictionary
def getTruthDict():
	truthDict = {}
	tempList = []
	with open('truth-table.csv', 'rb') as csvfile:
		cvsReader = csv.reader(csvfile, delimiter=';')
		count = 0
		toggle = 0
		for row in cvsReader:
			if toggle == 0:
				toggle = 1
			else :
				tempList = tempList + row[4].split(", ")
				count += 1
				if count == 3:
					highestVal = 0
					highestNum = 0
					for i in range(7):
						print(tempList.count(str(i)))
						if(tempList.count(str(i)) > highestVal):
							highestNum = i
							highestVal = tempList.count(i)
					truthDict[row[0]] = highestNum
					count = 0
					del tempList[:]

	return truthDict

