def printPoly(p_x): #p_x=[7,-4,0,5]
    term=len(p_x)-1 #term 3
    polyStr="P(x)=" #polyStr   P(x)= +7X^3 -4X^2 + 0X^1 + 5X^0

    for i in range(len(px)):
        coef=p_x[i]
        if(i>=1):
            polyStr+="+"
        if(coef!=0):
            polyStr+=str(coef)+"X^"+str(term)+" "
        term-=1
    
    return polyStr

def calcPoly(xVal,p_x): #xVal 1(입력값) p_x [7,-5,0,5]
    retValue=0
    term=len(p_x)-1   #term 3

    for i in range(len(px)):
        coef=p_x[i]
        retValue+=coef*xVal**term
        term-=1
    
    return retValue

px=[7,-4,0,5]

if __name__=="__main__":
    pStr=printPoly(px)
    print(pStr)

    xValue=int(input("X값 -->"))

    pxValue=calcPoly(xValue,px)
    print(pxValue)
