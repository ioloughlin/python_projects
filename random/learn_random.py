import random

rolls = input("Number of rolls: ")

print("Rolling the die", rolls, "times")

outcomes = {'one':0,
	'two':0,
	'three':0,
	'four':0,
	'five':0,
	'six':0
	}

sides = [*outcomes] #list(outcomes.keys())

for i in range(int(rolls)):
	outcomes[ random.choice(sides) ] += 1

print (sides)

total = 0
for v in outcomes.values():
	total += v

print (total)

for k,v in outcomes.items():
	print(k, 'corresponds to', v)
	print(int((v/total)*100), '%')