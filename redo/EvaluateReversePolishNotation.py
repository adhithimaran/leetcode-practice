class EvaluateReversePolishNotation:
    def __init__(self):
        self.stack = []

    def evalRPN(self, tokens: List[str]) -> int:
        for thing in tokens:
            if (thing == "+" or thing == "-" or thing == "*" or thing == "/"):
                # thing is an operator
                thing = thing.replace('"', '')

                if thing == "+":
                    self.stack.append(self.stack.pop() + self.stack.pop())

                elif thing == "-":
                    a, b = self.stack.pop(), self.stack.pop()
                    self.stack.append(b - a)
                
                elif thing == "*":
                    self.stack.append(self.stack.pop() * self.stack.pop())

                elif thing == "/":
                    a, b = self.stack.pop(), self.stack.pop()
                    self.stack.append(int(float(b) / a))
            else:
                # thing is type int
                self.stack.append(int(thing))
        return self.stack[-1]
                       
