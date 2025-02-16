def fun1(n):
    iletration = 0
    print("the total input is:",n)
    iletration+=1
    print("THE TOTAL ITERATION IS ",iletration)
fun1(10)
fun1(200)
#TIME COMPLEXITY=O(1)
#THIS IS BEST CASE SCENARIO


def OnTime(n):
    ilteration = 0
    for i in range(1,n+1):
        ilteration+=1
    print("THE TOTAL ITERATION WILL BE",ilteration)
OnTime(45)
OnTime(456)
OnTime(87)
#time complexity = O(n)
#This is average case scenario

def time(n):
    ilter = 0
    for i in range(0,n):
        for j in range(0,n):
            ilter+=1
            print("*",end="")
        print("")
    print("\nTHE TOTAL ILTERATION WILL BE",ilter)
time(3) 
time(4)       
#time complexity = O(n^2)
#its the worst case scenario