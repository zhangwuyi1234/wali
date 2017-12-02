# -*-coding:utf-8-*-
import os
import time
from timeout import timeout


def mainloop1(m,d):  
    i=n=p=0;a=[0]*30000
    print m
    while len(m)-1-i:
        print i          #TODO   while i=4 i=5
        s=m[i];o=1
        if s=='>':p+=1
        if s=='<':p-=1
        if s=='+':a[p]+=1
        if s=='-':a[p]-=1
        if s=='.':outList.append(a[p])
        if s==',':a[p]=d[n];n+=1
        if s=='[' and a[p]==0:
            while o:
                i+=1;c=m[i];
                if c=='[':o+=1
                if c==']':o-=1
        if s==']':
            while o:
                i-=1;c=m[i]
                if c=='[':o-=1
                if c==']':o+=1
            i-=1
        i+=1
    return outList




outList=[]

@timeout(5)
def mainloop(program, bracket_map,d):  
    #print "sleep"  
    #time.sleep(6)
    tempstr=[]
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
            #os.write(1, chr(tape.get()))  
            outList.append(tape.get())
        elif code == ",":  
            # read from stdin  
            tape.set(d.pop())  
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
        self.thetape = [0]  
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


def parse(program,d):  
    parsed = []  
    bracket_map = {}  
    leftstack = []  
    pc = 0  
    dataIndex=0
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
            elif char == ',':
                dataIndex+=1
                if len(d)<dataIndex:
                    d.insert(0,0)
            pc += 1
    #print dataIndex
    #print len(d)
    parseds="".join(parsed)
    if len(leftstack) !=0:
        raise Exception(" parse error ")
    return parseds, bracket_map ,d


def fitnessValue(output,taget):
    temp=0
    if output<taget:
        temp=temp-(taget-1000)+output
    else:
        temp=taget+1000-output
    return temp


def indListToProgram(indList):
    program_contents=[]
    ind=["<", ">", "+", "-", ",",".","[", "]"]
    for i in indList:
        program_contents.append(ind[i])
    return "".join(program_contents)


def run(indList):
    program_contents=indListToProgram(indList)
    #program_contents = ""
    print program_contents
    datas=[1,2,3,4,5,6,7,9]
    re=-1
    try:
        if "[]" in program_contents:
            return -5
        program, bm ,data = parse(program_contents,datas)
        re=re+5
        list1=mainloop(program_contents,bm,data)
        re=re+10
        temp1=fitnessValue(sum(list1),sum(datas)) 
        if temp1<0:
            temp1=0
        else:
            temp1=temp1/20
        print str(re)+"======="+str(temp1)
        re=re+temp1
        print re
        return re
    except BaseException as inis:
        temps=0
    print re
    return re


if __name__ == "__main__":
    print run([1,2])





