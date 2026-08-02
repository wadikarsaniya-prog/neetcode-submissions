class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ap = 0
        for i in range(len(tokens)):
            if tokens[i] not in ["+", "-", "*", "/"]:
                stack.append(int(tokens[i]))
            else:
                k = stack.pop() 
                j = stack.pop()
                if tokens[i] == "+":
                    ap = j + k
                if tokens[i] == "-":
                    ap = j - k
                if tokens[i] == "*":
                    ap = j * k
                if tokens[i] == "/":
                    ap = int(j / k)
                stack.append(ap)
        
        return stack.pop()
                

