import os
import tkinter as tk
os.system('cls')

def create_user(username,password):
   if os.path.exists(f"E:/My Programs/Temp/{username}.txt"):
      print('User already Exist')
   else:
      with open(f"E:/My Programs/Temp/{username}.txt", 'a') as file:
         file.write(f'{password}')

def verify_user(username,password):
   if os.path.exists(f"E:/My Programs/Temp/{username}.txt"):
      with open(f"E:/My Programs/Temp/{username}.txt", 'r') as file:
         filecontent = file.read()
      if filecontent==password:
         print('Success')
      else:print('Invalid Username or Password')
   else:print('Not registered')

def sub_buttong(username,password,checkbox):
   # print(f'{username.get()}')
   # print(f'{password.get()}')
   # print(f'{checkbox.get()}')
   # create_user(username.get(),password.get())
   verify_user(username.get(),password.get())

def main():      

   root = tk.Tk()
   root.title('Hi')
   root.geometry('680x500')
   root.resizable(False,False)

   frame1 = tk.Frame(root, bg = "dark grey",width = 270, height = 150)
   frame1.place(x = 210, y = 160)
   
   frame2 = tk.Frame(root, bg = "dark grey",width = 200, height = 1000)
   frame2.place(x = 1, y = 1)
   
   tk.Label(frame1, text = 'Username: ', relief = 'raised').place(relx = 0.1, rely = 0.2)
   tk.Label(frame1, text = 'Password: ', relief = 'raised').place(relx = 0.1, rely = 0.4)
   tk.Label(frame2, text = 'Welcome\nto Application', font = ['Lucida Handwriting',25], bg = 'dark grey').place(relx = 0.01, rely = 0.18)
   # tk.Label(frame2, text = 'Welcome\nto Application: ').pack()
   
   username1 = tk.StringVar()
   password1 = tk.StringVar()
   checkbox1 = tk.IntVar()
   
   tk.Entry(frame1, textvariable = username1).place(relx = 0.36, rely = 0.2)
   tk.Entry(frame1, textvariable = password1, show = '*').place(relx = 0.36, rely = 0.4)
   tk.Checkbutton(name='hii',text = 'Hi', variable = checkbox1).place(x=300,y=2)
   
   for_invalid = None
   def sub_button():
      nonlocal for_invalid
      if username1.get() and password1.get():
         if for_invalid:
            for_invalid.destroy()
            for_invalid = None
         sub_buttong(username1,password1,checkbox1)
         
      else:
         if for_invalid is None:
            for_invalid = tk.Label(root, text = 'Invalid', fg = 'red')
            for_invalid.place(x = 310,y = 251)
   
   button3 = tk.Button(frame1,text = 'Submit', command = sub_button)
   button3.place(relx = 0.6, rely = 0.6)
   
   
   root.tk.mainloop()

if __name__=='__main__':
   main()