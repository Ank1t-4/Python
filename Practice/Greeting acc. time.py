import time
current_hour= time.strftime("%H")
print(current_hour)
if (current_hour>="03" and current_hour<"12"):print("Good Morning")
elif(current_hour>="12" and current_hour<"17"):print("Good Afternoon")
elif(current_hour>="17" and current_hour<"20"):print("Good Evening")
elif(current_hour>="20" and current_hour<"24"):print("Good Night")
else:print("You Should be Asleep by now")