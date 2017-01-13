def main():
	#read file
	file = open ( "/Users/kbeattie/Desktop/yesno.txt", "r" )
	lines = file.readlines()
	file.close()

	#look for patterns
	countYES = 0
	countNO  = 0
	for line in lines:
		line = line.strip().upper()
		# print ( line )
		if line.find("YES")!= -1 and len(line)==3:
			countYES = countYES + 1
		if line.find("NO") != -1 and len(line)==2:
			countNO  = countNO + 1

	# display result
	print( "Yes: ", countYES)
	print( "No:  ", countNO)

main()