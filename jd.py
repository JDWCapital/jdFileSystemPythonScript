import os
dire = "C:/jd/"

for counter in range(0,10):
    if counter == 0:
        area_begin = "00"
        area_end = "09"
    else:
        area_begin = counter * 10
        area_end = counter * 10 + 9
    dire_name = str(area_begin) + "-" + str(area_end)
    os.makedirs(dire + dire_name)

loop_counter = 0 

for folder in os.listdir(dire):
    if os.path.isfile(dire+folder) == False:
        for counter in range(0,10):
            if loop_counter == 0:
                dire_name = "0" + str(counter)
            else:
                dire_name = str(loop_counter * 10 + counter)
            os.makedirs(dire + folder + "/" + dire_name)
        loop_counter += 1

mgmtIDs = [".00_index",".01_inbox",".02_WiP",".03_todo",
           ".04_bookmarks",".05_templates",".06_",".07_",
           ".08_someday",".09_archive"]

for folder in os.listdir(dire):
    if os.path.isfile(dire + folder) == False:
        for folder2 in os.listdir(dire + folder):
            for iD in mgmtIDs:
                os.makedirs(dire + folder + "/" + folder2 + \
                "/" + folder2 + iD)

system_index = dire + "00-09/00/00.00_index/index.txt"
index_list = []

for counter in range(0,10):
    if counter == 0:
        area_begin = "00"
        area_end = "09"
    else:
        area_begin = counter * 10
        area_end = counter * 10 + 9
    dire_name = "|_" + str(area_begin) + "-" + str(area_end) + " - "
    index_list.append(dire_name)
    for cat in range(0,10):
        cat = 10 * counter + cat
        if cat <= 9:
            cat = "0" + str(cat)
        dire_name = "|      |_" + str(cat) + " - "
        index_list.append(dire_name)

with open(system_index, "w") as file:
    file.write("\n".join(index_list))
