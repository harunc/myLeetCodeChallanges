class Solution:
    def decideOp(self,a:str,b:str,c:str)->int:
        if c =="+":
            return int(a)+int(b)
        elif c=="-":
            return int(a)-int(b)
        elif c=="*":
            return int(a)*int(b)
        else:
            return int(int(a)/int(b))
    def isOp(self,c:str)->bool:
        if c=="+" or c =="-" or c=="*" or c=="/":
            return True
        else:
            return False
    def evalRPN(self, tokens: List[str]) -> int:
        numStack=[]
        opStack=[]
        for t in tokens:
            opStack.append(t) if self.isOp(t) else numStack.append(t)
            if len(numStack)>=2 and opStack and numStack:
                a=numStack[-2]
                b=numStack[-1]
                numStack.pop()
                numStack.pop()
                c=opStack[-1]
                opStack.pop()
                numStack.append(self.decideOp(a,b,c))
            print(numStack[-1])
        return numStack[-1]

                
                