#This code solves Rayleigh-Plesset equation using Runge-Kutta method
#Two conditions for bubble are considered and plotted in the same graph

from os import system, remove
import numpy as np
import matplotlib.pyplot as plt

import RungeKutta as rk

start=0.0; end=0.00003#First and last time

N= 50000#Number of iterations. If it diverged increase this number 
NEqs=2 #Number of  coupled equations

w=range(N+1)

w=np.zeros((NEqs, N+1))
R0=4e-6#Initial bubble radius
mu_liquid=7.5e-3#Liquid viscosity
PB=190e6#Bubble initial pressure

w[0,0]=R0#Initial condition of the first equation
w[1,0]=0#Initial condition of the second equation

RK=rk.RungeKutta(start, end, N, NEqs,mu_liquid)#Initialise the object

RK.RK4Loop(w,R0,PB)#Call the solver

t = np.linspace(start, end, N+1)


plt.rc('text', usetex=False)#Write true if you have latex installed. with latex the graph is much fancier.
plt.rc('font', family='Serif')# If this does not work: sudo apt install msttcorefonts -qq   , then: rm 

plt.plot(t,w[0,:],linestyle="-",color="black",label="Bubble 1")

max1=max(w[0,:])

w=range(N+1)

w=np.zeros((NEqs, N+1))
R0=1.26e-6#Initial bubble radius
mu_liquid=7.5e-03#Liquid viscosity
PB=5e9#Bubble initial pressure
w[0,0]=R0#Initial condition of the first equation
w[1,0]=0#Initial condition of the second equation

RK=rk.RungeKutta(start, end, N, NEqs,mu_liquid)#Initialise the object

RK.RK4Loop(w,R0,PB)#Call the solver
plt.plot(t,w[0,:],linestyle=":",color="black",label="Bubble 2")
max2=max(w[0,:])
plt.xlabel(r"$t(s)$")
plt.ylabel(r"$r(m)$")
plt.legend()
plt.savefig("Radius.png")

print ("Maxim radius of the bubble 1: ",max1," Maxim radius of the bubble 2: ",max2)


plt.show()

