# -*-coding:utf-8-*-
import os


data=[1,2,3,4,5,6,7,9]
outList=[]

def mainloop(program, bracket_map):  
    pc = 0  
    tape = Tape()  
    while pc < len(program):  
        code = program[pc]  
        if code == ">":  
            tape.advance()  
        elif code == "<":  
            tape.devance()  
        elif code == "+":  
            tape.inc()  
        elif code == "-":  
            tape.dec()  
        elif code == ".":  
            # print  
            os.write(1, chr(tape.get()))  
        elif code == ",":  
            # read from stdin  
            tape.set(ord(os.read(0, 1)[0]))  
        elif code == "[" and tape.get() == 0:  
            # Skip forward to the matching ]  
            pc = bracket_map[pc]  
        elif code == "]" and tape.get() != 0:  
            # Skip back to the matching [  
            pc = bracket_map[pc]  
        pc += 1
    return outList

class Tape(object):  
    def __init__(self):  
        self.thetape = data 
        self.position = 0  
    def get(self):  
        return self.thetape[self.position]  
    def set(self, val):  
        self.thetape[self.position] = val  
    def inc(self):  
        self.thetape[self.position] += 1  
    def dec(self):  
        self.thetape[self.position] -= 1  
    def advance(self):  
        self.position += 1  
        if len(self.thetape) <= self.position:  
            self.thetape.append(0)  
    def devance(self):  
        self.position -= 1 

def parse(program):  
    parsed = []  
    bracket_map = {}  
    leftstack = []  
    pc = 0  
    for char in program:  
        if char in ('[', ']', '<', '>', '+', '-', ',', '.'):  
            parsed.append(char)  
            if char == '[':  
                leftstack.append(pc)  
            elif char == ']':  
                left = leftstack.pop()  
                right = pc  
                bracket_map[left] = right  
                bracket_map[right] = left  
            pc += 1  
    if len(leftstack) !=0:
        raise Exception(" parse error ")
    return "".join(parsed), bracket_map  
    

def fitnessValue(output,taget):
    temp= (1.0-(output-taget)/taget)*100
    if temp>100.0:
        temp=200.0-temp  
    return temp


def indListToProgram(indList):
    program_contents=[]
    ind=['[', ']', '<', '>', '+', '-', ',', '.']
    for i in indList:
        program_contents.append(ind[i])
    return ''.join(program_contents)

def run(indList):  
    #program_contents="++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>."
    program_contents=indListToProgram(indList)
    print program_contents
    try:
        program, bm = parse(program_contents)  
        list1=mainloop(program, bm) 
        return fitnessValue(sum(list1),sum(data)) 
    except BaseException as inis:
        return 0       




#m=s;i=n=p=0;d="";a=[0]*30000
#    while len(m)-1-i:
#        s=m[i];o=1
#        if s=='>':p+=1
#        if s=='<':p-=1
#        if s=='+':a[p]+=1
#        if s=='-':a[p]-=1
#        if s=='.':print(chr(a[p]),end="")
#        if s==',':a[p]=ord(d[n]);n+=1
#        if s=='[' and a[p]==0:
#            while o:
#                i+=1;c=m[i];
#                if c=='[':o+=1
#                if c==']':o-=1
#        if s==']':
#            while o:
#                i-=1;c=m[i]
#                if c=='[':o-=1
#                if c==']':o+=1
#            i-=1
#        i+=1




