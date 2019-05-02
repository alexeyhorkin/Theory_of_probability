import tkinter as tk
import matplotlib.pyplot as plt
import Table as Tbl
import numpy as np
from Main import *

def Initialize(e1,e2):
	n = e1.get()
	a = e2.get()
	if n !='':
		n = int(n)
	else:
		n = 0

	if a!='':
		a = float(a)
	else:
		a = 0.0
	return (n,a)


root = tk.Tk()
root.configure(background='#9cb8e5')
root.geometry("680x700")
root.title("Theory of propability, 22 вариант")
l1 = tk.Label(root, text = "Write count of experiments", font = "Arial 18",background='#9cb8e5')
l1.pack()

f1 = tk.Frame(root,background='#9cb8e5')
f1.pack(fill = "x")

f2 = tk.Frame(root,background="#9cb8e5")
f2.pack(fill = "x")

f3 = tk.Frame(root,background="#c2c4c6", bd = 3)
f3.pack(fill = "x")

f4 = tk.Frame(root,background='#9cb8e5', bd = 3)
f4.pack(fill= "x")

l2 = tk.Label(f4,text = "Numerical characteristics", font = "Arial 18", background='#9cb8e5')
l2.pack()


f5 = tk.Frame(root,background='#9cb8e5', bd = 3)
f5.pack(fill= "x")

f6 = tk.Frame(root,background="#c2c4c6", bd = 3)
f6.pack(fill= "x")


f_inside = tk.Frame(f3,height=300, bd =4 )
f_inside.pack(fill = tk.BOTH)

f_inside2 = tk.Frame(f4,height=30, bd =4 )
f_inside2.pack(fill = tk.BOTH)

f_inside3 = tk.Frame(f6,height=30, bd =4 )
f_inside3.pack(fill = tk.BOTH)


f3 = tk.Frame(root)
f3.pack(fill = "x", side = tk.BOTTOM)

l3 = tk.Label(f1,text = "Count of experiments = ", font = "Arial 10", background='#9cb8e5')
l3.pack(side = tk.LEFT)

l4 = tk.Label(f2,text = "write param - a  = ", font = "Arial 10", background='#9cb8e5')
l4.pack(side = tk.LEFT)

e1 = tk.Entry(f1, bd = 2)
e1.insert(0,"10")
e1.pack(side = tk.RIGHT)

e2 = tk.Entry(f2, bd = 2)
e2.insert(0,"1")
e2.pack(side = tk.RIGHT)

var1 = tk.IntVar()
var1.set(0)
def  GetMode():
	return var1.get()



l5 = tk.Label(f5,text = "number of partitions  = ", font = "Arial 10", background='#9cb8e5')
l5.pack(side = tk.LEFT)

e3 = tk.Entry(f5, bd = 2)
e3.insert(0,"10")
e3.pack(side = tk.LEFT)

RButton1 = tk.Radiobutton(f5, text = "Равномерное разбиение", variable = var1, value = 0,bg = "#9cb8e5")
RButton1.pack(side = tk.LEFT)
RButton2 = tk.Radiobutton(f5, text = "Неравномерное разбиение", variable = var1, value = 1,bg = "#9cb8e5")
RButton2.pack(side = tk.LEFT)
n,a  = Initialize(e1,e2)
mean = [0]
res = [[0]]
S_quad = [0]
Me = [0]
R= [0]
Main_table = [Tbl.Table(f_inside, ("№","случайная величина"))]
NC_table = [Tbl.Table(f_inside2, ("№","случайная величина"))]
q_table = [Tbl.Table(f_inside3, ("№","случайная величина"))]
def showtable():
	n,a  = Initialize(e1,e2)
	Main_table[0].destroy()
	res[0] = sorted([GetVal2(a) for i in range(n)])
	mean[0] = np.mean(res[0])
	R[0] = res[0][-1]- res[0][0]
	Me[0] = GetMe(res[0],n)
	S_quad[0] = np.mean([(i-mean[0])**2 for i in res[0]])
	res_final = [[i,res[0][i]] for i in range(n)]
	Main_table[0] = Tbl.Table(f_inside, ("№","случайная величина"),res_final)
	Main_table[0].pack(expand=tk.YES, fill=tk.BOTH)

def GetNC():
	n, a = Initialize(e1, e2)
	E = GetMathExp(a)
	E_num = mean[0]
	D_num = GetMathD(a)
	NC_table[0].destroy()
	NC_table[0] = Tbl.Table(f_inside2, ForTable2, [[E,E_num,abs(E-E_num),D_num,S_quad[0],abs(D_num-S_quad[0]),Me[0],R[0]]],1)
	NC_table[0].pack(expand=tk.YES, fill=tk.BOTH)

def GetGraph():
	n,a  = Initialize(e1,e2)
	delta = 0.000000001
	count_of_points = 2000
	lb = GetLeftEdge(a)
	rb=1
	y2 = np.array([0])
	x_F = np.array([lb-0.3])
	x = np.linspace(lb,rb,count_of_points)
	y = [F(i,a) for i in x]
	y_den = [Density_funk(i,a) for i in x]
	for i in res[0]:
		y2 = np.append(y2,F_num(i-delta,res[0]))
		x_F = np.append(x_F,i-delta)
		y2 = np.append(y2,F_num(i+delta,res[0]))
		x_F = np.append(x_F,i+delta)
	y2 = np.append(y2,1)
	x_F = np.append(x_F,rb+0.3)
	n_of_part = int(e3.get())+1
	if GetMode()==1:
		x2 = GetArr(lb,rb,n_of_part-2)
	else:
		x2 = np.linspace(lb,1,n_of_part)
	y3 = [Density_num(res[0],x2[i],x2[i+1],n) for i in range(len(x2)-1)]
	x2, y3 = GetHist(y3,x2)
	D = max(map(lambda x,y: abs(x-y),y2,[F(i,a) for i in x_F]))
	print("D  =  ", D)
	plt.plot(x,y,label='Интегральная функция')
	plt.plot(x_F,y2,label='Численная интегральная функция')
	plt.plot(x2,y3,label='Гистограмма плотности')
	plt.plot(x,y_den,label='Плотность')	
	plt.legend()
	plt.show()

def hypothesis():
	print("Введите уровень значимости критерия - ")
	alfa = float(input())
	n, a = Initialize(e1, e2)
	q_table[0].destroy()
	lb = GetLeftEdge(a)
	rb=1
	n_of_part = int(e3.get())+1
	if GetMode()==1:
		x2 = GetArr(lb,rb,n_of_part-2)
	else:
		x2 = np.linspace(lb,1,n_of_part)
	ForTable3 = tuple("["+str(x2[i-1])[0:5]+","+str(x2[i])[0:5]+"]" for i in range(1,n_of_part))
	q_arr = [Get_q(a,x2[i-1],x2[i])for i in range(1,n_of_part)]
	q_table[0] = Tbl.Table(f_inside3, ForTable3,[q_arr],1)
	q_table[0].pack(expand=tk.YES, fill=tk.BOTH)
	R_o = GetR(res[0],x2,n_of_part,n,a)
	print("F(R0) - ", GetXi_integral(n_of_part,R_o))
	if GetXi_integral(n_of_part,R_o) < alfa:
		print("Гипотеза отклонена")
	else:
		print("Гипотеза принята")




b_print_graph = tk.Button(f3,text = "RUN TABLE", command = showtable)
b_print_graph.pack(fill = "x")
b_NC = tk.Button(f3,text = "Numerical characteristics", command = GetNC)
b_NC.pack(fill = "x")
b_Gr = tk.Button(f3,text = "PrintGraph", command = GetGraph)
b_Gr.pack(fill = "x")
b_Check_hypothesis = tk.Button(f3,text = "Check hypothesis", command = hypothesis)
b_Check_hypothesis.pack(fill = "x")

root.mainloop()

