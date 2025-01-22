import math

def takeinput(a):
    '''user defined function to take user input'''
    userlist=[]
    b=0
    for i in range(1,(a+1)):
        # z=1
        while True:
            print("Enter elememt number",i ,end=": ")
            try:b=int(input())
            #   if b!=''and z==1:
            #     z=0
            except ValueError:print("Please enter a valid number.")
            else:break
            
        userlist.append(int(b))
    return(userlist)

def primee(a):
    if a==2 or a==3 or a==5 or a==7:return("Prime")
    elif (a%2==0):return("Non-prime")
    elif (a%3==0):return("Non-prime")
    elif (a%5==0):return("Non-prime")
    elif (a%7==0):return("Non-prime")
    else:return("Prime number")

def main():
    # z=1
    while True:
        try:listlengths=int(input("Enter the number of elements list contains: "))
        #  if listlengths!='' and z==1:
        #     z==0
        #  break
        except ValueError:print("Please enter a valid number.")
        else:break

    
    unsepratedlist=[]
    # listlength=int(listlengths)
    unsepratedlist=takeinput(listlengths)
    # print(unsepratedlist)
    primlist=[]
    nprimlist=[]
    for i in unsepratedlist:
        if primee(i)=="Prime":
            primlist.append(i)
        else:nprimlist.append(i)
    print(primlist)
    print(nprimlist)

if __name__=="__main__":
    main()