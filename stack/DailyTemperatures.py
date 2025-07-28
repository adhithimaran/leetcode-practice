def dailyTemperatures(temperatures):
    # don't perform any pop operations if elements are already in decreasing order. 
    # when we reach int greater than previous ones 
        # pop elements from the stack until the top element of the stack is no longer less than the current element.
        # For each popped element, we compute the difference between the indices and store it in the position corresponding to the popped element
    
    res = [0] * len(temperatures)  
    stack = []  
    
    for i in range(len(temperatures)):
        while stack and temperatures[stack[-1]] < temperatures[i]:
            j = stack.pop()
            res[j] = i - j
        stack.append(i)