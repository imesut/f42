#!/usr/bin/env python
# -*- coding: latin-1 -*-

data = open("console.log", "r").readlines()

# array for edges table
items = []
#array for all of data items
fullItmes=[]
# To handle data from raw file, sperated lines
subItem = []
# will contain id and IPC codes
codes = []

setItems = []
singleItems = []

#Checking for duplicate data from raw file
def seekApplyId(id):
	for i in items:
		if i[0] == id:
			return True;

i = 1
for line in data:
	if line.startswith("gatherv3:28 apply_number="):
		subItem = ", ".join(subItem)
		subItem.replace("\n", "").replace("\t", " ")
		subItem = subItem.split("END_OF_DATA")
		if len(subItem) >5:
			# Structured Data definitions
			apply_number = subItem[0].replace("gatherv3:28 apply_number= Başvuru Numarası\t: ", "").replace(", ", "")
			apply_date = subItem[1].replace("apply_date= Başvuru Tarihi	: ", "")
			registration_id = subItem[2].replace("registration_id= Tescil Numarası	: ","")
			registration_date = subItem[3].replace("registration_date= Tescil Tarihi	: ", "")
			protection_type = subItem[4].replace("protection_type= Koruma Tipi	: ", "")
			owner_1 = subItem[5].replace("owner_1=", "").replace(" ,  , ", " ")
			#country = owner_1.split(" ")[-2]
			owner_2 = subItem[6].replace("owner_2=", "").replace(" ,  , ", " ")
			title = subItem[7].replace("title=", "")
			summary = subItem[8].replace("summary=", "")
			ipc_codes = subItem[9].replace("ipc_codes=", "").replace(" ", "").replace("  ", "")
			# Add to lists if not duplicate
			if not seekApplyId(apply_number):
				items.append([apply_number, apply_date, owner_1, ipc_codes])
				fullItmes.append([apply_number, apply_date, registration_id, registration_date, protection_type, owner_1, owner_2, title, summary, ipc_codes])
				codes.append([apply_number, ipc_codes.split(", ")])

			else:
				#print("Duplicate found: " + apply_number)
				pass
			subItem = []
			#print(i)
			#i += 1
	#Eliminate lines which not about patent data
	if not line.startswith("gatherv3:1 undefined"):
		subItem.append(line.replace("\n", " "))



# i = 1
# nodes_info = open("nodes.csv", "w")
# for item in items:
# 	nodes_info.write("===".join(item) + "\n")
# 	#print(i)
# 	i += 1

n = 10

for nodes in codes:
	# n-digit ipc codes
	nodes = [node[:n] for node in nodes[1]]
	for node in nodes:
		for otherNode in nodes[nodes.index(node):]:
			if node != otherNode:
				for item in setItems:
					if (item[0] == node and item[1] == otherNode) or (item[1] == node and item[0] == otherNode):
						item[2] = str(int(item[2])+1)
						break
				else:
					setItems.append([node, otherNode, str(1)])
			else:
				for item in singleItems:
					if item[0] == node:
						item[1] = str(int(item[1])+1)
						break
				else:
					singleItems.append([node, str(1)])

# i = 1
# relations = open(str(n)+"_level_relation.csv", "w")
# for item in setItems:
# 	relations.write("===".join(item) + "\n")
# 	#print(i)
# 	i += 1

uniques = []

for i in setItems:
	for j in range(0,1):
		if not i[j][:4] in uniques:
			uniques.append(i[j][:4])

for i in codes:
	for j in i[1]:
		print(j)
