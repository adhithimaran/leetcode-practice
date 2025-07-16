def evalRPN(tokens):
    # Qs:
        # What are other stack data structures in Python

    # Input: tokens = Array of Strings (arithmetic exp in RPN)
    # Output: evaluation of tokens
    temp = [] # stack to hold ints before operator
    for token in tokens:
        print(f'this is token: {token}')
        try:
            # integer: add to stack
            num = int(token)
            temp.append(num)
        except ValueError:
        # operator: 
            # remove (first in first out) + apply operator
            curr_output = temp[0]
            del temp[0]
            if token == '+':
                for i in range(len(temp)):
                    curr_output += temp[i]
            if token == '-':
                for i in range(len(temp)):
                    curr_output -= temp[i]
            if token == '*':
                for i in range(len(temp)):
                    curr_output *= temp[i]
            if token == '/':
                for i in range(len(temp)):
                    curr_output *= temp[i]

            # add evaluation back to stack and continue
            temp = [curr_output]
    return temp[0] # should only be one left

tokens = ["1","2","+","3","*","4","-"] #5
print(evalRPN(tokens))