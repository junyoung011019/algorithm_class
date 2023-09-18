katok=[('다현',200),('정연',150),('쯔위',90),('사나',30),('지효',15)]

def find_def(name,positon):
    find_positon=0
    for i in range(len(katok)):
        if(katok[i][1]<=count):
            find_positon=i #몇번째 들어가야하는지 위치 찾음
            break
    katok.append([None,None])
    temp_tuple=(name,positon)
    insert_def(find_positon,temp_tuple)

def insert_def(find_positon,temp_tuple):
    for i in range(len(katok)-1,find_positon,-1):
        katok[i]=katok[i-1]
        katok[i-1]=None
    katok[find_positon]=temp_tuple


while(True):
    name=input("이름을 입력하셈")
    count=int(input("연락횟수를 입력하셈"))
    find_def(name,count)
    print(katok)

