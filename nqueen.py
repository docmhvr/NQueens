from itertools import permutations
from tkinter import *
from time import time
from tkinter import ttk, messagebox


class nqueens():
	#init function of nqueens
	def __init__(self, root):
		#no. of queens
		self.n = 4 
		#total queens in solution for current n
		self.queens = (0 for i in range(self.n))
		#current index of queen
		self.index = 0
		#list of all possible solution of queens
		self.solution = []

		#build GUI
		self.root = root
		self.root.title = ("NQUEENS")
		self.root.configure(background='#f1f8b9')
		self.root.minsize(410, 470)
		self.root.resizable(True, True)
		self.root.bind('<Configure>', lambda e: self.draw_board())

		self.style = ttk.Style()
		self.style.configure('TFrame',background='#f1f8b9')
		self.style.configure('TButton',background='#f1f8b9')
		self.style.configure('TLabel',background='#f1f8b9')

		self.board = Canvas(self.root)
		self.board.pack()

		self.controls_frame = ttk.Frame(self.root)
		self.controls_frame.pack(side=TOP, pady=10)

		ttk.Label(self.controls_frame, text='Number of Queens:',font='Verdana 10 bold').grid(row=0, column=0)
		self.n_var = StringVar()
		self.n_var.set(self.n)
		Spinbox(self.controls_frame, from_=4, to=99, width=3, font='Verdana 10 bold', textvariable=self.n_var).grid(row=0, column =1)
		ttk.Button(self.controls_frame, text="Update", command=self.solve).grid(row = 1,column=0, columnspan=2)
		ttk.Label(self.controls_frame).grid(row=0, column =2, padx =10)

		self.solution_var = StringVar()
		self.time_var = StringVar()
		self.solution_var.set("--")
		self.time_var.set("--")
		ttk.Label(self.controls_frame, text='Solution:',font='Verdana 10 bold').grid(row=0, column=3, sticky=(E))
		ttk.Label(self.controls_frame, textvariable=self.solution_var,font='Verdana 10').grid(row=0, column=4, sticky=(W))
		ttk.Label(self.controls_frame, text='Elapsed Time:',font='Verdana 10 bold').grid(row=1, column=3, sticky=(E))
		ttk.Label(self.controls_frame, textvariable = self.time_var,font='Verdana 10').grid(row=1, column=4, sticky=(W))

		self.solve()

	def draw_board(self):
		max_size = min(self.root.winfo_width(), self.root.winfo_height() - 60)
		square_size = max_size//self.n
		self.board.config(height=self.n*square_size, width=self.n*square_size)
		self.board.delete('all')

		#continue coding here

	def solve(self):
		input_n = int(self.n_var.get())
		self.n = input_n
		self.index = 0
		self.solution = []
		begin_time = time()
		if self.n!=input_n or self.solution == []:
			#Calculating solutions list for new input
			col = range(self.n)
			for perm in permutations(col):
				check1 = set()
				check2 = set()
				for i in col:
					check1.add(perm[i]+i)
					check2.add(perm[i]-i)
				if self.n == len(check1) == len(check2):
					self.solution.append(perm)

				end_time = time() - begin_time
				self.time_var.set("{0:.3f}s".format(end_time))	
		else:
			self.index+=1

		self.queens = self.solution[self.index % len(self.solution)]
		self.solution_var.set('{0}/{1}'.format(self.index % len(self.solution) + 1, len(self.solution)))
		self.draw_board()

def main():
	root = Tk()
	gui = nqueens(root)
	#print(gui.solution)
	root.mainloop()

if __name__=="__main__": main()
