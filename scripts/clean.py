
if __name__ == "__main__":
	f = open("../data/scores.csv", "r")
	d_scores = f.read()
	da_scores = d_scores.split("\n")[:-1]

	f.close()
	
	dta = []

	for item in da_scores:
		dta.append(item.split(',')[:-1])

	max = 0
	for item in dta:
		if len(item) > max:
			max = len(item)

	#print(max)    <----     14    <----- 2OT

	cta = []

	for item in dta:
		if len(item) == 10:   #Regular Game
			a = item[:4]
			a.extend(['0','0'])
			a.append(item[4])
			a.extend(item[5:-1])
			a.extend(['0','0'])
			a.append(item[-1])
			cta.append(a)
		elif len(item) == 12:    #OT1 Games
			a = item[:5]
			a.append('0')
			a.append(item[5])
			a.extend(item[6:-1])
			a.append('0')
			a.append(item[-1])
			cta.append(a)
		else:
			cta.append(item)

	#test
	for idx, item in enumerate(cta):
		if len(item) != 14:
			print(idx)
			print(item)
			print(True)

	g = open("../data/clean.csv", "w")

	for item in cta:
		for idx, attr in enumerate(item):
			if idx == 13:
				g.write(attr)
			else:
				g.write(attr + ",")

		g.write("\n")

	g.close()
