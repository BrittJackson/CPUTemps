#! /usr/bin/env python3
'''
Created on June 9, 2021

@author: Brittney Jackson
'''

import matplotlib.pyplot as plt
import numpy as np

def getTempData(core0, core1, core2, core3, step_size):
    
    """
    Grabs temperature data and time intervals for each core

    Args:
        core0, core1, core2, core3: Temp data for each core
        
        step_size: Time intervals in seconds
    """
    
    core_list = [core0, core1, core2, core3]
    
    core = 0
    
    for i, val in enumerate(core_list):
        interpolate(step_size, val, core)
        core +=1

def interpolate(x_val, y_val, core):

    """
    Performs linear interpolation

    Args:
        x_val: The time steps      
        y_val: The temperatures     
        core: The core for which the operations are being performed (i.e. core 1, 2, 3, or 4)
    """
    i = 0
    
    #iterates through each current time interval/temperature and the next time and temperature
    for cur_x, nxt_x, cur_y, nxt_y in zip (x_val, x_val[1:], y_val, y_val[1:]):
        x1 = cur_x
        x2 = nxt_x
        y1 = cur_y
        y2 = nxt_y
        
        #calculates the slope and y-intercept for the two (x,y) points
        m = (y2-y1)/(x2-x1)
        b = (-1)*(m)*(x1)+y1
        m = format(m, '.4f')
        b = format(b, '.4f')
        
        write_toFile(m, b, x1, x2, i, core)
        
        i+=1
    
    plot_graph(x_val,y_val,core)
    
def plot_graph(x, y, core):
    
    """
    Plots CPU temperatures and time in seconds for each core

    Args:
        x: The time steps      
        y: The temperatures     
        core: The core for which the operations are being performed (i.e. core 1, 2, 3, or 4)
    """
    
    plt.title('CPU Core Temperatures')
    plt.xlabel('Time in Seconds')
    plt.ylabel('Core Temperature')
    plt.scatter(x,y)
    plt.plot(x, y)
    
    if core == 3:
        plt.xticks(np.arange(min(x), max(x)+1, 60.0))
        plt.yticks(np.arange(min(y), max(y)+1, 10.0))
        plt.gca().legend(('core 0','core 1','core 2', 'core 3'))
        plt.show()   

def write_toFile(m, b, x1, x2, i, core):
    """
    Writes linear interpolation equations to respective core file

    Args:
        m: Slope of two points
        
        b: Y-intercept
        
        x1: Current time step
        
        x2: Next time step
        
        core: The core for which the operations are being performed (i.e. core 0, 1, 2, or 3)
    """
    if core == 0:
        f = open("cpuTemps-core-0.txt",'+a')
        f.write(str(x1)+' '+"<=x<"+' '+str(x2)+";"+' '+"y_%i=" %i+' '+str(b)+' '+"+" + " " +str(m)+"x"+";"+ " " + "interpolation"+"\n")
        f.close()
            
    elif core == 1:
        f = open("cpuTemps-core-1.txt",'+a')
        f.write(str(x1)+' '+"<=x<"+' '+str(x2)+";"+' '+"y_%i=" %i+' '+str(b)+' '+"+" + " " +str(m)+"x"+";"+ " " + "interpolation"+"\n")
        f.close()
           
    elif core == 2:
        f = open("cpuTemps-core-2.txt",'+a')
        f.write(str(x1)+' '+"<=x<"+' '+str(x2)+";"+' '+"y_%i=" %i+' '+str(b)+' '+"+" + " " +str(m)+"x"+";"+ " " + "interpolation"+"\n")
        f.close()
            
    elif core == 3:
        f = open("cpuTemps-core-3.txt",'+a')
        f.write(str(x1)+' '+"<=x<"+' '+str(x2)+";"+' '+"y_%i=" %i+' '+str(b)+' '+"+" + " " +str(m)+"x"+";"+ " " + "interpolation"+"\n")
        f.close()
    