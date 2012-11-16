import json

def main():
	file = open('hurricanes.txt', 'r')
	jsonFile = open('hurricanes.json', 'w')
	jsonFile.write('{ "name": "hurricanes", "children": [ \n')
	first = file.readline()
	for line in file:
		line = line.split()
		year= line[0]
		numStorms = line[1]
		ace = line[7]
		jsonFile.write('\n\t{ "name": ' + year + ' , "numStorms": ' + numStorms + ' , "ace": "' + ace + '" ,"children": [\n')
		for i in range(11,17):
			cat = i - 11 #give category of hurricane
			if cat == 0:
				cat = "tropicalStorm"
			else:
				cat = "cat" + str(cat)
			jsonFile.write('\n\t\t{ "name": "' + cat + '", "number": ' + line[i] + ',"year": ' + year + '}')
			if i != 16:
				jsonFile.write(',')
		jsonFile.write('\n\t] },')		
	jsonFile.write('\n] }')
	file.close()
	jsonFile.close()
	
main()