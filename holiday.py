k = []
while True:
	a = input()
	if a == '':
		break
	else:
		k.append(a.lower())
l=['sunday','saturday']
for i in k:
	if i in l:
		print("yes")
	else :
		print("no")
