############################################
#                                          #
#   Implicit Euler Method Implementation   #
#                Group: 73                 #
#                                          #
############################################
import numpy as np
import matplotlib.pyplot as plt

def implicit_euler(x0, y0, tmax, N):
    time = [0]
    R = [x0]
    J = [y0]
    h = tmax / N
    for k in range(N):
        time.append((k+1) * h)
        # Ex1
        # jk1 = (h**2+h*(J[k]+R[k])-1+np.sqrt((1-h*(J[k]+R[k])-h**2)**2-4*J[k]*(h-1)*(h+h**2)))/(2*(h+h**2))
        # rk1 = R[k]/(1-h*(1-jk1))
	    #
        # Ex2
        # jk1 = (-h*J[k]+2*h*R[k]+J[k])/(7*h**2-2*h+1)
        # rk1 = (R[k]-3*h*jk1)/(1-h)
	    #
        # Ex3
        # jk1 = (2*h*J[k]+h*R[k]+J[k])/(h**2+h+1)
        # rk1 = (R[k]-3*h*jk1)/(1+2*h)
	    #
        # Ex4
        # jk1 = (h*J[k]+6*h*R[k]-J[k])/(19*h**2-6*h-1)
        # rk1 = (R[k]-2*h*jk1)/(1-h)
	    # 
        # Ex5
        # jk1 = (-h*J[k]-6*h*R[k]+J[k])/(6*h**2+5*h+1)
        # rk1 = (R[k]+2*h*jk1)/(1-h)              
        R.append(rk1)
        J.append(jk1)
    return (R, J, time)

def draw_J(x0, y0, tmax, N):

    R, J, time = implicit_euler(x0, y0, tmax, N)
    plt.plot(time, J)
    plt.xlabel("time")
    plt.ylabel("J")
    plt.title("Plot of J")
    plt.show()

def draw_R(x0, y0, tmax, N):
   
    R, J, time = implicit_euler(x0, y0, tmax, N)
    plt.plot(time, R)
    plt.xlabel("time")
    plt.ylabel("R")
    plt.title("Plot of R")
    plt.show()

def draw_both(x0, y0, tmax, N):

    R, J, time = implicit_euler(x0, y0, tmax, N)
    pl=plt.figure()
    plt.grid()
    plt.plot(time, R, label = u"R")
    plt.plot(time, J, label = u"J")
    plt.legend(loc='best')
    plt.xlabel('time')
    plt.ylabel('J/R')
    plt.title("Plot of R and J")
    plt.show()

draw_both(1,1,20,100)
