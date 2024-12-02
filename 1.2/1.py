import os

path = os.path.join(os.path.dirname(__file__), "input.txt")

f = open(path, "r")
inp = f.read()

inp = inp.replace("   ", "\n").split("\n")[0:-2]
lista = []
listb = []

for i in range(0, len(inp)):
	if i%2 == 0:
		lista.append(inp[i])
	else:
		listb.append(inp[i])

solution = 0
for t in lista:
    solution += listb.count(t) * int(t)

print(solution)