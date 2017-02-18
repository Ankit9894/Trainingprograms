class matrix :	
	def __init__(self,array):
		self.array=array
	def __add__(self,other):
		'''if len(self.array==other.array):	
			row_len1=self.array[0]
			row_len2=other.array[1]
			for row in self.array :
				if row.len == len(row):
					return none

		for row in other.array : 
			if row_len2 != len(row) : 	
				return none'''
		new_matrix=[]
		for i in range(len(self.array)):
			row=[]
			for j in range(len(self.array[0])) :
				row.append(self.array[i][j]+other.array[i][j])
				new_matrix.append(row)
			return matrix(new_matrix)

	def __str__(self):
		return str(self.array)
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
	list2.append(row1)
print list1
print list2
m=matrix(list1)
m1=matrix(list2)
print m+m1


			

