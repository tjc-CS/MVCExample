

import random

import tkinter as tk
from tkinter import ttk
import time

import datetime



class Game:
    def __init__(self):
        self.col = 0
        
    def do_something(self):
        self.col = (self.col +1) % 2    
    def get_colour(self):
        return self.col;
                      
class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.clock()     
               
    def button_clicked(self):
        self.model.do_something()
        
        
    def update_ui(self):
        print("update UI")
        
        v=self.model.get_colour()
        self.view.change_button_colour(v)
        
    
    def clock(self):
        # calls update ui
        self.update_ui()
        # calls clock method after 100ms   
        self.view.after(100, self.clock) 
    
   

        
        
        
class View(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # create widgets
        # label
        self.label = ttk.Label(self, text='MVC Example')
        self.label.grid(row=1, column=2)  
        
        self.start_button = ttk.Button(self, text='Start', command= self.button_clicked)
        self.start_button["state"]="enabled"
        self.start_button.grid(row=2, column=1, padx=0)
        
        
       
        self.controller=None
    def change_button_colour(self,v):
        if v ==0:
            
            self.start_button.configure(text="red")
            
        else:
            self.start_button.configure(text="blue")
               

    def button_clicked(self):
        self.controller.button_clicked()
                                  
          
    def set_controller(self, controller):
      
        self.controller = controller
        
class App(tk.Tk):
    def __init__(self):
        super().__init__()
       # self.root =tk.Tk()
        self.title('Tkinter MVC Demo')
        # create a model
        model = Game()

        # create a view and place it on the root window
        view = View(self)
        view.grid(row=0, column=0, padx=10, pady=10)

        # create a controller
        controller = Controller(model, view)

        # set the controller to view
        view.set_controller(controller)
            
     


if __name__ == '__main__':
    app = App()
    app.mainloop()  
