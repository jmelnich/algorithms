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
	altogether = cpp_1 + cpp_2
	print(altogether)





if(sys.argv[1] == '-n'):
	servers_quantity = int(sys.argv[2])
	randomize(servers_quantity)
else:
	print ('usage: ./simulate.py -n quantity[int] --method[str]')