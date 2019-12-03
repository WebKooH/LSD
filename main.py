from random import randrange as rnd, choice
from tkinter import mainloop
import tkinter as tk
import time
import math
import time

root = tk.Tk()
# fr = tk.Frame(root)
root.geometry('1000x800')

#canv = tk.Canvas(root, bg='white')
#canv.pack(fill=tk.BOTH, expand=1)

class Field(tk.Canvas):
    
    def __init__(self, master):
        super().__init__(master, background='pink')

        self.x = 1000
        self.y = 800
        self.colors = ['white', 'red', 'green', 'yellow', 'blue']
        self.side = 15
        self.N_X = N_X = 20
        self.N_Y = N_Y = 16
        self.matrix = [[{} for i in range(N_X)] for j in range(N_Y)]

        for i in range(N_X):
            for j in range(N_Y):
                self.matrix[j][i]['active'] = 0
                self.matrix[j][i]['id'] = self.create_rectangle(self.side*i, self.side*j, self.side*(i + 1), self.side*(j + 1), fill="grey", width=1, outline="black" )
                print('who')

    def UpdateField(self):
        for i in range(self.N_X):
            for j in range(self.N_Y):
                if self.matrix[j][i]['active'] == 1:
                    self.matrix[j][i]['id'] = self.create_rectangle(self.side*i, self.side*j, self.side*(i + 1), self.side*(j + 1), fill="white", width=1, outline="black")
                    self.itemconfig(self.matrix[j][i]['id'], fill='white')

                if self.matrix[j][i]['active'] == 0:
                    self.matrix[j][i]['id'] = self.create_rectangle(self.side*i, self.side*j, self.side*(i + 1), self.side*(j + 1), fill="grey", width=1, outline="black" )
                    self.itemconfig(self.matrix[j][i]['id'], fill='grey')

    def Evolution(self):
        tempmatrix = [[{} for i in range(self.N_X)] for j in range(self.N_Y)]
        for i in range(self.N_X):
            for j in range(self.N_Y):
                neighbors = self.matrix[(j - 1) % self.N_Y][(i - 1) % self.N_X]['active'] + \
                            self.matrix[j % self.N_Y][(i - 1) % self.N_X]['active'] + \
                            self.matrix[(j + 1) % self.N_Y][(i - 1) % self.N_X]['active'] + \
                            self.matrix[(j - 1) % self.N_Y][i % self.N_X]['active'] + \
                            self.matrix[(j + 1) % self.N_Y][i % self.N_X]['active'] + \
                            self.matrix[(j - 1) % self.N_Y][(i + 1) % self.N_X]['active'] + \
                            self.matrix[j % self.N_Y][(i + 1) % self.N_X]['active'] + \
                            self.matrix[(j + 1) % self.N_Y][(i + 1) % self.N_X]['active']
                if (neighbors == 3):
                    tempmatrix[j][i]['active'] = 1
                else:
                    tempmatrix[j][i]['active'] = 0
        for i in range(self.N_X):
            for j in range(self.N_Y):
                self.matrix[j][i]['active'] = tempmatrix[j][i]['active']

    def main(self):
        self.Evolution()
        self.UpdateField()


gamefield = Field(root)
gamefield.pack(fill=tk.BOTH)


gamefield.matrix[2][2]['active'] = 1
gamefield.matrix[2][3]['active'] = 1
gamefield.matrix[2][4]['active'] = 1
gamefield.matrix[1][4]['active'] = 1
gamefield.matrix[0][3]['active'] = 1

gamefield.main()
root.mainloop()





