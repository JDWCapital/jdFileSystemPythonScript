import os
dire = "" # input your desired directory location
start = 0

def combination(x, y):
	first = str(x)
	second = str(y)
	file_Name = str(first+"-"+second)
	return file_Name

# the loop below creates the areas (i.e. 00-09, 10-19, etc.)
# it does them all up to 99 per the system but you do have to manually update the first folder
# the function returns it as a 0-9 rather than 00-09
# i cant be bothered changing the code to fix that at the moment
# *only bit of a manual input i swear*

for counter in range(0,10): 
	first_number = 10 * counter
	second_number = 9 + 10 * counter
	dire_name = combination(first_number, second_number)
	os.makedirs(dire+dire_name)

# the below makes all the categories (00 to 99). it houses them in the appropriate
# area too. 

for folder in os.listdir(dire):
	if os.path.isfile(dire+folder) == False:
		for counter in range(0,10):
			os.makedirs(dire+folder+"/"+str(start))
			start += 1

# finally, this loop below inserts the essential ids
# these are the management ids that occupy the first ten ids in every category

for folder in os.listdir(dire):
	if os.path.isfile(dire+folder) == False:
		for folder2 in os.listdir(dire+folder):
			os.makedirs(dire+folder+"/"+folder2+"/"+str(folder2+".00_Index/"))
			os.makedirs(dire+folder+"/"+folder2+"/"+str(folder2+".01_Inbox/"))
			os.makedirs(dire+folder+"/"+folder2+"/"+str(folder2+".02_WiP/"))
			os.makedirs(dire+folder+"/"+folder2+"/"+str(folder2+".03_ToDo/"))
			os.makedirs(dire+folder+"/"+folder2+"/"+str(folder2+".04_Bookmarks/"))
			os.makedirs(dire+folder+"/"+folder2+"/"+str(folder2+".05_Templates/"))
			os.makedirs(dire+folder+"/"+folder2+"/"+str(folder2+".06_/"))
			os.makedirs(dire+folder+"/"+folder2+"/"+str(folder2+".07_/"))
			os.makedirs(dire+folder+"/"+folder2+"/"+str(folder2+".08_Someday/"))
			os.makedirs(dire+folder+"/"+folder2+"/"+str(folder2+".09_Archive/"))