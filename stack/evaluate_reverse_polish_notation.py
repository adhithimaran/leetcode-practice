def evalRPN(tokens):
    stack = []
    for token in tokens:
        if token in ['+', '-', '*', '/']:
            # Pop last two elements (LIFO)
            b = stack.pop()  # second operand
            a = stack.pop()  # first operand
            
            if token == '+':
                result = a + b
            elif token == '-':
                result = a - b
            elif token == '*':
                result = a * b
            elif token == '/':
                result = int(a / b)  # truncate toward zero
            
            stack.append(result)
        else:
            stack.append(int(token))
    
    return stack[0]