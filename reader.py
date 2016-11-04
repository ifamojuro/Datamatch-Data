import numpy
import csv

data = open('data.txt','r')
lines = data.readlines()
#print lines[4195].split(':')

matcheshistogram=[] 
for i in range(30):
	matcheshistogram.append(0)

for i in range(4196):
	matcheshistogram[len(lines[i].split(':')) - 5]+=1

def lookup_attribute(id_number,attribute_number):
	for i in range(4196):
		line = lines[i].split(':')
		if line[0]==id_number:
			return line[attribute_number]


def housenumber(residence):
	if residence == "Leverett":
		return 1
	elif residence == "Kirkland":
		return 2
	elif residence == "Cabot":
		return 3
	elif residence == "Lowell":
		return 4 
	elif residence == "Adams":
		return 5
	elif residence =="Dunster":
		return 6
	elif residence =="Mather":
		return 7
	elif residence =="Winthrop":
		return 8
	elif residence == "Pforzheimer":
		return 9
	elif residence =="Currier":
		return 10
	elif residence =="Quincy":
		return 11
	elif residence =="Eliot":
		return 12
	else:
		return 13


matches = numpy.zeros((13,13), dtype=numpy.int)
for i in range(4196):
	line = lines[i].split(':')
	length = len(line)
	#Max length = 24, max matches =24-5=19
	#First make all rows the same length, length 24
	for i in range(24-length):
		line.append(0)
	index, year, house, gender, seeking, match1, match2, match3, match4, match5, match6, match7, match8, match9, match10, match11, match12, match13, match14, match15, match16, match17, match18, match19=line
	personhouse = housenumber(house)
	for j in range(length-5): #Number of matches
		match = line[5+j]
		matcharray=match.split(',')
		targethouse = housenumber(lookup_attribute(matcharray[0],2))
		matches[personhouse-1][targethouse-1] +=1
print matches 

file1=open('matchmatrix.csv','wb')
writer = csv.writer(file1)
listhouses = ["Leverett", "Kirkland", "Cabot", "Lowell", "Adams", "Dunster", "Mather", "Winthrop", "Phorzheimer", "Currier", "Quincy", "Eliot", "Freshman"]
writer.writerow(listhouses)
for i in range(13):
	writer.writerow([listhouses[i], matches[i]])


