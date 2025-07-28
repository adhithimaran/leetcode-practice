def dailyTemperatures(temperatures):
    # don't perform any pop operations if elements are already in decreasing order. 
    # when we reach int greater than previous ones 
        # pop elements from the stack until the top element of the stack is no longer less than the current element.
        # For each popped element, we compute the difference between the indices and store it in the position corresponding to the popped element
    
    stack_temps = temperatures.copy()
    res = []
    for i in range(1, len(temperatures)):
        print(f'bigger for loop: {temperatures[i]}')
        if temperatures[i] <= temperatures[i-1]:
            continue
        print(f'larger element: {temperatures[i]}')
        count = 0
        while count < i:
            temp = stack_temps.pop(0)
            print(f'stack ele poper off: {temp}')
            res.append(count+1)
            print(f'stack: \n{stack_temps}')
            count +=1
    return res

temperatures = [30,38,30,36,35,40,28]
print(dailyTemperatures(temperatures))