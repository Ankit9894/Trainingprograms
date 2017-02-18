class Matrix:
def __init__(self,)
list1 = []
list2 = []
list3 =[]
inp1 = int(raw_input("ENTER NO OF DIMENTIONS"))
for i in range(inp1):
	row = []
	for j in range(inp1):
		data=input()
		row.append(data)
	list1.append(row)
for i in range(inp1):
	row1 = []
	for j in range(inp1):
		data=input()
		row1.append(data)
	list2.append(row)
print list1
print list2
resultm=[]
for i in range(inp1):
	row2=[]
	for j in range(inp1):
		data=list1[i][j]*list2[i][j]
		row2.append(data)
	resultm.append(row2)
print resultm

		
