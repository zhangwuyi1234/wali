# -*-coding:utf-8-*-
import os


data=[1,2,3,4,5,6,7,9]
outList=[]

def mainloop(program):  
    m=program;i=n=p=0;d="";a=[0]*30000
    while len(m)-1-i:
        s=m[i];o=1
        if s=='>':p+=1
        if s=='<':p-=1
        if s=='+':a[p]+=1
        if s=='-':a[p]-=1
        if s=='.':outList.append(a[p])
        if s==',':a[p]=ord(d[n]);n+=1
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
    return "".join(parsed)  
    



def fitnessValue(output,taget):
    temp=0
    if output<taget:
        temp=temp-(taget-1000)+output
    else:
        temp=taget+1000-output
    print temp


def indListToProgram(indList):
    program_contents=[]
    ind=['[', ']', '<', '>', '+', '-', ',', '.']
    for i in indList:
        program_contents.append(ind[i])
    return ''.join(program_contents)

def run(indList):  
    #program_contents = ".,[,[].+>.>+,+->>,+,++>-.<]<,[--[+-]>,<+<>,>]->>.+.[-+.>+[->+-[+<.+++,--[>-.<][<<++[>[,+,>>+]+<-]>,]>>[.-<,.-,--,]+>-.-].+[]>.<[+[.,-,,+,]>[<.-,<>,[>-,.[<[.<,>.]>><+>,.,<---<-.--]][,.]><]<--.><.-,[+],<+.].<<],+++,,[+>..[]-]<.]<+[<>,<>..>-><->>.>-,]>>"
    program_contents=indListToProgram(indList)
    re=0
    try:
        program = parse(program_contents) 
        re=re+10
        list1=mainloop(program)
        re=re+20
        temp1=fitnessValue(sum(list1),sum(data)) 
        re=re+30+temp1
        return temp1
    except BaseException as inis:
        print re
        return re
if __name__ == "__main__":
    #run([])
    program_contents = ".,[,[].+>.>+,+->>,+,++>-.<]<,[--[+-]>,<+<>,>]->>.+.[-+.>+[->+-[+<.+++,--[>-.<][<<++[>[,+,>>+]+<-]>,]>>[.-<,.-,--,]+>-.-].+[]>.<[+[.,-,,+,]>[<.-,<>,[>-,.[<[.<,>.]>><+>,.,<---<-.--]][,.]><]<--.><.-,[+],<+.].<<],+++,,[+>..[]-]<.]<+[<>,<>..>-><->>.>-,]>>"
    print(len(program_contents))


