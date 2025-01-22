def prim(a):
 if a==2 or a==3 or a==5 or a==7:print("Prime Number")
 elif (a%2==0):print("Not a prime number")
 elif (a%3==0):print("Not a prime number")
 elif (a%5==0):print("Not a prime number")
 elif (a%7==0):print("Not a prime number")
 else:print("Prime number")

if __name__=="__main__":
      a=int(input("Enter an mumber: "))
      prim(a)