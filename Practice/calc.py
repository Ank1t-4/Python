a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))
# i=1
# its a do-while loop where while loop will be executed first and then condition is checked
# using if statement and if true then break statement is used to get out of loop
while True:
    c=input("Which operation you want to performe? ")
    if c=="+" or c=="-" or c=="*" or c=="/" or c=="%" or c=="0" : break
    # elif c=="0" : break
    else:print("Error choose correct operator or press 0 to exit")

if c=="+":print("Sum of",a, "and",b ,"is" ,a+b) 
elif c=="-": print("Substraction of",a, "and",b ,"is" ,a-b)
elif c=="*": print("Multiplication of",a, "and",b ,"is" ,a*b)
elif c=="/": print("Division of",a, "and",b ,"is" ,a/b)
elif c=="%":print("Remainder of division of",a, "and",b ,"is" ,a%b)