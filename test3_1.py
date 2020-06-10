cyclenum = 0

desired_len = 4
listofnums = []

while True:
    newnum = n
    if newnum in listofnums:
        print(cyclenum)
        
        
    x2 = sorted(map(int, str(newnum)), key=int)
    x = int(''.join(str(i) for i in x2))
    
    
    y2 = sorted(map(int, str(newnum)), key=int, reverse=True)
    y = int(''.join(str(i) for i in y2))
    
    
    k = len(str(newnum))
    z = x - y
    
    
    if len(str(z)) != desired_len:
        newz = map(int, str(z))
        lendiff = desired_len - len(str(z))
        newz = list(newz)
        for i in range(0, lendiff):
            newz.insert(0, 0)
    cyclenum += 1
    listofnums.append(newnum)
    n = newz
answer(1,10)
