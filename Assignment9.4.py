while True:
    try:
        fName = input('File Name: ')
        fHandle = open(fName, 'r')
        #print('Handle opened')
        break
    except:
        print('File not found.  Input a file name for a file that exists.')
        continue


counts = {}
for line in fHandle:
    if line.startswith("From ") :
        splitLine = line.split()
        address = splitLine[1]
        counts[address] = counts.get(address, 0) + 1

maxVal = max(counts.values())
for key in counts:
    if counts[key] == maxVal:
        print(key, counts[key])
