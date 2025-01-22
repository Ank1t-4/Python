# import random as rand
# inpu=str(input('enter string: '))
# choice=int(input('you want to incode(1) or decode(2): '))
# splitedstr=inpu.split(' ')
# mergedlist=[]
# if choice == 1:  
#  for word in splitedstr:  
#   if len(word)>=3:
#     temp=word[1:]+word[0]
#     randfront= ''.join(rand.choices('abcdefghijklmnopqrstuvwxyz', k=3))
#     randback= ''.join(rand.choices('abcdefghijklmnopqrstuvwxyz', k=3))
#     temp=randfront+temp+randback
#     mergedlist.append(temp)
#   elif len(word)<3:
#     mergedlist.append(word[::-1])

# if choice == 2:
#   for words in splitedstr:   
#    if len(words)<3:
#      mergedlist.append(words[::-1])   
#    else:
#      temp=words[3:-3]
#      temp=temp[-1]+temp[:-1]
#      mergedlist.append(temp)
# print(' '.join(mergedlist))




import random as rand
def encode(inpu):
  '''Will convert the provided string into a coded string by changing sequence of elements and adding additional elements in front and back of the string'''
  
  inpu=str(inpu)
  splitedtstr=inpu.split(' ')
  mergedlist=[]
  
  for word in splitedtstr:
  
    if len(word)>=3:
     temp=word[1:]+word[0]
     randfront= ''.join(rand.choices('abcdefghijklmnopqrstuvwxyz', k=3))
     randback= ''.join(rand.choices('abcdefghijklmnopqrstuvwxyz', k=3))
     temp=randfront+temp+randback
     mergedlist.append(temp)

    elif len(word)<3:
     mergedlist.append(word[::-1])
    
  return mergedlist

def decode(inpu):
  '''Will convert the provided coded string into a normal string by changing sequence of elements and removing additionalelements in front and back of the string'''
  
  inpu=str(inpu)
  splitedstr=inpu.split(' ')
  mergedlist=[]
  
  for words in splitedstr:
   
   if len(words)<3:
     mergedlist.append(words[::-1])
   
   else:
     ierror=0
     temp=words[3:-3]
    
     try:
       temp=temp[-1]+temp[:-1]
       mergedlist.append(temp)
    
     except IndexError:
       ierror=1
  
  if ierror!=1:
    return mergedlist
  
  else:
    return 'Provided coded string cant be decoded'


def main(): 
 while True:
   while True:
    ierror=0
    try:userinput=int(input('Do you want to encode(1), decode(2) or quit(3): '))
    except ValueError:
      print('invalid Choice - Please choose either 1,2 or 3')
      ierror=1
    if ierror!=1:break

   if userinput==1 or userinput==2:
     match userinput:
      case 1:
         inpu=input('Enter word you want to encode: ')
         finres=encode(inpu)
        #  for i in finres:print(f'{i}',end=' ')
        #  print()
         print(' '.join(finres))#this method join the elements of a list into a string where each element is seperated by characters specified by you in '' marks
      case 2:
         inpu=input('Enter word you want to decode: ')
         finresu=decode(inpu)
         if type(finresu)==list:
          # for i in finresu:print(f'{i}',end=' ')
          # print()
          print(' '.join(finresu))
         else:print(finresu)
   elif userinput==3:break

if __name__=='__main__':
 main()