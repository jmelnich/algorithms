import sys
import random

def mirror(servers_quantity):
	servers = []
	start = 1
	end = start + 10
	count = 0
	for i in range(0, servers_quantity):
		row = []
		for j in range(start, end):
			row.append(j)
		count += 1
		if count % 2 == 0:
			start += 10
			end = start + 10
		servers.append(row)
	return servers

def randomize(servers_quantity):
	servers = mirror(servers_quantity)
	i = 0
	arr = []
	while i < servers_quantity:
		if i % 2 == 0:
			arr.append(servers[i])
		i += 1

	flat = []
	for sublist in arr:
		for item in sublist:
			flat.append(item)
	cpp_1 = random.sample(flat,len(flat))
	cpp_2 = random.sample(flat,len(flat))

	altogether = []
	k = 0
	i = 0
	while (i < servers_quantity - 1):
		j = 0
		altogether.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
		altogether.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
		while (j < 10):
			altogether[i][j] = cpp_1[k]
			altogether[i + 1][j] = cpp_2[k]
			k += 1
			j += 1
		i += 2
	return(altogether)

def checkFragment(servers, dead_server, fragment):
	row = 0
	while (row < 10):
		if (arr[dead_server][row] == fragment):
			return True
		row += 1
	return False

def getNum(dead_server, servers_quantity, servers):
	count = 0

	srv = 0
	while (srv < servers_quantity):
		if (srv != dead_server):
			row = 0
			while (row < 10):
				if (checkFragment(servers, dead_server, servers[srv][row])):
					count += 1
					break
				row += 1
		srv += 1
	return count

def printResult(count, num):
	res = (100.0 * count) / num 
	print ("Killing 2 arbitrary servers results in data loss in " + str(res) + "% cases")

if(sys.argv[1] == '-n'):
	servers_quantity = int(sys.argv[2])
	if(sys.argv[3] == '--random'):
		arr = randomize(servers_quantity)
	elif(sys.argv[3] == '--mirror'):
		arr = mirror(servers_quantity)
	print(arr)
	count = getNum(0, servers_quantity, arr)
	printResult(count, servers_quantity - 1)
else:
	print ('usage: ./simulate.py -n quantity[int] --method[str]')