
def numberofstudent():
   while True:
      try: 
         student_count=int(input("Enter the number of students : "))
         return student_count
      except ValueError:
         print("Please enter a valid number.")


def numberofsubject():
   while True:
       try:
          sub_count=int(input("Enter the number of subjects: "))
          return sub_count
       except ValueError:
           print("Please enter a valid number.")


def subinput(number_subjects):
   allsubjects=[]
   for i in range(number_subjects):
       try: 
            subject_name=str(input(f"Enter the name of subject number {i+1}: "))
            allsubjects.append(subject_name) 
       except ValueError:
            print("Please enter a valid subject.")
   return allsubjects


def nameinput(student_count):
   student_names=[]
   for i in range(student_count):
    try:
       name=str(input(f"Enter the name of student number {i+1}: "))
       student_names.append(name)
    except ValueError:
       print("Please enter a valid name.")
   return student_names


def rollnumber(name,counter):
   roll_temp=[]
   for i in range(1):
      try: 
         roll=int(input(f"Enter the roll number of {name[counter]}: "))
         roll_temp.append(roll)
      except ValueError:print("Please enter a valid number.")
   return roll_temp


def marksinput(name,subject,subject_num,counter):
   mark=[]
   for i in range(1):
      while True:
        try: 
             marks=int(input(f"Enter the marks obtained by {name[counter]} in {subject[subject_num]}: "))
             if 0<=marks<=100:
                mark.append(marks)
                break
             else:print("Enter valide marks(i.e. out of 100)")
        except ValueError:
           print("Please enter a valid number.")
   
   return mark


def adddata(student_numbers,subnumbers,subject,name,rnum,marks,counter):
    student_numbers=numberofstudent()
    print()
   #  subnumbers=numberofsubject()
   #  print()
   #  subject=subinput(subnumbers)
   #  print()
    name=nameinput(student_numbers)
    print()
    for i in range(student_numbers):
       rnum=rollnumber(name,counter)
       for i in range(len(subject)):
         marks=marksinput(name,subject,i,counter)
       counter=counter+1
       print()
    return student_numbers,subnumbers,subject,name,rnum,marks
   

def search_student(name):
   student_to_find=str(input("Please enter name of student you wish to see data of: "))
   if student_to_find in name:
      indexstudent=name.index(student_to_find)
   return indexstudent


def access(student_numbers,subnumbers,subject,name,rollnum,marks,counter):
   student_index=search_student(name)
   print("Name of the student is ",name[student_index],"\nRoll number of student is ",rollnum[student_index])
   print()   


def main():
   student_numbers=0
   subnumbers=5
   subject=["English","Hindi","Math","Science","Computer"]
   name=[]
   rollnum=[]
   marks=[]
   counter=0
   while True:
    choice=int(input("Do you wish to\n1.add data\n2.access added data\n3.Exit? \n"))
    if choice==1:
       student_numbers,subnumbers,subject,name,rollnum,marks=adddata(student_numbers,subnumbers,subject,name,rollnum,marks,counter)
       print(name)  
    if choice==2:
        access(student_numbers,subnumbers,subject,name,rollnum,marks,counter)
        print()
    if choice==3:
       print("Ba Bye")
       break
    


if __name__=="__main__":
    main()

