
def dailyTemperatures(temperatures):
    dif = []
    for d in range(len(temperatures)):
        if (d ==(len(temperatures)-1)):
            dif.append(0)
            return dif
        ptr = d+1
        count = 0
        for p in range(ptr, len(temperatures)):
            count +=1
            print(f'{temperatures[p]} greater than {temperatures[d]}?')
            print(f'this is day, ptr: {d}, {p}')
            if temperatures[p] > temperatures[d]:
                dif.append(count)
                break
            elif (temperatures[p] <= temperatures[d] and p == (len(temperatures)-1)):
                dif.append(0)
    return dif

print(dailyTemperatures([30,38,30,36,35,40,28]))