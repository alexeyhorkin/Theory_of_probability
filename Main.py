import matplotlib.pyplot as plt
import math as mt
import tkinter as tk
import random as rd
import numpy as np
import scipy.integrate as integrate

ForTable2 = ("E(x)","x_сред","|E(x)-x_сред|","D(x)","S^2","|D(x) - S^2|","Me","R")
rd.seed(2) # set seed
def Gamma(x):
	if x ==1:
		return 1
	elif x ==1/2:
		return mt.sqrt(mt.pi)
	return (x-1)*Gamma(x-1)

def GetXi_integral(r,R):
	result,_ = integrate.quad(lambda x: x**(r/2-1)*mt.exp(-x/2), 0, R)
	return 1-result/(Gamma(r/2)*2**(r/2))

def GetLeftEdge(a):
	return -mt.asin(a/2)/a

def F(x,a):
	if x<=GetLeftEdge(a):
		return 0
	elif x<=0:
		return (1/a)*(mt.sin(a*x))+1/2
	elif x<=1:
		return 1/2+x-x**2/2
	else:
		return 1.0

def F_num(x,arr):
	count =0
	for i in arr:
		if i<x:
			count+=1
	return count/len(arr)

def Density_funk(x,a):
	if x>=0:
		return 1-x
	else:
		return mt.cos(a*x)


def Get_q(A,a,b):
	z,_ = integrate.quad(lambda x: Density_funk(x,A),a,b)
	return z

def Density_num(arr,x1,x2,n):
	count = 0
	for i in arr:
		if i >= x1 and i <x2:
			count += 1
	return count/(n*abs(x2-x1))

def Get_n(arr,x1,x2):
	count = 0
	for i in arr:
		if i >= x1 and i <x2:
			count += 1
	return count
def GetR(arrval,arr_x2,n_of_part,n,A):
	RES = 0
	for i in range(1,n_of_part):
		RES = RES + (Get_n(arrval,arr_x2[i-1],arr_x2[i])- n*Get_q(A,arr_x2[i-1],arr_x2[i]))**2/(n*Get_q(A,arr_x2[i-1],arr_x2[i])) 
	return RES
def GetArr(lb,rb,n):
	res = []
	res.append(lb)
	for i in range(n):
		res.append(float(input()))
	res.append(rb)
	return res



def GetVal(a):

	start  = GetLeftEdge(a)
	end = 1
	M = 2
	def f(x):
		if x<=0:
			return mt.cos(a*x) 
		elif x>0:
			return 1-x	
	while(True): 
		r1 = rd.random()
		r2 = rd.random()
		x0 = start + r1*(end-start)
		y = M*r2
		if y<=f(x0):
			return x0

def GetVal2(a):
	p = GetLeftEdge(a)
	def f(x):
		if x<=0.5:
			return mt.asin(a*x+mt.sin(a*p))/a
		if x>0.5:
			return 1 - mt.sqrt(2-2*x)
	return f(rd.random())

def GetMe(arr,n):
	if(n%2)==1:
		return arr[int(n//2)]
	else:
		return (arr[int(n/2-1)] + arr[int(n/2)])/2

def GetMathExp(a):
	return 1/6-(1/a)*mt.asin(a/2)*0.5-(1/a**2)*(mt.cos(mt.asin(a/2))-1)


def GetMathD(a):
	z = mt.asin(a/2)
	return (z/a)**2/2 +(2/a**3)*z*mt.cos(z)-1/a**2 - GetMathExp(a)**2 +1/12

def GetHist(arrVal, arrpoint):
	x_res = np.array([])
	y_res = np.array([0])
	index = 0
	for i in range(len(arrpoint)):
		x_res = np.append(x_res,arrpoint[index])
		x_res = np.append(x_res,arrpoint[index])
		index= index+1
	index = 0
	for i in range(len(arrpoint)-1):
		y_res = np.append(y_res,arrVal[index])
		y_res = np.append(y_res,arrVal[index])
		index= index+1
	y_res = np.append(y_res,0)
	return (x_res,y_res)
