from os import system
from math import sqrt,pow
import tkinter as tk
system('cls')

class MyGui(tk.Tk):

   def __init__(self):
      super().__init__()
      self.title('Calculator')
      self.geometry('320x500')
      self.resizable(False,False)
      self.wm_iconbitmap("E:/My Programs/Temp/199262_.ico_icon.ico")
   
   def get_window_size(self):
      '''It tells user the size of window'''
      win_geo = self.geometry()
      win_width_height = win_geo.split('+')[0]
      width, height = map(int, win_width_height.split('x'))#can be used if need width and height seperately
      return width,height#win_width_height

   def create_frame(self, fwidth, fheight, place_x, place_y, place_bg='red'):
      '''As arguments it takes framewidth, frameheight, it's 'x' and 'y' cordinates with respect to the frame and an optional Background(Deafult is Red) and then it return a Frame with Height and Width as passed by user. '''
      frame_made = tk.Frame(self, bg=place_bg, width=fwidth, height=fheight)
      frame_made.place(x=place_x, y=place_y)
      return frame_made

   def create_button(self, fname, place_x, place_y, bcommand, btext='Button'):
      '''As arguments it takes frame(in which you want to place the widget), it's 'x' and 'y' cordinates with respect to the frame and a text variable in which value will be stored, Button command and optional Button text and then it return a Button with 'relwidth=0.25', 'relheight=0.17', 'font=Helvetica 30' and other value as passed by user. '''
      button_created =  tk.Button(fname, text=btext, command=bcommand)
      button_created.place(relx=place_x, rely=place_y, relwidth=0.25, relheight=0.17)
      return button_created

   def create_entry(self, fname, place_x, place_y, textvar):
      '''As arguments it takes frame(in which you want to place the widget), it's 'x' and 'y' cordinates with respect to the frame and a text variable in which value will be stored and then it return an Entry Widget of 'width=5', 'justify=right', 'font=Helvetica 30' and other value as passed by user. '''
      entry_created = tk.Entry(fname, width=5, textvariable=textvar, justify='right', font='Helvetica 30')
      entry_created.place(rely=place_y,relx=place_x, relheight=1, relwidth=1)
      return entry_created

def main():
   window1 = MyGui()
   win_size = window1.get_window_size()
   print(f'{win_size[0]}x{win_size[1]}')
   
   tittle_frame = window1.create_frame(320, 37, 0, 0,'grey')

   display_frame = window1.create_frame(320, 105, 0, 37,'dark grey')
   entry_var = tk.StringVar()
   entry1 = window1.create_entry(display_frame, 0.0, 0.0, entry_var)

   def button_command(b):
      '''It handels all the logic when the buttons are pressed.'''

      print(f'Button {b} pressed')
      if entry_var.get()=='Error':
         entry_var.set('')
         entry1.update()

      if b=='CE' or b=='C':
         entry_var.set('')
         entry1.update()

      elif b=='sqr':
         square = entry_var.get()
         float_square = float(square)
         square = pow(float_square,2)
         square = str(square)
         entry_var.set(square)
         entry1.update()
         
      elif b=='sqrt':
         square_root = entry_var.get()
         float_square_root = float(square_root)
         square_root = sqrt(float_square_root)
         square_root = str(square_root)
         entry_var.set(square_root)
         entry1.update()

      elif b=='Del':
         entry_var.set(entry_var.get()[:len(entry_var.get())-1])
         entry1.update()

      elif b=='=':
         try:
            entry_var.set(eval(entry_var.get()))
         except Exception as e:
            entry_var.set('Error')

      elif b=='+/-':
         checker = entry_var.get()
         if checker:
            if checker.startswith('-'):
               entry_var.set(entry_var.get()[1:])
               entry1.update()
         
            else:
               new_checker = '-' + checker
               entry_var.set(new_checker)
      
      elif entry_var.get() == '' and b in ('+', '-', '*', '/'):
         entry_var.set(f'0{b}')

      elif entry_var.get().endswith(('+' ,'-' ,'*' ,'/')) and b in ('+', '-', '*', '/'):
         pass

      elif b=='1/x':pass
         
      else:
         entry1.insert(tk.END,b)


   buttons_frame = window1.create_frame(320, 360, 0, 140)
   calc_butttons = ['+/-', '0', '.','=', '1', '2', '3', '+', '4', '5', '6', '-', '7', '8', '9', '*', '1/x', 'sqr', 
                    'sqrt', '/', '%', 'CE', 'C', 'Del'] #if you add buttons to this list you also have to update 'if' condition in 'for' loop

   place_x = 0.0  #used to obtain 'x' co-ordinates in for loop to place buttons in a frame
   place_y = 0.85 #used to obtain 'y' co-ordinates in for loop to place buttons in a frame
   
   for i, button_content in enumerate(calc_butttons, 1):
      #this loop takes the calc_buttons list and map it's content to different co-ordinates on the buttons_frame we made just above and it changes 'place_x' & 'place_y' to change the co-ordinates of each button as we have 24 buttons divided in 6 rows and 4 columns. So, as we are placing buttons bottop-up we move the button placement up by decresing 'y' co-ordinate and we reset the 'x' co-ordinate after every four buttons so placement return to the left of the screen as it is increased to move the placement from left to right.
       
      if i == 5 or i == 9 or i == 13 or i == 17 or i == 21:
         place_x = 0.0
         place_y -= 0.17
         
      window1.create_button(buttons_frame, place_x, place_y, lambda t=button_content: button_command(t), button_content)
      place_x += 0.25

   window1.mainloop()

if __name__=='__main__':
   main()

#in the for loop used to create buttons i have used lambda function but we also bind the button with an evevt and then use event.widget.cget('item_you_wnat_from_the_widget'). Here, item can be any aparameter like 'text' which in our case will return 1,2,3... depending on the button we press.

#it can also be done like this as suggested by Chat GPT
# def main():
#    window1 = MyGui()
#    frame1 = window1.create_frame(320, 360, 0, 140)
#    calc_buttons = [
#        ('+/-', 0.0, 0.89), ('0', 0.25, 0.89), ('.', 0.5, 0.89), ('=', 0.75, 0.89),
#        ('1', 0.0, 0.78), ('2', 0.25, 0.78), ('3', 0.5, 0.78), ('+', 0.75, 0.78),
#        ('4', 0.0, 0.67), ('5', 0.25, 0.67), ('6', 0.5, 0.67), ('-', 0.75, 0.67),
#        ('7', 0.0, 0.56), ('8', 0.25, 0.56), ('9', 0.5, 0.56), ('*', 0.75, 0.56),
#        ('1/x', 0.0, 0.45), ('sqr', 0.25, 0.45), ('sqrt', 0.5, 0.45), ('/', 0.75, 0.45),
#        ('%', 0.0, 0.34), ('CE', 0.25, 0.34), ('C', 0.5, 0.34), ('del', 0.75, 0.34),
#    ]

#    def button_command(label):
#        print(f"Button {label} pressed")

#    for text, x, y in calc_buttons:
#        window1.create_button(frame1, x, y, btext=text, bcommand=lambda t=text: button_command(t))

#    window1.mainloop()