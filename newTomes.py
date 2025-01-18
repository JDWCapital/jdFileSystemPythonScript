import os

dire = "/home/jake/jd/"
counter = [0]
counterMax = [len(os.listdir(dire))]
direList = sorted(os.listdir(dire))
scripture = []
scripture.append("# Tome of Indexes")
tomePath = "/home/jake/jd/00-09/00/00.00_index/tomeOfIndexes.md"
while counter[-1] <= counterMax[-1]:
    suspect = direList[counter[-1]]
    counter[-1] += 1
    if os.path.isfile(dire+suspect) == True:
        line = "[["+dire+suspect+"]]"
    else:
        line = "#" * len(counter) + " " + suspect
    scripture.append(line)
    if suspect[0] != "." and os.path.isfile(dire+suspect) == False:
        counter.append(0)
        dire = dire + str(suspect) + "/"
        counterMax.append(len(os.listdir(dire)))
        direList = sorted(os.listdir(dire))
    # go back
    while counter[-1] == counterMax[-1]:
        counter.pop()
        counterMax.pop()
        modify = dire.split("/")
        modify.pop()
        modify.pop()
        dire = "/".join(modify) + "/"
        direList = sorted(os.listdir(dire))
        if len(counter) == 0:
            print("DONE")
            break
    if len(counter) == 0:
        break

with open(tomePath, "w") as file:
    file.write("\n".join(scripture))

