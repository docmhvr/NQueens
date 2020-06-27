from itertools import permutations
from tkinter import *
from time import time
from tkinter import ttk, messagebox

class nqueens():
	#init function of nqueens
	def __init__(self, root):
		#no. of queens
		self.n = 8 
		#total queens in solution for current n
		self.queens = (0 for i in range(self.n))
		#current index of queen
		self.index = 0
		#list of all possible solution of queens
		self.solution = []

		#build GUI
		self.root = root
		self.root.title = ("NQUEENS")
		self.root.configure(background='blue')
		self.root.minsize(480, 480)
		self.root.resizable(True, True)

		self.style = ttk.style()
		self.style.configure('TFrame',background='blue')
		self.style.configure('TButton',background='blue')
		self.style.configure('TLabel',background='blue')

		

	def draw_board():
		pass

	def solve():
		pass

def main():
	root = Tk()
	gui = Nqueens(root)
	root.mainloop()

if __name__=="__main__": main()
